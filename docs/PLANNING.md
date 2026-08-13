# Melokaktos


## Project Overview

A desktop application that allow users to record their climbs, either sport or boulder. Climbers will be able to add, edit and delete the routes they complete.


## Problem Statement

As a climber, I need a way to save the climbs I complete, creating a history of my progress in the sport for future reference.


## Core Features (MVP)
1. Log, edit and delete climbs, with route names, grade, discipline, send type (onsight, flash, redpoint, attempt), date and location.
2. Simple and minimalist design.


## Nice-to-Have Features
1. User can upload images of each climb.
2. User can filter/search climb logs (by date, grade, location, type, etc.)
3. User can view aggregate stats (e.g. climbs per grade, progress over time)


## Stretch Goals
1. Mobile version of the application.


## Technical Stack
- **Front-end:** PySide6 (GUI)
- **Back-end:** Python
- **Database:** SQLAlchemy - SQLite
- **Deployment:** PyInstaller


## Project Structure
- **UI Layer** (PySide6) — windows, widgets, forms; handles user input and display only
- **Business Logic / Services** — CRUD operations, validation, application rules; decoupled from UI
- **Data Layer** (SQLAlchemy models) — table definitions, relationships
- **Persistence** (SQLite) — the actual database file, local to the user's machine
- **Migrations** (Alembic) — schema versioning as the data model evolves
- **Packaging** (PyInstaller, via uv) — bundling into a distributable executable


## Success Criteria
- [ ] User is able to install the application on their OS without needing Python installed separately.
- [ ] User is able to add, view, edit, and delete climb logs.
- [ ] Data persists across application restarts.
- [ ] Application does not crash on basic invalid input (e.g. empty required field).

## Out of Scope
User authentication. Application is local-only by design; no network sync or multi-device access for MVP.