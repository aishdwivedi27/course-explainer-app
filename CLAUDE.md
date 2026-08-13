# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A small Flask app (`src/app.py`) that lists courses and shows a detail page per course. Windows dev environment with a `venv` already present at the repo root.

## Commands

Activate the venv first (Windows):
```
venv\Scripts\activate
```

Install dependencies:
```
uv pip install -r requirements.txt
```

Run the app (serves at http://127.0.0.1:5000):
```
python src/app.py
```

Run all tests:
```
python -m unittest discover -s tests
```

Run a single test:
```
python -m unittest test_app.AppTestCase.test_index
```
(run from the `tests` directory, or use `-s tests` discovery syntax as above and filter with `-k`)

## Architecture

- `src/app.py` — Flask entry point. Routes are registered manually via `app.add_url_rule` rather than `@app.route` decorators, pointing at view functions imported from `src/views.py`. `/course/<int:course_id>` uses the `int` URL converter, so non-numeric ids 404 automatically.
- `src/views.py` — view functions (`index`, `course`). `course(course_id)` looks up a `Course` from `models.courses` by 1-based id (`course_id - 1` as the list index) and calls `abort(404)` if out of range.
- `src/models.py` — defines the `Course` class (`title`, `description`, `instructor`, `duration`, `topics`) and a hardcoded in-memory `courses` list, indexed 0-based but addressed via 1-based ids from the URL.
- `src/templates/` — `layout.html` is the base template (head/header/nav/footer, with a `{% block content %}`); `index.html` and `course.html` both use `{% extends 'layout.html' %}` and only fill `content`/`title` blocks. Keep new templates consistent with this `extends` pattern rather than `{% include %}`-ing the whole layout.
- Tests (`tests/test_app.py`) manipulate `sys.path` to import `app` directly from `src/` (no package/`__init__.py` structure), then use Flask's `test_client()`.
