import requests
import json
import os

# ----------------------------
# Configuration
# ----------------------------
GROUP_ID = "859166638"  # Roblox group ID
OUTPUT_FILE = "staff.md"
STAFF_FOLDER = "Staff"  # folder for individual staff pages

# Roles we want (highest rank first)
ROLE_IDS = [
    (496092058, "Creator"),
    (488634029, "Developer"),
    (479342092, "Administrator"),
    (483560069, "Senior Moderator"),
    (488738058, "Junior Moderator"),
]

# ----------------------------
# Helper Functions
# ----------------------------
def fetch_members_by_role(group_id, role_id):
    url = f"https://groups.roblox.com/v1/groups/{group_id}/roles/{role_id}/users"
    members = []
    cursor = ""

    while True:
        full_url = url + (f"?cursor={cursor}" if cursor else "")
        print(f"Fetching: {full_url}")  # Log request URL

        r = requests.get(full_url)
        r.raise_for_status()
        data = r.json()

        print("API Response:", json.dumps(data, indent=2))  # Log API response

        members.extend([u['username'] for u in data.get('data', [])])

        if data.get('nextPageCursor'):
            cursor = data['nextPageCursor']
        else:
            break

    return members

def create_staff_page(username):
    """Create individual staff page if it doesn't exist."""
    os.makedirs(STAFF_FOLDER, exist_ok=True)
    filename = os.path.join(STAFF_FOLDER, f"{username}.md")
    if os.path.exists(filename):
        return  # Don't overwrite existing page

    template = f"""# {username}

## Main Info
<img class="" src="https://t2.rbxcdn.com/30DAY-AvatarHeadshot-17441E080E9DD79F37219DC82B709BB6-Png" alt="{username}" style="width:128px;height:128px;">

## About
[{username}](https://www.roblox.com/users/USERID/profile) (AKA) ... description goes here ...

### Quote
said, `"Insert quote here..."`

### Lore
Insert lore or story here...
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(template)

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
                create_staff_page(m)
                staff_list.append(f"- [{m}]({STAFF_FOLDER}/{m}.md)")
            staff_list.append("")  # empty line

    # Write to staff.md
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(staff_list))

    total_members = sum(len(fetch_members_by_role(GROUP_ID, r[0])) for r in ROLE_IDS)
    print(f"✅ {OUTPUT_FILE} updated with {total_members} staff members")

if __name__ == "__main__":
    main()
