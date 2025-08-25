import requests
import json
import os

# ----------------------------
# Configuration
# ----------------------------
GROUP_ID = "859166638"  # Roblox group ID
OUTPUT_FILE = "staff.md"
STAFF_FOLDER = "Staff"  # Folder for individual staff pages

# Roles we want (highest rank first)
ROLE_IDS = [
    (496092058, "Creator"),
    (488634029, "Developer"),
    (479342092, "Administrator"),
    (483560069, "Senior Moderator"),
    (488738058, "Junior Moderator"),
]

# Ensure staff folder exists
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
        print(f"Fetching: {full_url}")

        r = requests.get(full_url)
        r.raise_for_status()
        data = r.json()

        # Add usernames directly
        members.extend([u['username'] for u in data.get('data', [])])

        if data.get('nextPageCursor'):
            cursor = data['nextPageCursor']
        else:
            break

    return members

def fetch_avatar_url(username):
    # Step 1: Get numeric UserId from username
    url = "https://users.roblox.com/v1/usernames/users"
    headers = {"Content-Type": "application/json"}
    payload = {
        "usernames": [username],
        "excludeBannedUsers": True
    }
    r = requests.post(url, headers=headers, json=payload)
    r.raise_for_status()
    data = r.json()
    user_data = next((item for item in data["data"] if item["requestedUsername"] == username), None)
    if not user_data:
        return "", None
    user_id = user_data["id"]

    # Step 2: Get avatar headshot
    thumb_url = f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={user_id}&size=420x420&format=Png&isCircular=false"
    r2 = requests.get(thumb_url)
    r2.raise_for_status()
    thumb_data = r2.json()
    if thumb_data.get("data") and len(thumb_data["data"]) > 0:
        return thumb_data["data"][0]["imageUrl"], user_id
    return "", user_id

def create_staff_page(username):
    path = os.path.join(STAFF_FOLDER, f"{username}.md")
    
    # If the file already exists, skip creation
    if os.path.exists(path):
        return path

    avatar_url, user_id = fetch_avatar_url(username)
    if user_id is None:
        return path

    profile_url = f"https://www.roblox.com/users/{user_id}/profile"

    page_content = f"""# {username}

## Main Info
<img class="" src="{avatar_url}" alt="{username}" style="width:128px;height:128px;">

## About
[{username}]({profile_url}) — Write a short bio here.

### Quote
<!-- Add a quote here -->

### Lore
<!-- Add lore here -->
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(page_content)

    return path

# ----------------------------
# Main
# ----------------------------
def main():
    staff_list = []

    for role_id, role_name in ROLE_IDS:
        members = fetch_members_by_role(GROUP_ID, role_id)
        if members:
            staff_list.append(f"## {role_name}\n")
            for m in members:
                staff_page_path = create_staff_page(m)
                # Make link relative to the root so docsify can find it
                staff_list.append(f"- [{m}]({staff_page_path})")
            staff_list.append("")  # empty line

    # Write staff.md
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(staff_list))

    total_members = sum(len(fetch_members_by_role(GROUP_ID, r[0])) for r in ROLE_IDS)
    print(f"✅ {OUTPUT_FILE} updated with {total_members} staff members")

if __name__ == "__main__":
    main()
