# Repository Automation and Validation Guide

This document is for repository owners and maintainers. It explains how contributor validation works, how the contributor wall is generated, which commands are used, and how the GitHub Actions flow updates the repository automatically.

## Repository Flow

The repository follows this process:

1. A contributor opens a pull request with one JSON file inside `contributors/`
2. The contributor includes a LinkedIn post URL in the pull request description
3. GitHub Actions validates the contribution automatically
4. GitHub Actions validates the LinkedIn post URL format in the pull request body
5. If the pull request is merged into `main` or `master`, the contributor wall is regenerated
6. GitHub Actions commits the updated `README.md` automatically if the wall changed

## Validation Script

Script:

```text
scripts/validate_contributors.py
```

This script checks:

- the JSON file is readable
- the profile matches `schema.json`
- the GitHub URL is present and correctly formatted for the expected username
- the file name matches the GitHub username from the `github` field

## Contributor Wall Script

Script:

```text
scripts/generate_contributors_wall.py
```

This script:

- reads all `contributors/*.json` files except `example.json`
- extracts the contributor name, country, role, and GitHub username
- builds the HTML contributor card wall
- replaces the section between:

```text
<!-- CONTRIBUTORS-WALL:START -->
<!-- CONTRIBUTORS-WALL:END -->
```

- writes the updated content back into `README.md`

## Local Commands

### Check Python

```bash
python --version
```

If needed:

```bash
py --version
```

### Install validation dependency

```bash
pip install jsonschema
```

Or:

```bash
py -m pip install jsonschema
```

### Validate contributor files locally

```bash
python scripts/validate_contributors.py
```

Or:

```bash
py scripts/validate_contributors.py
```

### Validate pull request LinkedIn metadata locally

This script reads the pull request event payload provided by GitHub Actions:

```bash
python scripts/validate_pr_metadata.py
```

In GitHub Actions it checks the PR description and confirms that a LinkedIn post URL is present in one of these formats:

- `https://www.linkedin.com/posts/...`
- `https://www.linkedin.com/feed/update/urn:li:activity:...`

### Regenerate the contributor wall locally

```bash
python scripts/generate_contributors_wall.py
```

Or:

```bash
py scripts/generate_contributors_wall.py
```

## GitHub Actions Workflows

### Pull request validation workflow

File:

```text
.github/workflows/validate-contributors.yml
```

This workflow runs on pull requests when these files change:

- `contributors/*.json`
- `schema.json`
- `scripts/validate_contributors.py`
- `scripts/validate_pr_metadata.py`
- `scripts/generate_contributors_wall.py`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `CONTRIBUTING.md`
- `docs/LINKEDIN_POST_GUIDE.md`

It performs these steps:

1. Checks out the repository
2. Sets up Python 3.11
3. Installs `jsonschema`
4. Runs `python scripts/validate_contributors.py`
5. Runs `python scripts/validate_pr_metadata.py`
6. Runs `python scripts/generate_contributors_wall.py`

Purpose:

- reject invalid contributor data before merge
- reject pull requests that do not include a LinkedIn post URL
- catch schema issues early
- confirm the contributor wall can still be built successfully

## LinkedIn Verification Scope

The automated LinkedIn check validates:

- a LinkedIn post URL exists in the pull request description
- the URL matches an accepted LinkedIn post format

The automated check does not validate:

- whether the post content is meaningful
- whether the post is still publicly visible to every viewer
- whether the post text includes specific wording

If deeper manual review is needed, maintainers can open the URL from the PR description.

### Contributor wall update workflow

File:

```text
.github/workflows/update-contributor-wall.yml
```

This workflow runs on pushes to `main` or `master` when these files change:

- `contributors/*.json`
- `schema.json`
- `scripts/generate_contributors_wall.py`

It performs these steps:

1. Checks out the repository with write access
2. Sets up Python 3.11
3. Runs `python scripts/generate_contributors_wall.py`
4. Stages `README.md`
5. Commits the change if there is an update
6. Pushes the commit back to the repository

Purpose:

- keep the contributor wall in sync automatically
- remove manual README maintenance
- ensure every merged valid contributor appears on the wall

## Required README Marker

The wall generator depends on these markers inside `README.md`:

```text
<!-- CONTRIBUTORS-WALL:START -->
<!-- CONTRIBUTORS-WALL:END -->
```

If these markers are removed or renamed, the generator will fail.

## Recommended Maintainer Checklist

Before enabling this setup in a new repository, confirm:

- Python scripts exist in `scripts/`
- `schema.json` matches the contributor format you want
- `README.md` includes the contributor wall markers
- GitHub Actions are enabled for the repository
- the default branch name matches `main` or `master`, or the workflow is updated accordingly
- the repository allows GitHub Actions to push commits

## Suggested Setup Order for a New Repository

1. Add `contributors/example.json`
2. Add `schema.json`
3. Add `scripts/validate_contributors.py`
4. Add `scripts/generate_contributors_wall.py`
5. Add the contributor wall markers to `README.md`
6. Add `.github/workflows/validate-contributors.yml`
7. Add `.github/workflows/update-contributor-wall.yml`
8. Test validation locally
9. Test wall generation locally
10. Push to GitHub and test with a sample pull request

## Related Files

- [README.md](../README.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)
- [GIT_COMMANDS.md](./GIT_COMMANDS.md)
- [MAINTAINER_GUIDE.md](./MAINTAINER_GUIDE.md)
