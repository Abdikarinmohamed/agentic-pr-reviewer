from typing import Dict, List


def format_review_report(review: Dict[str, object]) -> str:
    risks: List[str] = review["risks"]
    edge_cases: List[str] = review["edge_cases"]
    tests: List[str] = review["suggested_tests"]

    return f"""
# AI PR Review Report

## Summary
{review["summary"]}

## Potential Risks
{chr(10).join(f"- {risk}" for risk in risks)}

## Edge Cases
{chr(10).join(f"- {case}" for case in edge_cases)}

## Suggested Tests
{chr(10).join(f"- {test}" for test in tests)}

## Risk Level
{review["risk_level"]}
""".strip()