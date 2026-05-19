import json
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
CONTRIBUTORS_DIR = ROOT / "contributors"
START_MARKER = "<!-- CONTRIBUTORS-WALL:START -->"
END_MARKER = "<!-- CONTRIBUTORS-WALL:END -->"
CARDS_PER_ROW = 4
PINNED_USERNAMES = ["sureshbarach2001"]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def github_username_from_url(url: str) -> str:
    return url.rstrip("/").split("/")[-1]


def load_contributors():
    contributors = []
    for file_path in sorted(CONTRIBUTORS_DIR.glob("*.json")):
        if file_path.name == "example.json":
            continue

        data = load_json(file_path)
        username = github_username_from_url(data["github"])
        contributors.append(
            {
                "name": data["name"],
                "country": data["country"],
                "role": data["role"],
                "github": data["github"],
                "username": username,
            }
        )

    contributors.sort(
        key=lambda contributor: (
            contributor["username"].lower() not in PINNED_USERNAMES,
            PINNED_USERNAMES.index(contributor["username"].lower())
            if contributor["username"].lower() in PINNED_USERNAMES
            else len(PINNED_USERNAMES),
            contributor["username"].lower(),
        )
    )

    return contributors


def build_card(contributor: Dict[str, str]) -> str:
    return "\n".join(
        [
            "<td align='center' width='200px'>",
            f"  <a href='{contributor['github']}'>",
            (
                f"    <img src='https://github.com/{contributor['username']}.png?size=160' "
                f"width='96px' alt='{contributor['name']}' style='border-radius: 50%;'><br>"
            ),
            f"    <sub><b>{contributor['name']}</b></sub>",
            "  </a><br>",
            f"  <sub>{contributor['role']}</sub><br>",
            f"  <sub>{contributor['country']}</sub>",
            "</td>",
        ]
    )


def build_wall(contributors: List[Dict[str, str]]) -> str:
    if not contributors:
        return "\n".join(
            [
                "<p align='center'>",
                "<sub>No contributors yet. Be the first one to add your card.</sub>",
                "</p>",
            ]
        )

    lines = ["<p align='center'>", "<table>"]

    for index in range(0, len(contributors), CARDS_PER_ROW):
        lines.append("<tr>")
        for contributor in contributors[index : index + CARDS_PER_ROW]:
            lines.append(build_card(contributor))
        lines.append("</tr>")

    lines.extend(["</table>", "</p>"])
    return "\n".join(lines)


def replace_section(readme: str, new_section: str) -> str:
    start = readme.find(START_MARKER)
    end = readme.find(END_MARKER)

    if start == -1 or end == -1:
        raise ValueError("Contributor wall markers were not found in README.md")

    end += len(END_MARKER)
    replacement = f"{START_MARKER}\n{new_section}\n{END_MARKER}"
    return readme[:start] + replacement + readme[end:]


def main():
    contributors = load_contributors()
    wall = build_wall(contributors)
    readme = README_PATH.read_text(encoding="utf-8")
    updated_readme = replace_section(readme, wall)
    README_PATH.write_text(updated_readme, encoding="utf-8")
    print(f"Updated contributor wall with {len(contributors)} contributor(s).")


if __name__ == "__main__":
    main()
