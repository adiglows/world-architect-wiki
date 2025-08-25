import requests
import os

# ----------------------------
# Configuration
# ----------------------------
GITHUB_REPO = "adiglows/world-architect-wiki"
OUTPUT_FILE = "wiki_team.md"
WIKI_TEAM_FOLDER = "Wiki_Team"
LEADER_USERNAME = "adiglows"

# Ensure folder exists
os.makedirs(WIKI_TEAM_FOLDER, exist_ok=True)

# ----------------------------
# Helper Functions
# ----------------------------
def fetch_github_contributors(repo):
    url = f"https://api.github.com/repos/{repo}/contributors"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()

def create_wiki_team_page(username, avatar_url, profile_url):
    path = os.path.join(WIKI_TEAM_FOLDER, f"{username}.md")
    if os.path.exists(path):
        return path

    page_content = f"""# {username}

## Main Info
<img class="" src="{avatar_url}" alt="{username}" style="width:128px;height:128px;">

## Contact
[{username}]({profile_url}) — Write Roblox link here.

### Bio
<!-- Add a bio here -->
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(page_content)

    return path

# ----------------------------
# Main
# ----------------------------
def main():
    wiki_team_list = []

    contributors = fetch_github_contributors(GITHUB_REPO)

    # Separate leader and contributors
    leader = [c for c in contributors if c["login"] == LEADER_USERNAME]
    others = [c for c in contributors if c["login"] != LEADER_USERNAME]

    # Leader section
    if leader:
        l = leader[0]
        page_path = create_wiki_team_page(l["login"], l["avatar_url"], l["html_url"])
        wiki_team_list.append("## Wiki Team Leader\n")
        wiki_team_list.append(f"- [{l['login']}]({page_path})\n")

    # Contributors section
    if others:
        wiki_team_list.append("## Contributors\n")
        for c in others:
            page_path = create_wiki_team_page(c["login"], c["avatar_url"], c["html_url"])
            wiki_team_list.append(f"- [{c['login']}]({page_path})")
        wiki_team_list.append("")

    # Write wiki_team.md
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(wiki_team_list))

    print(f"✅ {OUTPUT_FILE} updated with {len(contributors)} members")

if __name__ == "__main__":
    main()
