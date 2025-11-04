import re, sys, json, yaml, pathlib, urllib.request

TIMEOUT = 8
OK = {200, 206, 301, 302, 307, 308}

def head(url):
    req = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status
    except Exception:
        # 有些站点不支持 HEAD，尝试 GET
        try:
            with urllib.request.urlopen(url, timeout=TIMEOUT) as r:
                return r.status
        except Exception:
            return None

def extract_md_links(text):
    # [title](url) & bare links
    urls = re.findall(r"\]\((https?://[^\s)]+)\)", text) + re.findall(r"\bhttps?://[^\s)]+", text)
    return sorted(set(urls))

def extract_structured_links(p):
    links = []
    if p.suffix == ".yaml" or p.suffix == ".yml":
        data = yaml.safe_load(p.read_text(encoding="utf-8"))
    else:
        data = json.loads(p.read_text(encoding="utf-8"))
    for item in data:
        u = item.get("url", {})
        for k in ("primary","paper","home"):
            v = u.get(k)
            if v: links.append(v)
    return sorted(set(links))

def main():
    root = pathlib.Path(".")
    md_files = list(root.glob("README.md")) + list(root.glob("categories/*.md"))
    urls = set()
    for f in md_files:
        urls.update(extract_md_links(f.read_text(encoding="utf-8")))
    for f in [*root.glob("datasets.yaml"), *root.glob("datasets.json")]:
        urls.update(extract_structured_links(f))
    print(f"Found {len(urls)} urls")
    bad = []
    for u in sorted(urls):
        status = head(u)
        ok = status in OK
        print(f"[{'OK' if ok else 'BAD'}] {u} ({status})")
        if not ok:
            bad.append((u, status))
    if bad:
        print("\nBroken links:")
        for u, s in bad:
            print(f"- {u} ({s})")
        sys.exit(1)

if __name__ == "__main__":
    main()
