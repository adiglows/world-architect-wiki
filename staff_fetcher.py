import requests
import json

# ----------------------------
# Configuration
# ----------------------------
GROUP_ID = "859166638"  # replace with your Roblox group ID
OUTPUT_FILE = "staff.md"

# Roles we want (highest rank first)
ROLE_IDS = [
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

        # Log the raw API response
        print("API Response:", json.dumps(data, indent=2))

        # Add usernames directly (no nested 'user' field)
        members.extend([u['username'] for u in data.get('data', [])])

        if data.get('nextPageCursor'):
            cursor = data['nextPageCursor']
        else:
            break

    return members

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
                staff_list.append(f"- {m}")
            staff_list.append("")  # empty line

    # Write to file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(staff_list))

    total_members = sum(len(fetch_members_by_role(GROUP_ID, r[0])) for r in ROLE_IDS)
    print(f"✅ {OUTPUT_FILE} updated with {total_members} staff members")

if __name__ == "__main__":
    main()
