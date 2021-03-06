from scripts.changed.category import get_category
from scripts.helpers.hacs_manifest import get_hacs_manifest


def check():
    print("Information: https://hacs.xyz/docs/publish/include#check-hacs-manifest")
    if get_category() != "integration":
        print("Only integrations are checked.")
        return

    manifest = get_hacs_manifest()
    issues = []

    if manifest.get("name") is None:
        issues.append("No name")

    if issues:
        for issue in issues:
            print(issue)
        exit(1)


if __name__ == "__main__":
    check()
