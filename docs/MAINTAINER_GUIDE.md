# Maintainer Guide

This guide helps maintainers review pull requests consistently, quickly, and fairly.

## Accept a Pull Request When

- it adds exactly one JSON file
- the file is inside `contributors/`
- the file name matches the GitHub username in the `github` field
- the JSON passes schema validation
- the PR includes a LinkedIn post URL
- there are no unrelated file changes

## Request Changes When

- the JSON file is invalid
- required fields are missing
- URL formats are wrong
- the file name does not match the GitHub username
- the LinkedIn post URL is missing or malformed
- the contributor changed unrelated files

## Close a Pull Request When

- it contains spam
- it contains fake profiles
- it edits other contributors' files without reason
- it repeatedly ignores repository rules
- it exposes sensitive data

## Recommended Review Flow

1. Check the changed files list.
2. Confirm only one contributor JSON file was added.
3. Check that the PR description includes a LinkedIn post URL.
4. Run `python scripts/validate_contributors.py` locally if needed.
5. Confirm there are no unrelated file changes.
6. Approve or request changes with a clear explanation.

## Suggested Review Comment: Accepted

```text
Thanks for your contribution. Your JSON file follows the repository rules and is ready to merge.
```

## Suggested Review Comment: Changes Needed

```text
Thanks for opening this pull request. Please update it so it only adds one JSON file inside the contributors folder, includes a valid LinkedIn post URL, passes validation, and removes unrelated changes.
```

## Related Docs

- [README.md](../README.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)
- [GIT_COMMANDS.md](./GIT_COMMANDS.md)
- [REPO_AUTOMATION_GUIDE.md](./REPO_AUTOMATION_GUIDE.md)
