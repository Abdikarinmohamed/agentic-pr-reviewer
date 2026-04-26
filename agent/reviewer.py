import os
from typing import Dict
from dotenv import load_dotenv
from openai import OpenAI

USE_AI = False  # 🔁 turn ON later when billing is ready


def refine_review(review: Dict[str, object]) -> Dict[str, object]:
    """
    Second pass: refine review using AI (or fallback to rule-based)
    """

    if not USE_AI:
        return fallback_refine(review)

    load_dotenv()
    client = OpenAI()

    prompt = f"""
You are an expert software engineer reviewing a PR analysis.

Improve the following review:
- Make risks more precise
- Add missing edge cases
- Improve test suggestions
- Adjust risk level if needed

Return ONLY structured JSON with keys:
summary, risks, edge_cases, suggested_tests, risk_level

Review:
{review}
"""

    response = client.responses.create(
        model="gpt-5.4",
        input=prompt,
    )

    try:
        import json
        return json.loads(response.output_text)
    except Exception:
        return fallback_refine(review)


def fallback_refine(review: Dict[str, object]) -> Dict[str, object]:
    risks = review["risks"][:]
    tests = review["suggested_tests"][:]

    if "account_age may be missing or None." in risks:
        tests.append("test_null_account_age_does_not_crash")

    tests = list(set(tests))

    risk_level = "High" if len(risks) > 3 else review["risk_level"]

    return {
        "summary": review["summary"],
        "risks": risks,
        "edge_cases": review["edge_cases"],
        "suggested_tests": tests,
        "risk_level": risk_level,
    }