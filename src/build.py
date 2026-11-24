"""index.html for GitHub Pages (BISPL-WM.github.io) from src/home.html, the page as published to the preview Artifact.

    python3 src/build.py
"""
import os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = open(f"{R}/src/home.html").read()
i = s.index("<header")
head = "\n".join(l for l in s[:i].split("\n") if "claude:" not in l)
open(f"{R}/index.html", "w").write(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{head}</head>
<body>
{s[i:]}</body>
</html>
""")
print("index.html", len(s))
