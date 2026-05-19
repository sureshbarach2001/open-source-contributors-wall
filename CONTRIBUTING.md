# Contributing to Open Source Contributors Wall

This repository is built to help beginners make a clean first open-source contribution.

## Contribution Steps

### 1. Fork the repository

Use the `Fork` button on GitHub.

### 2. Clone your fork

```bash
git clone https://github.com/YOUR_USERNAME/open-source-contributors-wall.git
cd open-source-contributors-wall
```

### 3. Create a branch

```bash
git checkout -b add-YOUR_USERNAME
```

### 4. Add your contributor file

Create exactly one file inside `contributors/`.

```text
contributors/YOUR_USERNAME.json
```

### 5. Use this format

```json
{
  "name": "Your Full Name",
  "country": "Your Country",
  "role": "Your Role",
  "github": "https://github.com/YOUR_USERNAME",
  "linkedin": "https://www.linkedin.com/in/YOUR_LINKEDIN_USERNAME",
  "portfolio": "https://your-portfolio.com",
  "highlight": "One short line about your skills or open-source journey."
}
```

### 6. Commit and push

```bash
git add contributors/YOUR_USERNAME.json
git commit -m "Add my profile to Open Source Contributors Wall"
git push origin add-YOUR_USERNAME
```

### 7. Create a LinkedIn post

Before opening your pull request, create a public LinkedIn post about your contribution.

Your post should include:

- a short note about your contribution
- the repository link
- what you learned from the contribution flow

Use [docs/LINKEDIN_POST_GUIDE.md](./docs/LINKEDIN_POST_GUIDE.md) if you want a ready-to-use format.

### 8. Open a pull request

Open your PR to this repository after pushing your branch.

Make sure you paste your LinkedIn post URL in the pull request description.

## Rules

- Add only one JSON file
- Keep it inside `contributors/`
- Use your GitHub username as the file name
- Do not edit another contributor's file
- Do not add unrelated files or changes
- Use real public profile details only

## Helpful Docs

- [README.md](./README.md)
- [docs/GIT_COMMANDS.md](./docs/GIT_COMMANDS.md)
- [docs/LINKEDIN_POST_GUIDE.md](./docs/LINKEDIN_POST_GUIDE.md)
- [contributors/example.json](./contributors/example.json)
