# Reviews

A Django-based reviews and company-directory website.

## Requirements

- Python 3.12+
- pip
- Docker Desktop / Docker Engine (optional, easiest local setup)

The project uses Django 6.1, WhiteNoise for static assets, Gunicorn for WSGI serving, and SQLite by default. The old collection of unused and pinned legacy packages has been removed from the runtime requirements.

## Run locally with Docker

Start the app:

```bash
docker compose up --build
```

Open http://127.0.0.1:8000/

The Compose configuration uses a development-only secret and enables DEBUG for local use. Do not reuse those defaults in production.

## Run locally without Docker

Create and activate a virtual environment, then install dependencies:

```bash
python3.12 -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Set development environment variables before running Django:

```bash
export DJANGO_SECRET_KEY='replace-with-a-long-random-local-secret'
export DJANGO_DEBUG=True
export DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
python manage.py migrate
python manage.py runserver
```

On Windows PowerShell, use `$env:NAME="value"` instead of `export NAME=value`.

## Tests and checks

```bash
python manage.py check
python manage.py test
python manage.py collectstatic --noinput
```

## Production configuration

Set these in the hosting provider's environment/secret manager:

- `DJANGO_SECRET_KEY`: a newly generated, private secret; never commit it.
- `DJANGO_DEBUG=False`
- `DJANGO_ALLOWED_HOSTS`: comma-separated hostnames, without schemes.
- `DJANGO_CSRF_TRUSTED_ORIGINS`: comma-separated HTTPS origins, including schemes.
- Configure HTTPS at the platform/proxy before enabling `DJANGO_SECURE_SSL_REDIRECT=True` and HSTS.

Use a persistent database for production. SQLite is configured as the zero-setup local default; it is not recommended for multi-worker production deployments.

## Notes

- The login, registration, and review templates are currently presentation pages; the repository does not yet implement account creation, authentication flows, or persisted review submission.
- The historical SQLite database and old Git commits are not rewritten by this upgrade. Review database contents before sharing or deploying the repository.
