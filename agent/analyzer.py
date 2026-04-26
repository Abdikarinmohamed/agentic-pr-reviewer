from typing import Dict, List


def analyze_diff(diff_text: str) -> Dict[str, object]:
    lines = diff_text.split("\n")

    added_lines: List[str] = [line for line in lines if line.startswith("+") and not line.startswith("+++")]
    removed_lines: List[str] = [line for line in lines if line.startswith("-") and not line.startswith("---")]

    summary = "Code changes detected."
    risks = []
    edge_cases = []
    tests = []

    # Very basic logic (but REAL)
    if any("account_age" in line for line in added_lines):
        summary = "Introduced account_age-based logic for discount calculation."

        risks.append("account_age may be missing or None.")
        risks.append("Boundary conditions around account_age need validation.")

        edge_cases.extend([
            "account_age = 0",
            "account_age = 30",
            "account_age very large",
        ])

        tests.extend([
            "test_account_age_above_30_gets_correct_discount",
            "test_account_age_equal_30_boundary",
            "test_missing_account_age_handled",
        ])

    if any("if" in line and "and" in line for line in added_lines):
        risks.append("Complex conditional logic may introduce bugs.")

    return {
        "summary": summary,
        "risks": risks or ["No major risks detected."],
        "edge_cases": edge_cases or ["No edge cases identified."],
        "suggested_tests": tests or ["No tests suggested."],
        "risk_level": "Medium" if risks else "Low",
    }