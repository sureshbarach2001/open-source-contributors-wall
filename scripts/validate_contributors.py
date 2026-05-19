import json
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema.json"
CONTRIBUTORS_DIR = ROOT / "contributors"


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON in {path}: {error}") from error


def main():
    schema = load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema)

    errors_found = False
    contributor_files = sorted(CONTRIBUTORS_DIR.glob("*.json"))

    if not contributor_files:
        print("No contributor files found.")
        raise SystemExit(1)

    for file_path in contributor_files:
        try:
            data = load_json(file_path)
        except ValueError as error:
            print(error)
            errors_found = True
            continue

        schema_errors = sorted(validator.iter_errors(data), key=lambda e: e.path)

        if schema_errors:
            errors_found = True
            print(f"Schema errors in {file_path}:")
            for error in schema_errors:
                field = ".".join(str(part) for part in error.path) or "root"
                print(f"  - {field}: {error.message}")

        github_url = data.get("github", "")
        expected_username = file_path.stem.lower()

        if github_url:
            github_username = github_url.rstrip("/").split("/")[-1].lower()
            if github_username != expected_username and file_path.name != "example.json":
                errors_found = True
                print(
                    f"Filename mismatch in {file_path}: "
                    f"file name should match GitHub username '{github_username}'."
                )

    if errors_found:
        raise SystemExit(1)

    print("All contributor files are valid.")


if __name__ == "__main__":
    main()
