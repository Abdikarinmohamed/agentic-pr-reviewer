from agent.analyzer import analyze_diff
from agent.reviewer import refine_review
from agent.formatter import format_review_report


def run_review_workflow(diff_text: str) -> str:
    # Step 1: initial analysis
    initial_review = analyze_diff(diff_text)

    # Step 2: refinement (agent step)
    final_review = refine_review(initial_review)

    # Step 3: format output
    return format_review_report(final_review)