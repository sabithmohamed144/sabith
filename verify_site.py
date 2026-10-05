import os
import re

base = r"c:\Users\acer\Documents\Custom Office Templates\mohamedsabith.portfolio.com"
broken_assets = []
scanned_assets = set()

for r, d, fs in os.walk(base):
    for f in fs:
        if f.endswith('.html'):
            p = os.path.join(r, f)
            with open(p, 'r', encoding='utf-8') as fp:
                c = fp.read()
            
            # Find all script src
            for src in re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', c):
                if src.startswith('http'):
                    continue
                scanned_assets.add(src)
                if not os.path.exists(os.path.join(base, src.lstrip('/'))):
                    broken_assets.append(('script', src, os.path.relpath(p, base)))

            # Find all link href (css)
            for href in re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', c):
                if href.startswith('http') or href.startswith('data:'):
                    continue
                scanned_assets.add(href)
                if not os.path.exists(os.path.join(base, href.lstrip('/'))):
                    broken_assets.append(('link', href, os.path.relpath(p, base)))

print("Scanned local script and css assets:")
for a in sorted(scanned_assets):
    print(f"  {a}")

if broken_assets:
    print(f"\nBroken assets ({len(broken_assets)}):")
    for typ, src, page in broken_assets:
        print(f"  {typ} {src} in {page}")
else:
    print("\nSUCCESS: All local scripts and stylesheets exist and resolve perfectly!")
