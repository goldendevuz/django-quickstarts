# Django Quickstarts

A cookbook of focused, single-purpose Django integrations.

Each branch in this repo is the same vanilla `django-admin startproject core` —
with **one package added** and **only the lines that package actually requires** changed.

Open any branch, run `git diff main`, and you see exactly what to add to your own project. No boilerplate noise, no "kitchen sink" config, no decisions made for you.

## Why this exists

Most Django tutorials either:
- Bury the integration in a blog post that's stale 6 months later, or  
- Ship a giant starter template where you can't tell which lines belong to which package.

This repo solves both: **one branch per package, one minimal diff per branch.**

## Recipes

### Static files & assets
| Branch | Package | What it solves |
|---|---|---|
| [`whitenoise`](../../tree/whitenoise) | whitenoise | Serve static files in production without nginx |
| [`storages-s3`](../../tree/storages-s3) | django-storages | Offload media to S3 / R2 / GCS |

### Authentication
| Branch | Package | What it solves |
|---|---|---|
| [`allauth`](../../tree/allauth) | django-allauth | Social login (Google, GitHub, etc.) |
| [`simplejwt`](../../tree/simplejwt) | djangorestframework-simplejwt | JWT auth for DRF |

### API & DRF
| Branch | Package | What it solves |
|---|---|---|
| [`drf-spectacular`](../../tree/drf-spectacular) | drf-spectacular | OpenAPI 3 schema + Swagger UI |
| ... | ... | ... |

### Background tasks
| ... | ... | ... |

### Performance & caching
| ... | ... | ... |

### Dev tooling
| ... | ... | ... |

## How to use a recipe

```bash
git clone -b whitenoise https://github.com/goldendevuz/django-quickstarts.git
cd django-quickstarts
uv sync   # or pip install -r requirements.txt
python manage.py runserver
```

To see **exactly what changed** vs vanilla Django:

```bash
git diff main..whitenoise
```

## Philosophy

- One branch = one package = one concern
- Smallest possible diff against vanilla `startproject`
- Every recipe runs out of the box
- README in every branch explains the *why*, not just the *how*

## Contributing

Found a missing package or a better way? Open an issue or PR.
