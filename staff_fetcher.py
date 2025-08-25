import requests
import json
import os

# ----------------------------
# Configuration
# ----------------------------
GROUP_ID = "859166638"  # Roblox group ID
OUTPUT_FILE = "staff.md"
STAFF_FOLDER = "Staff"  # Folder for individual staff pages

ROLE_IDS = [
    (496092058, "Creator"),
    (488634029, "Developer"),
    (479342092, "Administrator"),
    (483560069, "Senior Moderator"),
    (488738058, "Junior Moderator"),
]

os.makedirs(STAFF_FOLDER, exist_ok=True)

# ----------------------------
# Helper Functions
# ----------------------------
def fetch_members_by_role(group_id, role_id):
    url = f"https://groups.roblox.com/v1/groups/{group_id}/roles/{role_id}/users"
    members = []
    cursor = ""

    while True:
        full_url = url + (f"?cursor={cursor}" if cursor else "")
        r = requests.get(full_url)
        r.raise_for_status()
        data = r.json()
        members.extend([u['username'] for u in data.get('data', [])])
        cursor = data.get('nextPageCursor')
        if not cursor:
            break
    return members

def fetch_avatar_url(username):
    url = "https://users.roblox.com/v1/usernames/users"
    r = requests.post(url, json={"usernames":[username], "excludeBannedUsers":True})
    r.raise_for_status()
    data = r.json()
    user_data = next((x for x in data["data"] if x["requestedUsername"] == username), None)
    if not user_data:
        return "", None
    user_id = user_data["id"]
    thumb_url = f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={user_id}&size=420x420&format=Png&isCircular=false"
    r2 = requests.get(thumb_url)
    r2.raise_for_status()
    thumb_data = r2.json()
    avatar_url = thumb_data["data"][0]["imageUrl"] if thumb_data.get("data") else ""
    return avatar_url, user_id

def create_staff_page(username):
    path = os.path.join(STAFF_FOLDER, f"{username}.md")
    if os.path.exists(path):
        return path
    avatar_url, user_id = fetch_avatar_url(username)
    profile_url = f"https://www.roblox.com/users/{user_id}/profile" if user_id else "#"
    content = f"""# {username}

## Main Info
<img src="{avatar_url}" alt="{username}" style="width:128px;height:128px;">

## About
[{username}]({profile_url}) — Write a short bio here.

### Quote
<!-- Add a quote here -->

### Lore
<!-- Add lore here -->
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path

# ----------------------------
# Main
# ----------------------------
def main():
    md_lines = []
    for role_id, role_name in ROLE_IDS:
        members = fetch_members_by_role(GROUP_ID, role_id)
        if not members:
            continue
        md_lines.append(f"## {role_name}\n")
        md_lines.append('<div class="block-grid">')
        for m in members:
            page_path = create_staff_page(m)
            avatar_url, _ = fetch_avatar_url(m)
            md_lines.append(f"""
  <div class="block-item">
    <a href="#/{page_path}">
      <img src="{avatar_url}" alt="{m}">
      <p>{m}</p>
    </a>
    <!-- VSCode nav: [{page_path}]({page_path}) -->
  </div>""")
        md_lines.append("</div>\n")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f"✅ {OUTPUT_FILE} updated")

if __name__ == "__main__":
    main()
