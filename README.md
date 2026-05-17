# Django + WhiteNoise

Serve compressed, hashed static files directly from your Django app —
no nginx, no S3, no extra service.

## What this branch adds

Exactly three changes vs vanilla `startproject core`:

```bash
git diff main
```

1. **Dependency** in `pyproject.toml`:
```
   "whitenoise>=6.9.0"
```
2. **Middleware** in `core/settings.py` (placed right after `SecurityMiddleware`):
```python
   MIDDLEWARE = [
       "django.middleware.security.SecurityMiddleware",
       "whitenoise.middleware.WhiteNoiseMiddleware",  # ← added
       ...
   ]
```
3. **Storage backend** for `collectstatic`:
```python
   STORAGES = {
       "staticfiles": {
           "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
       },
   }
```

## When to use this

✅ Single-server deployments (Railway, Render, Fly.io, Heroku, single VPS)  
✅ You want one fewer moving part than nginx + collectstatic  
✅ You're fine with Python serving static bytes (it's fast enough for most apps)

## When NOT to use this

❌ High-traffic sites where CDN + S3 is cheaper than app server bandwidth  
❌ You're already running nginx and don't mind one more `location` block

## Gotchas

- `CompressedManifestStaticFilesStorage` requires `collectstatic` to run before
  the server starts — your deploy step must include it.
- In `DEBUG=True`, Django's runserver bypasses WhiteNoise unless you add
  `whitenoise.runserver_nostatic` to `INSTALLED_APPS` (above `django.contrib.staticfiles`).
- Hashed filenames mean cache-busting is automatic, but also that any reference
  to `/static/foo.css` in templates must go through `{% static %}`.

## Try it

```bash
python manage.py collectstatic --noinput
python manage.py runserver
```

Static files now served with gzip + brotli + immutable cache headers.

## Further reading

- [WhiteNoise docs](https://whitenoise.readthedocs.io/)
- [Django staticfiles](https://docs.djangoproject.com/en/stable/howto/static-files/)
