"""index.html for GitHub Pages (BISPL-WM.github.io) from src/home.html, the page as published to the preview Artifact.

    python3 src/build.py
"""
import os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = open(f"{R}/src/home.html").read()
i = s.index("<header")
head = "\n".join(l for l in s[:i].split("\n") if "claude:" not in l)
ICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%2312151a'/%3E"
        "%3Cpath d='M4 16c2-9 4-9 6 0s3 9 5 0 2-9 4 0 2 9 3 0 1-9 2 0 1 9 2 0 1-9 2 0' fill='none' stroke='%23fff' stroke-width='1.8' stroke-linecap='round'/%3E%3C/svg%3E")
open(f"{R}/index.html", "w").write(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta property="og:title" content="BISPL-WM Projects">
<meta property="og:description" content="Project pages of BISPL-WM: GALILEO and Mind the Band.">
<meta property="og:url" content="https://bispl-wm.github.io/">
<link rel="icon" href="{ICON}">
{head}</head>
<body>
{s[i:]}</body>
</html>
""")
print("index.html", len(s))
