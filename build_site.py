import os
import re
import shutil

BASE_DIR = r"c:\Users\acer\Documents\Custom Office Templates\mohamedsabith.portfolio.com"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
IMG_DIR = os.path.join(BASE_DIR, "img")

# 1. Create favicon.svg
favicon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <rect width="32" height="32" fill="#15130f"/>
  <path d="M3 18h7l2-3 3 9 3-17 3 11h8" fill="none" stroke="#e8411b" stroke-width="2.2" stroke-linejoin="round"/>
</svg>'''
with open(os.path.join(BASE_DIR, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(favicon_svg)
print("Created favicon.svg")

# 2. Patch OptimizedImage-DBAtxuaH.js to return clean local image paths
opt_img_path = os.path.join(ASSETS_DIR, "OptimizedImage-DBAtxuaH.js")
if os.path.exists(opt_img_path):
    with open(opt_img_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Replace o function and l function
    patched = re.sub(
        r'function o\(n,\{[^}]*\}\=\{[^}]*\}\{[^}]*\}',
        'function o(n){return n}',
        content
    )
    patched = re.sub(
        r'function l\(n,a,r\)\{[^}]*\}',
        'function l(n){return n}',
        patched
    )
    with open(opt_img_path, "w", encoding="utf-8") as f:
        f.write(patched)
    print("Patched OptimizedImage-DBAtxuaH.js")

# 3. Create assets/portfolio.js
portfolio_js = '''// Mohamed Sabith Portfolio - Interactive Enhancements
document.addEventListener('DOMContentLoaded', () => {
  // Mobile Nav Toggle
  const header = document.querySelector('header');
  const menuBtn = document.querySelector('button[aria-controls="mobile-nav"]');
  if (menuBtn && header) {
    let nav = document.getElementById('mobile-nav');
    if (!nav) {
      nav = document.createElement('nav');
      nav.id = 'mobile-nav';
      nav.className = 'border-t border-rule px-5 pb-6 md:hidden';
      nav.setAttribute('aria-label', 'Mobile');
      nav.style.display = 'none';
      nav.innerHTML = `
        <a class="flex items-baseline gap-3 border-b border-rule py-4 font-display text-4xl" href="/projects"><span class="font-mono text-xs text-graphite">01</span>Work</a>
        <a class="flex items-baseline gap-3 border-b border-rule py-4 font-display text-4xl" href="/gallery"><span class="font-mono text-xs text-graphite">02</span>Gallery</a>
        <a class="flex items-baseline gap-3 border-b border-rule py-4 font-display text-4xl" href="/about"><span class="font-mono text-xs text-graphite">03</span>About</a>
        <a class="flex items-baseline gap-3 border-b border-rule py-4 font-display text-4xl" href="/contact"><span class="font-mono text-xs text-graphite">04</span>Contact</a>
      `;
      header.appendChild(nav);
    }
    menuBtn.addEventListener('click', () => {
      const isOpen = menuBtn.getAttribute('aria-expanded') === 'true';
      menuBtn.setAttribute('aria-expanded', !isOpen);
      menuBtn.textContent = isOpen ? 'Menu' : 'Close';
      nav.style.display = isOpen ? 'none' : 'block';
    });
  }

  // Live IST Clock (Chennai, India)
  const clockEl = document.getElementById('ist-clock');
  if (clockEl) {
    function updateClock() {
      try {
        const now = new Date();
        const timeStr = new Intl.DateTimeFormat('en-GB', {
          timeZone: 'Asia/Kolkata',
          hour: '2-digit',
          minute: '2-digit',
          hour12: false
        }).format(now);
        clockEl.textContent = timeStr;
      } catch (e) {
        const utc = new Date();
        const ist = new Date(utc.getTime() + (5.5 * 60 * 60 * 1000));
        const h = String(ist.getUTCHours()).padStart(2, '0');
        const m = String(ist.getUTCMinutes()).padStart(2, '0');
        clockEl.textContent = `${h}:${m}`;
      }
    }
    updateClock();
    setInterval(updateClock, 1000);
  }

  // Copy Email Address Button
  const copyBtn = document.getElementById('copy-email-btn');
  if (copyBtn) {
    copyBtn.addEventListener('click', async () => {
      const email = 'sabithmohamed144@gmail.com';
      try {
        await navigator.clipboard.writeText(email);
        const textSpan = document.getElementById('copy-text');
        const iconEl = document.getElementById('copy-icon');
        if (textSpan) textSpan.textContent = 'Copied';
        if (iconEl) {
          iconEl.innerHTML = '<path d="M20 6 9 17l-5-5"></path>';
        }
        setTimeout(() => {
          if (textSpan) textSpan.textContent = 'Copy address';
          if (iconEl) {
            iconEl.innerHTML = '<rect width="14" height="14" x="8" y="8" rx="2" ry="2"></rect><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path>';
          }
        }, 2000);
      } catch (err) {
        window.location.href = 'mailto:' + email;
      }
    });
  }

  // Contact Form Submission Handler
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const submitBtn = contactForm.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = 'Transmitting…';
      }
      setTimeout(() => {
        const formBox = document.getElementById('contact-form-box');
        if (formBox) {
          formBox.innerHTML = `
            <div class="flex items-center justify-between border-b border-ink bg-paper px-5 py-3">
              <span class="label !text-ink">Message form</span>
              <span class="label">Status: Sent</span>
            </div>
            <div class="bg-paper/80 px-6 py-16 text-center">
              <svg viewBox="0 0 1680 80" preserveAspectRatio="none" aria-hidden="true" class="mx-auto h-12 max-w-xs text-signal">
                <path d="M0,50 L46,50 L49,56 L54,8 L59,70 L63,50 L100,50" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"></path>
              </svg>
              <p class="mt-6 font-display text-5xl">Signal received.</p>
              <p class="mt-3 text-ink-soft">Thanks — I’ll get back to you soon.</p>
              <button type="button" onclick="location.reload()" class="link-underline mt-8 text-sm font-medium">Send another message</button>
            </div>
          `;
        }
      }, 700);
    });
  }

  // Gallery Filters
  const filterBtns = document.querySelectorAll('[data-gallery-filter]');
  const galleryItems = document.querySelectorAll('[data-series]');
  if (filterBtns.length && galleryItems.length) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const target = btn.getAttribute('data-gallery-filter');
        filterBtns.forEach(b => {
          b.className = 'px-3 py-1.5 font-mono text-xs uppercase tracking-[0.1em] transition-colors text-graphite hover:text-ink';
          b.setAttribute('aria-pressed', 'false');
        });
        btn.className = 'px-3 py-1.5 font-mono text-xs uppercase tracking-[0.1em] transition-colors bg-ink text-paper';
        btn.setAttribute('aria-pressed', 'true');

        galleryItems.forEach(item => {
          if (target === 'All' || item.getAttribute('data-series') === target) {
            item.style.display = '';
          } else {
            item.style.display = 'none';
          }
        });
      });
    });
  }

  // Gallery Lightbox Modal
  const modal = document.getElementById('gallery-modal');
  if (modal) {
    const modalImg = document.getElementById('modal-img');
    const modalTitle = document.getElementById('modal-title');
    const modalSeries = document.getElementById('modal-series');
    const modalNote = document.getElementById('modal-note');
    const modalClose = document.getElementById('modal-close');

    document.querySelectorAll('[data-modal-open]').forEach(btn => {
      btn.addEventListener('click', () => {
        const src = btn.getAttribute('data-img-src');
        const title = btn.getAttribute('data-img-title');
        const series = btn.getAttribute('data-img-series');
        const note = btn.getAttribute('data-img-note');
        if (modalImg) modalImg.src = src;
        if (modalTitle) modalTitle.textContent = title;
        if (modalSeries) modalSeries.textContent = series;
        if (modalNote) modalNote.textContent = note;
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        document.body.style.overflow = 'hidden';
      });
    });

    function closeModal() {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
      document.body.style.overflow = '';
    }

    if (modalClose) modalClose.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeModal();
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
        closeModal();
      }
    });
  }
});
'''
with open(os.path.join(ASSETS_DIR, "portfolio.js"), "w", encoding="utf-8") as f:
    f.write(portfolio_js)
print("Created assets/portfolio.js")

# Function to clean and sanitize HTML
def clean_html(html, current_page=""):
    # 1. Clean image sources
    # Replace netlify dynamic image url with direct /img/...
    html = re.sub(
        r'/\.netlify/images\?url=(?:%2F|/)img(?:%2F|/)([^&"\'\s]+)[^"\'\s]*',
        r'/img/\1',
        html
    )
    # Also clean in srcset
    def fix_srcset(match):
        val = match.group(1)
        fixed = re.sub(r'/\.netlify/images\?url=(?:%2F|/)img(?:%2F|/)([^&"\'\s]+)[^,\s]*', r'/img/\1', val)
        return f'srcSet="{fixed}"'
    html = re.sub(r'srcSet="([^"]*)"', fix_srcset, html)
    html = re.sub(r'srcset="([^"]*)"', fix_srcset, html)

    # 2. Remove Netlify preview / hud scripts
    html = re.sub(r'<script async src="/\.netlify/scripts/[^"]*"[^>]*></script>', '', html)

    # 3. Remove Netlify comment headers
    html = re.sub(r'<!--\s*This site is hosted on Netlify.*?-->', '', html, flags=re.DOTALL)

    # 4. Ensure favicon link
    if 'favicon.svg' not in html:
        html = re.sub(r'(<head[^>]*>)', r'\1<link rel="icon" type="image/svg+xml" href="/favicon.svg"/>', html)

    # 5. Inject assets/portfolio.js before </body>
    if 'portfolio.js' not in html:
        html = html.replace('</body>', '<script src="/assets/portfolio.js" defer></script></body>')

    return html

# 4. Build contact.html
def generate_contact_html():
    with open(os.path.join(BASE_DIR, "about.html"), "r", encoding="utf-8") as f:
        about_html = f.read()
    
    # We take head from about_html
    head_match = re.search(r'(<head.*?</head>)', about_html, re.DOTALL)
    head = head_match.group(1) if head_match else ""
    head = head.replace("<title>About - Mohamed Sabith</title>", "<title>Contact - Mohamed Sabith</title>")
    head = clean_html(head, "contact")

    # Header with Contact highlighted
    header = '''<header class="sticky top-0 z-40 border-b border-rule bg-paper/85 backdrop-blur-md">
  <div class="mx-auto flex h-16 max-w-[1400px] items-center justify-between px-5 md:px-10">
    <a class="group flex items-center gap-3" href="/">
      <span class="font-display text-2xl leading-none tracking-tight">Mohamed<span class="italic text-signal"> Sabith</span></span>
      <span class="hidden items-center gap-2 border-l border-rule pl-3 sm:flex">
        <span class="h-1.5 w-1.5 rounded-full bg-signal animate-pulse-dot"></span>
        <span class="label">Open to roles · 2026</span>
      </span>
    </a>
    <nav class="hidden items-center gap-8 md:flex" aria-label="Main">
      <a class="group flex items-baseline gap-1.5 text-sm" href="/projects">
        <span class="font-mono text-[10px] text-graphite group-hover:text-signal">01</span>
        <span class="link-underline">Work</span>
      </a>
      <a class="group flex items-baseline gap-1.5 text-sm" href="/gallery">
        <span class="font-mono text-[10px] text-graphite group-hover:text-signal">02</span>
        <span class="link-underline">Gallery</span>
      </a>
      <a class="group flex items-baseline gap-1.5 text-sm" href="/about">
        <span class="font-mono text-[10px] text-graphite group-hover:text-signal">03</span>
        <span class="link-underline">About</span>
      </a>
      <a class="group flex items-baseline gap-1.5 text-sm text-signal" href="/contact" data-status="active" aria-current="page">
        <span class="font-mono text-[10px] text-graphite group-hover:text-signal">04</span>
        <span class="link-underline">Contact</span>
      </a>
    </nav>
    <button type="button" class="label md:hidden" aria-expanded="false" aria-controls="mobile-nav">Menu</button>
  </div>
</header>'''

    # Contact main section
    main = '''<main id="main">
  <section class="mx-auto max-w-[1400px] px-5 pt-16 md:px-10 md:pt-24">
    <div class="flex flex-wrap items-baseline justify-between gap-4">
      <p class="label">Contact · Chennai, India</p>
      <p class="label" aria-live="polite">
        <span class="mr-2 inline-block h-1.5 w-1.5 rounded-full bg-signal align-middle animate-pulse-dot"></span>
        Local time <span id="ist-clock">11:45</span> IST
      </p>
    </div>
    <h1 class="mt-4 font-display text-[clamp(3.5rem,10vw,10rem)] leading-[0.86] tracking-tight">
      Say <em class="text-signal">hello.</em>
    </h1>
    <p class="mt-6 max-w-xl text-xl leading-relaxed text-ink-soft">
      Hiring for a data science or ML role, have an AI project in mind, or just want to argue about SHAP values? I reply to every message.
    </p>
    <div class="mt-14 flex flex-col gap-4 border-y border-ink py-8 md:flex-row md:items-center md:justify-between">
      <a href="mailto:sabithmohamed144@gmail.com" class="group break-all font-display text-3xl leading-tight sm:text-5xl lg:text-6xl">
        <span class="link-underline group-hover:text-signal">sabithmohamed144@gmail.com</span>
      </a>
      <button type="button" id="copy-email-btn" class="inline-flex shrink-0 items-center gap-2 self-start border border-ink px-4 py-2.5 font-mono text-xs uppercase tracking-[0.1em] transition-colors hover:bg-ink hover:text-paper md:self-auto">
        <svg id="copy-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-copy">
          <rect width="14" height="14" x="8" y="8" rx="2" ry="2"></rect>
          <path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path>
        </svg>
        <span id="copy-text">Copy address</span>
      </button>
    </div>
    <div class="mt-20 grid gap-16 lg:grid-cols-12">
      <div class="lg:col-span-5">
        <p class="label !text-ink">Elsewhere</p>
        <ul class="mt-4">
          <li>
            <a href="https://linkedin.com/in/mohamed-sabith-421233368" target="_blank" rel="noreferrer" class="group grid grid-cols-[2.5rem_1fr_auto] items-center gap-2 border-b border-rule py-5 hover:border-ink">
              <span class="font-mono text-[11px] text-graphite">01</span>
              <span>
                <span class="block font-display text-4xl leading-tight">LinkedIn</span>
                <span class="block truncate text-sm text-graphite">in/mohamed-sabith-421233368</span>
              </span>
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="transition-transform group-hover:-translate-y-1 group-hover:translate-x-1 group-hover:text-signal">
                <path d="M7 7h10v10"></path>
                <path d="M7 17 17 7"></path>
              </svg>
            </a>
          </li>
          <li>
            <a href="mailto:sabithmohamed144@gmail.com" class="group grid grid-cols-[2.5rem_1fr_auto] items-center gap-2 border-b border-rule py-5 hover:border-ink">
              <span class="font-mono text-[11px] text-graphite">02</span>
              <span>
                <span class="block font-display text-4xl leading-tight">Email</span>
                <span class="block truncate text-sm text-graphite">sabithmohamed144@gmail.com</span>
              </span>
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="transition-transform group-hover:-translate-y-1 group-hover:translate-x-1 group-hover:text-signal">
                <path d="M7 7h10v10"></path>
                <path d="M7 17 17 7"></path>
              </svg>
            </a>
          </li>
          <li>
            <a href="tel:+919361951968" class="group grid grid-cols-[2.5rem_1fr_auto] items-center gap-2 border-b border-rule py-5 hover:border-ink">
              <span class="font-mono text-[11px] text-graphite">03</span>
              <span>
                <span class="block font-display text-4xl leading-tight">Phone</span>
                <span class="block truncate text-sm text-graphite">+91 93619 51968</span>
              </span>
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="transition-transform group-hover:-translate-y-1 group-hover:translate-x-1 group-hover:text-signal">
                <path d="M7 7h10v10"></path>
                <path d="M7 17 17 7"></path>
              </svg>
            </a>
          </li>
          <li>
            <div class="group grid grid-cols-[2.5rem_1fr_auto] items-center gap-2 border-b border-rule py-5 opacity-50">
              <span class="font-mono text-[11px] text-graphite">04</span>
              <span>
                <span class="block font-display text-4xl leading-tight">GitHub</span>
                <span class="block truncate text-sm text-graphite">Repository going public soon</span>
              </span>
              <span class="label">soon</span>
            </div>
          </li>
        </ul>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <div id="contact-form-box" class="ecg-grid border border-ink">
          <div class="flex items-center justify-between border-b border-ink bg-paper px-5 py-3">
            <span class="label !text-ink">Message form</span>
            <span class="label">Response &lt; 48h</span>
          </div>
          <form id="contact-form" name="contact" method="POST" class="space-y-6 bg-paper/80 p-6 md:p-8">
            <div class="grid gap-6 sm:grid-cols-2">
              <label class="block">
                <span class="label !text-ink">Name</span>
                <input type="text" name="name" required placeholder="Ada Lovelace" autocomplete="name" class="mt-2 w-full border-b border-ink bg-transparent py-2 text-lg outline-none placeholder:text-graphite/50 focus:border-signal"/>
              </label>
              <label class="block">
                <span class="label !text-ink">Email</span>
                <input type="email" name="email" required placeholder="you@company.com" autocomplete="email" class="mt-2 w-full border-b border-ink bg-transparent py-2 text-lg outline-none placeholder:text-graphite/50 focus:border-signal"/>
              </label>
            </div>
            <label class="block">
              <span class="label !text-ink">Subject</span>
              <input type="text" name="subject" required placeholder="Data scientist role at …" class="mt-2 w-full border-b border-ink bg-transparent py-2 text-lg outline-none placeholder:text-graphite/50 focus:border-signal"/>
            </label>
            <label class="block">
              <span class="label !text-ink">Message</span>
              <textarea name="message" required minlength="10" rows="6" placeholder="Tell me about the problem, the data, and the timeline." class="mt-2 w-full resize-none border-b border-ink bg-transparent py-2 text-lg outline-none placeholder:text-graphite/50 focus:border-signal"></textarea>
            </label>
            <div class="flex flex-wrap items-center justify-between gap-4 pt-2">
              <button type="submit" class="group inline-flex items-center gap-2 bg-ink px-6 py-3.5 text-sm font-medium text-paper transition-colors hover:bg-signal disabled:opacity-60">
                <span>Send message</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="transition-transform group-hover:-translate-y-0.5 group-hover:translate-x-0.5">
                  <path d="M7 7h10v10"></path>
                  <path d="M7 17 17 7"></path>
                </svg>
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
</main>'''

    # Extract footer from about_html
    footer_match = re.search(r'(<footer.*</footer>)', about_html, re.DOTALL)
    footer = footer_match.group(1) if footer_match else ""

    # Assemble contact HTML
    contact_page = f'''<!DOCTYPE html>
<html lang="en">
{head}
<body class="bg-paper text-ink font-sans antialiased selection:bg-signal selection:text-paper min-h-screen flex flex-col justify-between">
{header}
{main}
{footer}
<script src="/assets/portfolio.js" defer></script>
</body>
</html>'''
    return contact_page

contact_html_content = generate_contact_html()
with open(os.path.join(BASE_DIR, "contact.html"), "w", encoding="utf-8") as f:
    f.write(contact_html_content)
print("Generated complete contact.html")

# 5. Clean and process all main HTML files
files_to_clean = [
    "index.html",
    "projects.html",
    "about.html",
    "gallery.html",
    "projects_ecg-stress-xai.html",
    "projects_house-price-regression.html"
]

for fname in files_to_clean:
    p = os.path.join(BASE_DIR, fname)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            c = f.read()
        cleaned = clean_html(c, fname)
        with open(p, "w", encoding="utf-8") as f:
            f.write(cleaned)
        print(f"Cleaned {fname}")

# 6. Enhance gallery.html with filter attributes and modal markup
gallery_path = os.path.join(BASE_DIR, "gallery.html")
with open(gallery_path, "r", encoding="utf-8") as f:
    gal_content = f.read()

# Add data-gallery-filter attributes to buttons
gal_content = re.sub(
    r'<button([^>]*>All.*?)</button>',
    r'<button data-gallery-filter="All"\1</button>',
    gal_content
)
gal_content = re.sub(
    r'<button([^>]*>Signals.*?)</button>',
    r'<button data-gallery-filter="Signals"\1</button>',
    gal_content
)
gal_content = re.sub(
    r'<button([^>]*>Vision.*?)</button>',
    r'<button data-gallery-filter="Vision"\1</button>',
    gal_content
)
gal_content = re.sub(
    r'<button([^>]*>Patterns.*?)</button>',
    r'<button data-gallery-filter="Patterns"\1</button>',
    gal_content
)
gal_content = re.sub(
    r'<button([^>]*>Chennai.*?)</button>',
    r'<button data-gallery-filter="Chennai"\1</button>',
    gal_content
)

# Plates data mapping for lightbox & filter
plates_meta = {
    "ecg-thermal.jpg": ("Lead II, curled", "Signals", "Thermal ECG paper - where the stress-prediction project started."),
    "edge-rickshaw.jpg": ("Half seen", "Vision", "A street, and what a Canny edge detector keeps of it."),
    "kolam.jpg": ("Doorstep algorithm", "Patterns", "Kolam: a hand-drawn rule system, redrawn every morning."),
    "marina-dawn.jpg": ("Low signal, Marina", "Chennai", "Chennai at 5:40am. The quietest dataset I know."),
    "saliency-leaf.jpg": ("Where the model looked", "Vision", "A Grad-CAM style saliency study on a banyan leaf."),
    "signal-light.jpg": ("Waveform, long exposure", "Signals", "Light as a time series."),
    "notebook-desk.jpg": ("Before the notebook, a notebook", "Patterns", "Every model starts on graph paper, next to filter coffee."),
    "gopuram-grid.jpg": ("Repetition with variance", "Chennai", "Gopuram tiers - a lesson in features that almost repeat.")
}

for img_file, (title, series, note) in plates_meta.items():
    # Wrap list item with data-series and button with data-modal-open
    pattern = rf'(<li[^>]*><button[^>]*aria-label="Open &quot;{re.escape(title)}&quot;"[^>]*>)'
    replacement = rf'<li class="mb-10 break-inside-avoid" data-series="{series}"><button type="button" class="group block w-full text-left" data-modal-open data-img-src="/img/{img_file}" data-img-title="{title}" data-img-series="{series}" data-img-note="{note}">'
    gal_content = re.sub(pattern, replacement, gal_content)

# Add Lightbox Modal to gallery.html if not already present
if 'id="gallery-modal"' not in gal_content:
    modal_html = '''
<!-- Gallery Lightbox Modal -->
<div id="gallery-modal" class="fixed inset-0 z-50 hidden items-center justify-center bg-ink/90 backdrop-blur-md p-4 sm:p-8">
  <div class="relative max-w-5xl w-full bg-paper border border-rule overflow-hidden shadow-2xl flex flex-col max-h-[92vh]">
    <div class="flex items-center justify-between border-b border-rule px-6 py-4 bg-paper/95">
      <div class="flex items-center gap-3">
        <span id="modal-series" class="label text-signal">Series</span>
        <h3 id="modal-title" class="font-display text-2xl leading-none">Plate Title</h3>
      </div>
      <button id="modal-close" type="button" class="label p-2 hover:text-signal transition-colors" aria-label="Close modal">
        ✕ Close
      </button>
    </div>
    <div class="overflow-auto flex-1 p-6 flex flex-col items-center justify-center bg-paper-deep/30">
      <img id="modal-img" src="" alt="Enlarged plate" class="max-h-[65vh] w-auto object-contain border border-rule bg-paper shadow-sm" />
      <p id="modal-note" class="mt-4 text-center font-sans text-sm text-graphite max-w-xl"></p>
    </div>
  </div>
</div>
'''
    gal_content = gal_content.replace('</main>', modal_html + '</main>')

with open(gallery_path, "w", encoding="utf-8") as f:
    f.write(gal_content)
print("Enhanced gallery.html with interactive filters and lightbox")

# 7. Create directory routes for clean URLs
routes_map = {
    "projects": "projects.html",
    "gallery": "gallery.html",
    "about": "about.html",
    "contact": "contact.html",
    os.path.join("projects", "ecg-stress-xai"): "projects_ecg-stress-xai.html",
    os.path.join("projects", "house-price-regression"): "projects_house-price-regression.html"
}

for route_dir, src_file in routes_map.items():
    dest_dir = os.path.join(BASE_DIR, route_dir)
    os.makedirs(dest_dir, exist_ok=True)
    src_path = os.path.join(BASE_DIR, src_file)
    dest_path = os.path.join(dest_dir, "index.html")
    shutil.copy2(src_path, dest_path)
    print(f"Created route {route_dir}/index.html from {src_file}")

# 8. Create serve.py for local testing
serve_py = '''import http.server
import socketserver
import os

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS and disable cache during preview
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"================================================================")
        print(f"  Mohamed Sabith Portfolio is live at: http://localhost:{PORT}")
        print(f"  Serving files from: {DIRECTORY}")
        print(f"  Press Ctrl+C to stop the server.")
        print(f"================================================================")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\\nServer stopped.")
'''
with open(os.path.join(BASE_DIR, "serve.py"), "w", encoding="utf-8") as f:
    f.write(serve_py)
print("Created serve.py")

# 9. Create start_server.bat
start_bat = '''@echo off
title Mohamed Sabith Portfolio - Local Server
echo Starting Mohamed Sabith Portfolio server at http://localhost:3000 ...
python "%~dp0serve.py"
pause
'''
with open(os.path.join(BASE_DIR, "start_server.bat"), "w", encoding="utf-8") as f:
    f.write(start_bat)
print("Created start_server.bat")

print("Build complete! All routes, assets, and pages are ready.")
