# guidelines.md (Django Monolith + Django Templates + Tailwind)

## 1) Product Overview

### What this app is
A two-sided B2B marketplace that connects:
- Customers who need custom software
- Providers (software companies/teams) who can deliver it

Core value:
- Structured intake (comparable requirements)
- High-signal matching (shortlist, not a directory)
- Controlled intros + contextual messaging
- Trust/safety + auditability

### What this app is not
- Not a bidding/auction marketplace
- Not a public directory-first product
- Not procurement (contracts, payments, escrow) in MVP
- Not realtime-first chat
- Not industry-specific

---

## 2) Mandated Stack

- Python + **Django**
- Server-rendered pages via **Django templates**
- **Tailwind CSS** for UI
- PostgreSQL
- Background jobs: **Celery + Redis** (recommended) or Django-Q/RQ
- Email provider (Resend/Postmark/SendGrid)
- Storage: local dev; S3-compatible for production

---

## 3) Architecture: Modular Monolith (Django)

Single deployable Django app, but organized into apps (“modules”) with strict boundaries.

### Core Django apps
- accounts (auth, roles)
- projects (customer intake + lifecycle + attachments)
- providers (provider profile + preferences)
- matching (scoring, candidates, overrides)
- intros (intro requests)
- messaging (conversations, messages)
- moderation (reports, suspensions)
- notifications (preferences, email sending)
- adminops (queues, metrics)
- audit (audit log, event log)

### Non-negotiable rules
- Templates must not contain business logic (only presentation).
- Views call **service functions**; avoid heavy logic in views.
- Permissions enforced server-side on every action.
- Background work runs in Celery tasks (no long work in request/response).
- Status transitions centralized and validated.

---

## 5) UI Guidelines (Django Templates + Tailwind)

### Principles
- Minimal, utilitarian, fast
- Tailwind utility classes only
- Reuse partials; no ad-hoc UI patterns

### Required partials (source of truth)
- `partials/_nav.html`
- `partials/_page_header.html`
- `partials/_button.html`
- `partials/_badge.html` (status badges)
- `partials/_alert.html`
- `partials/_form_field.html`
- `partials/_empty_state.html`

### Layout conventions
- Container: `max-w-6xl mx-auto px-4 py-6`
- Cards: `bg-white border border-slate-200 rounded-lg p-6`
- Tables: simple, readable, responsive (wrap, not horizontal scroll unless needed)
- Status uses consistent badges (no custom colors beyond defined palette)

### Color scheme (simple)
- Background: slate-50
- Surfaces: white
- Text: slate-900 / slate-700 / slate-500
- Primary: indigo-600 (buttons, active nav)
- Success: emerald-600
- Warning: amber-500
- Danger: rose-600

---

## 6) Auth & Roles

- Use Django auth (sessions)
- Role stored on `UserProfile.role` (Customer/Provider/Admin)
- Decorators/mixins for role checks (e.g., `@customer_required`)
- Ownership checks for:
  - project access
  - intro requests
  - conversations/messages
  - attachments

---

## 7) Data & Migrations

- Postgres is system of record
- All schema changes via migrations
- Index common filters: status, created_at, foreign keys
- Avoid N+1 queries (select_related/prefetch_related)
- Audit log for state changes and admin overrides

---

## 8) Background Jobs (Celery)

Use tasks for:
- candidate recompute (publish, provider profile change)
- email notifications
- cleanup

Rules:
- Tasks must be idempotent
- Retries configured
- Log entity ids + correlation/request id when available

---

## 9) Matching (MVP)

- Rule-based scoring with explainable reasons
- Hard excludes for non-fit
- Admin overrides: pin/remove/add
- Customer sees 3–5 recommended

---

## 10) Testing & Merge Gates (Vibecoding Safety)

Minimum gate before merge:
- `python -m ruff check .` (or flake8)
- `python -m mypy .` (or pyright) for typed modules
- migrations are created and applied in CI

---

## 12) Definition of Done

Done means:
- acceptance criteria met
- permissions verified
- UI consistent with Tailwind partial system
