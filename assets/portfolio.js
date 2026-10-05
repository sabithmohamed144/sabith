// Mohamed Sabith Portfolio - Interactive Enhancements
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
