from pathlib import Path

from agent.workflow import run_review_workflow


def read_diff_file(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def main() -> None:
    diff_text = read_diff_file("sample_data/sample_diff.txt")
    report = run_review_workflow(diff_text)
    print(report)


if __name__ == "__main__":
    main()