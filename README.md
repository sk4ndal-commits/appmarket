# AppMarket — Tailwind UI System

This workspace adds a minimal Tailwind CSS system for Django templates per `guidelines.md`.

Quick start (requires Node.js/npm):

1. Install dev deps

```bash
npm install
```

2. Build Tailwind CSS

```bash
npm run build:css
```

3. Run Django dev server

```bash
python manage.py migrate
python manage.py runserver
```

Files added:
- `tailwind.config.js`, `postcss.config.js`, `package.json`
- `styles/src/styles.css` -> compiled to `appmarket/static/css/tailwind.css`
- Templates: `templates/base.html`, `templates/partials/*`, `templates/login.html`, `templates/customer/dashboard.html`, `templates/project/create.html`

Notes:
- Tailwind-only UI; small helper CSS is in `styles/src/styles.css`.
- Add production Purge/optimization in `tailwind.config.js` for production builds.
# appmarket
