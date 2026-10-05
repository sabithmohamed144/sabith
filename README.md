# Mohamed Sabith — AI & Data Science Portfolio
> **Domain:** `mohamedsabith.portfolio.com`  
> **Author:** Mohamed Sabith  
> **Location:** Chennai, India  
> **Focus:** Machine Learning · Data Analytics · Explainable AI (XAI)

---

## 🌟 Overview

This is the standalone, production-ready portfolio website for **Mohamed Sabith**, designed with an editorial aesthetic, typography, and interactive components showcasing machine learning systems, research case studies, and field notes.

### Features Included:
- **01 Work / Projects:**
  - *Explainable AI for ECG-Based Stress Prediction in Autism Care* (Hybrid CNN-LSTM + SHAP, LIME, Grad-CAM on WESAD dataset, 94.3% accuracy, 0.942 macro F1-score)
  - *House Price Prediction — Regression Analysis* (Linear Regression vs Random Forest benchmark, 85–90% accuracy, feature importance breakdown)
- **02 Gallery / Field Notes:**
  - 8 photographic plates across 4 series (*Signals*, *Vision*, *Patterns*, *Chennai*)
  - Interactive series filtering (*All*, *Signals*, *Vision*, *Patterns*, *Chennai*)
  - Full-screen lightbox modal preview with metadata and series tags
- **03 About:**
  - Career journey & background in Artificial Intelligence & Data Science
  - SHAP Waterfall visualization (*Fig. A — Local explanation*)
  - Internship history (Barola Technologies, Cognifyz Technologies, Image Analysis)
  - Core competencies (ML, XAI, Python, Pandas, NumPy, SQL, Power BI, Scikit-learn)
  - Education (B.Tech AI & Data Science, Dhanalakshmi Srinivasan University, 2026)
  - Certifications (GUVI, Cognifyz, Barola)
- **04 Contact:**
  - Live Indian Standard Time (IST) clock for Chennai, India
  - One-click copy email address button (`sabithmohamed144@gmail.com`) with instant feedback
  - Direct connection channels (LinkedIn, Email, Phone: `+91 93619 51968`, GitHub)
  - Functional message form container styled with the signature ECG grid theme
- **Header & Footer:**
  - Mobile responsive drawer menu
  - Dynamic ECG pulse divider SVG animation
  - Quick contact links and copyright footer

---

## 📁 Directory Structure

```text
mohamedsabith.portfolio.com/
├── index.html                           # Home Page
├── projects/
│   ├── index.html                       # Selected Work Overview
│   ├── ecg-stress-xai/
│   │   └── index.html                   # Case study: ECG Stress Prediction
│   └── house-price-regression/
│       └── index.html                   # Case study: House Price Prediction
├── gallery/
│   └── index.html                       # Field Notes & Photographic Plates
├── about/
│   └── index.html                       # Biography, Experience, Skills & SHAP chart
├── contact/
│   └── index.html                       # Contact Page with Live IST & Copy feature
├── assets/
│   ├── index-CVcOTz3_.css               # Full stylesheet (Tailwind + Typography)
│   ├── portfolio.js                     # Mobile nav, filters, modal, clock, copy
│   └── *.js                             # JavaScript bundle chunks
├── img/                                 # All project covers and gallery plates
│   ├── cover-ecg.jpg
│   ├── cover-housing.jpg
│   ├── ecg-thermal.jpg
│   ├── edge-rickshaw.jpg
│   ├── kolam.jpg
│   ├── marina-dawn.jpg
│   ├── saliency-leaf.jpg
│   ├── signal-light.jpg
│   ├── notebook-desk.jpg
│   └── gopuram-grid.jpg
├── favicon.svg                          # Custom ECG pulse vector favicon
├── serve.py                             # Local development web server
├── start_server.bat                     # Windows one-click local server launcher
└── README.md                            # Documentation
```

---

## 🚀 Running Locally

### Option 1: Double-Click (Windows)
Double-click `start_server.bat` in this folder. It will launch the local web server and open your portfolio at `http://localhost:3000`.

### Option 2: Command Line (Python)
Open a terminal in `mohamedsabith.portfolio.com` and run:
```bash
python serve.py
```
Then visit: [http://localhost:3000](http://localhost:3000)

---

## 🌐 Deploying & Setting Up Custom Domain (`mohamedsabith.portfolio.com`)

### Deploying to Netlify:
1. Log in to [Netlify](https://www.netlify.com/).
2. Drag and drop the `mohamedsabith.portfolio.com` folder onto your Netlify dashboard under **Sites** > **Deploy manually**.
3. Go to **Site Configuration** > **Domain management** > **Custom domains**.
4. Click **Add a domain** and enter `mohamedsabith.portfolio.com` (or your registered domain).
5. Add the CNAME / DNS records indicated by Netlify in your domain provider’s DNS settings (e.g. GoDaddy, Namecheap, Cloudflare).

### Deploying to Vercel:
1. Install Vercel CLI (`npm i -g vercel`) or import via GitHub.
2. Run `vercel deploy --prod` from this folder.
3. In the Vercel project settings, navigate to **Domains** and attach `mohamedsabith.portfolio.com`.

### Deploying to GitHub Pages:
1. Initialize a git repository and push this directory to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit of Mohamed Sabith portfolio"
   git branch -M main
   git remote add origin https://github.com/<your-username>/mohamedsabith.portfolio.com.git
   git push -u origin main
   ```
2. In the repository settings, go to **Pages**, select **Deploy from a branch** (`main` / root), and set custom domain to `mohamedsabith.portfolio.com`.
