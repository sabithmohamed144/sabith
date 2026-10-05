import os
import re

base = r"c:\Users\acer\Documents\Custom Office Templates\mohamedsabith.portfolio.com"

def sanitize(content):
    # 1. Remove modulepreloads
    content = re.sub(r'<link\s+rel=["\']modulepreload["\'][^>]*>', '', content)
    # 2. Remove tsr stream scripts
    content = re.sub(r'<script\s+data-tsr-stream-part=["\']["\']>.*?</script>', '', content, flags=re.DOTALL)
    # 3. Remove index-Dp5s20_x.js script
    content = re.sub(r'<script\s+type=["\']module["\'][^>]*src=["\']/assets/index-Dp5s20_x\.js["\'][^>]*></script>', '', content)
    # 4. Remove tsr-stream-boundary script
    content = re.sub(r'<script>document\.currentScript\.remove\(\);/\*\$tsr-stream-boundary\*/</script>', '', content)
    # 5. Remove tsr-scroll-restoration script
    content = re.sub(r'<script>\(function\(a,f\)\{let l;try\{l=JSON\.parse\(sessionStorage\.getItem\(a\).*?</script>', '', content, flags=re.DOTALL)
    # 6. Ensure portfolio.js has cache buster ?v=3
    content = re.sub(r'/assets/portfolio\.js(?:\?v=\d+)?', '/assets/portfolio.js?v=3', content)
    # 7. Ensure CSS has cache buster ?v=3
    content = re.sub(r'/assets/index-CVcOTz3_\.css(?:\?v=\d+)?', '/assets/index-CVcOTz3_.css?v=3', content)
    return content

count = 0
for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fp:
                c = fp.read()
            cleaned = sanitize(c)
            with open(p, 'w', encoding='utf-8') as fp:
                fp.write(cleaned)
            count += 1

print(f"Sanitized {count} HTML files successfully.")
