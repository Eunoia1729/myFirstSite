# myFirstSite

Django learning/test project. <br>
The blogSite wouldn't be making any sense as I made this just to understand and absorb the framework.

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
DJANGO_DEBUG=1 python manage.py runserver
```

## Configuration

| Variable | Purpose |
| --- | --- |
| `DJANGO_SECRET_KEY` | Secret key. Required for any deployment; a placeholder is used otherwise. |
| `DJANGO_DEBUG` | Set to `1` to enable debug mode. Off by default. |

The SQLite database (`db.sqlite3`) is not committed; `migrate` creates it.
