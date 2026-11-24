import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

DEFAULT_SECURITY_CHECKS: Dict[str, bool] = {
    "Strong password policy": True,
    "Multi-factor authentication": False,
    "Firewall enabled": True,
    "Regular software updates": False,
    "Antivirus protection": True,
    "Data backup enabled": True,
    "Unused accounts disabled": False,
}


def load_checks(input_path: Optional[Path]) -> Dict[str, bool]:
    """Load security checks from a JSON file, or return the default sample checks."""
    if input_path is None:
        return DEFAULT_SECURITY_CHECKS

    try:
        raw_data = json.loads(input_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"Error reading input file '{input_path}': {error}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(raw_data, dict) or not raw_data:
        print("Input JSON must be a non-empty object mapping check names to booleans.", file=sys.stderr)
        sys.exit(1)

    return {str(key): bool(value) for key, value in raw_data.items()}


def get_rating(score: float) -> str:
    """Map a percentage score to a security rating."""
    if score >= 85:
        return "Good"
    if score >= 60:
        return "Moderate"
    return "Poor"


def evaluate_checks(checks: Dict[str, bool]) -> Tuple[int, List[str], float, str]:
    """Print check results and return (passed_count, failed_checks, score, rating)."""
    passed_checks = 0
    failed_checks: List[str] = []

    print("\n===== SECURITY CHECK RESULTS =====")
    for check, status in checks.items():
        if status:
            print(f"[PASS] {check}")
            passed_checks += 1
        else:
            print(f"[FAIL] {check}")
            failed_checks.append(check)

    total_checks = len(checks)
    score = round((passed_checks / total_checks) * 100, 2)
    rating = get_rating(score)
    return passed_checks, failed_checks, score, rating


def build_report(score: float, rating: str, failed_checks: List[str], fmt: str) -> str:
    """Format the audit report as plain text or Markdown."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if fmt == "md":
        lines = [
            "# Security Audit Report",
            "",
            f"- **Date:** {timestamp}",
            f"- **Security Score:** {score}%",
            f"- **Security Rating:** {rating}",
            "",
            "## Failed Security Checks",
        ]
        lines.extend([f"- {item}" for item in failed_checks] if failed_checks else ["- No failed checks."])
        lines.extend(["", "## Recommendations"])
        lines.extend(
            [f"- Review and improve: {item}" for item in failed_checks]
            if failed_checks
            else ["- All baseline checks passed."]
        )
        return "\n".join(lines) + "\n"

    lines = [
        "===== SECURITY AUDIT REPORT =====",
        f"Date: {timestamp}",
        f"Security Score: {score}%",
        f"Security Rating: {rating}",
        "\nFailed Security Checks:",
    ]
    lines.extend([f"- {item}" for item in failed_checks] if failed_checks else ["No failed checks."])
    lines.append("\nRecommendations:")
    lines.extend(
        [f"- Review and improve: {item}" for item in failed_checks]
        if failed_checks
        else ["All baseline checks passed."]
    )
    lines.append("\nAudit completed.")
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Evaluate security posture checks and generate an audit report."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        default=None,
        help="Path to a JSON file of check_name: boolean pairs (default: built-in sample)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("security_audit_report.txt"),
        help="Output report file path (default: security_audit_report.txt)",
    )
    parser.add_argument(
        "--format",
        choices=["txt", "md"],
        default="txt",
        help="Report output format: 'txt' or 'md' (default: txt)",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    print("===== SECURITY AUDIT REPORT GENERATOR =====")

    checks = load_checks(args.input)
    passed_checks, failed_checks, score, rating = evaluate_checks(checks)

    print("\n===== SECURITY SUMMARY =====")
    print(f"Total Checks: {len(checks)}")
    print(f"Passed Checks: {passed_checks}")
    print(f"Failed Checks: {len(failed_checks)}")
    print(f"Security Score: {score}%")
    print(f"Security Rating: {rating}")

    report_content = build_report(score, rating, failed_checks, args.format)
    args.output.write_text(report_content, encoding="utf-8")

    print("\nAudit report generated successfully!")
    print(f"File: {args.output}")


if __name__ == "__main__":
    main()
