# Git Commands for Contributors

This quick guide gives you the most useful commands for contributing to this repository.

## Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/open-source-contributors-wall.git
cd open-source-contributors-wall
```

## Create a Branch

```bash
git checkout -b add-YOUR_USERNAME
```

## Check What Changed

```bash
git status
```

## Add Your Contributor File

```bash
git add contributors/YOUR_USERNAME.json
```

## Commit

```bash
git commit -m "Add my profile to Open Source Contributors Wall"
```

## Push Your Branch

```bash
git push origin add-YOUR_USERNAME
```

## Validate Your JSON Quickly

```bash
python -m json.tool contributors/YOUR_USERNAME.json
```

## Run the Full Validator

```bash
python scripts/validate_contributors.py
```

## Unstage the Wrong File

```bash
git restore --staged path/to/wrong-file
```

## Rename Your Contributor File

Linux or macOS:

```bash
mv contributors/OldName.json contributors/newname.json
```

PowerShell:

```powershell
Rename-Item contributors/OldName.json newname.json
```

## Create Another Commit After Fixes

```bash
git add contributors/YOUR_USERNAME.json
git commit -m "Fix contributor profile"
git push origin add-YOUR_USERNAME
```

## Helpful Next Reads

- [README.md](../README.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)
- [LINKEDIN_POST_GUIDE.md](./LINKEDIN_POST_GUIDE.md)
