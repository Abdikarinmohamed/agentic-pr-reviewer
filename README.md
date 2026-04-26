# Agentic PR Reviewer

A tool that analyzes code diffs and generates PR-style reviews including risks and test cases.

---

## What It Does

Given a code diff, it:
- Summarizes the change
- Identifies risks
- Suggests edge cases
- Generates unit tests

---

## How to Run

Run:
python main.py

This will:
- Read a diff from sample_data/sample_diff.txt
- Generate a review
- Save it to outputs/review.md

---

## Example Input (Diff)

```diff
- if user.is_premium:
-     return 0.2
+ if user.is_premium and user.account_age > 30:
+     return 0.2
+ elif user.is_premium:
+     return 0.1
```

---

## Example Output

Summary:
Modified discount logic to include account age

Risks:
- Missing account_age field
- Boundary condition at 30

Suggested Tests:
- test_account_age_boundary
- test_missing_account_age

---

## Architecture

diff → analyze → refine → format → output

---

## Limitations

- Does not connect to GitHub
- Requires diff input
- Uses rule-based logic unless AI is enabled

---

## Future Improvements

- GitHub API integration
- Better AI reasoning
- Auto test generation
