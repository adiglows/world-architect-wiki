import requests
import os

# ----------------------------
# Configuration
# ----------------------------
GITHUB_REPO = "adiglows/world-architect-wiki"
OUTPUT_FILE = "wiki_team.md"
WIKI_TEAM_FOLDER = "Wiki_Team"
LEADER_USERNAME = "adiglows"

os.makedirs(WIKI_TEAM_FOLDER, exist_ok=True)

# ----------------------------
# Helper Functions
# ----------------------------
def fetch_github_contributors(repo):
    r = requests.get(f"https://api.github.com/repos/{repo}/contributors")
    r.raise_for_status()
    return r.json()

def create_wiki_team_page(username, avatar_url, profile_url):
    path = os.path.join(WIKI_TEAM_FOLDER, f"{username}.md")
    if os.path.exists(path):
        return path
    content = f"""# {username}

## Main Info
<img src="{avatar_url}" alt="{username}" style="width:128px;height:128px;">

## Contact
[{username}]({profile_url}) — Write Roblox link here.

### Bio
<!-- Add a bio here -->
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path

# ----------------------------
# Main
# ----------------------------
def main():
    contributors = fetch_github_contributors(GITHUB_REPO)
    md_lines = []

    # Leader
    leader = next((c for c in contributors if c["login"] == LEADER_USERNAME), None)
    if leader:
        path = create_wiki_team_page(leader["login"], leader["avatar_url"], leader["html_url"])
        md_lines.append("## Wiki Team Leader\n<div class=\"block-grid\">")
        md_lines.append(f"""
  <div class="block-item">
    <a href="#/{path}">
      <img src="{leader['avatar_url']}" alt="{leader['login']}">
      <p>{leader['login']}</p>
    </a>
    <!-- VSCode nav: [{path}]({path}) -->
  </div>""")
        md_lines.append("</div>\n")

    # Other contributors
    others = [c for c in contributors if c["login"] != LEADER_USERNAME]
    if others:
        md_lines.append("## Contributors\n<div class=\"block-grid\">")
        for c in others:
            path = create_wiki_team_page(c["login"], c["avatar_url"], c["html_url"])
            md_lines.append(f"""
  <div class="block-item">
    <a href="#/{path}">
      <img src="{c['avatar_url']}" alt="{c['login']}">
      <p>{c['login']}</p>
    </a>
    <!-- VSCode nav: [{path}]({path}) -->
  </div>""")
        md_lines.append("</div>\n")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"✅ {OUTPUT_FILE} updated with {len(contributors)} members")

if __name__ == "__main__":
    main()
