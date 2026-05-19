import json
import os
import re
from pathlib import Path


LINKEDIN_POST_PATTERNS = [
    re.compile(r"https://(?:www\.)?linkedin\.com/posts/[^\s)]+", re.IGNORECASE),
    re.compile(
        r"https://(?:www\.)?linkedin\.com/feed/update/urn:li:activity:[^\s)]+",
        re.IGNORECASE,
    ),
]


def load_event_payload():
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        raise ValueError("GITHUB_EVENT_PATH is not set.")

    path = Path(event_path)
    if not path.is_file():
        raise ValueError(f"GitHub event payload file was not found: {path}")

    return json.loads(path.read_text(encoding="utf-8"))


def extract_pr_body(payload: dict) -> str:
    pull_request = payload.get("pull_request")
    if not pull_request:
        raise ValueError("This script must run on a pull_request event.")

    return pull_request.get("body") or ""


def find_linkedin_post_url(pr_body: str) -> str | None:
    for pattern in LINKEDIN_POST_PATTERNS:
        match = pattern.search(pr_body)
        if match:
            return match.group(0)
    return None


def main():
    payload = load_event_payload()
    pr_body = extract_pr_body(payload)
    linkedin_post_url = find_linkedin_post_url(pr_body)

    if not linkedin_post_url:
        print("LinkedIn post validation failed.")
        print("Add a valid LinkedIn post URL in your pull request description.")
        print("Accepted formats include:")
        print("- https://www.linkedin.com/posts/...")
        print("- https://www.linkedin.com/feed/update/urn:li:activity:...")
        raise SystemExit(1)

    print("LinkedIn post URL found in pull request description:")
    print(linkedin_post_url)


if __name__ == "__main__":
    main()
