import sys
import requests

HEADERS={"User-Agent":"macos:com.alu.subredditinfo:v1.0 (by /u/mmarvellio7)"}

def get(sub, path,**params):
    url=f"https://www.reddit.com/r/{sub}/{path}.json"
    try:
        r=requests.get(url, headers=HEADERS, params=params, allow_redirects=False, timeout=10)

    except requests.RequestException as e:
        sys.exit(f"Error: could not reach Reddit({e})")
    if r.status_code!=200:
        sys.exit(f"Error: request failed with status {r.status_code}")
    return r.json()

sub=sys.argv[1] if len(sys.argv)> 1 else "python"

about=get(sub, "about")["data"]
print("Subreddit:", about["display_name"])
print("Subscribers:", about["subscribers"])
print("Description:", about["public_description"])

print("\n10 newest posts:")
for post in get(sub, "new", limit=10)["data"]["children"]:
    print("-", post["data"]["title"])

print("\nRules:")
for rule in get(sub, "about/rules")["rules"]:
    print("-", rule["short_name"])