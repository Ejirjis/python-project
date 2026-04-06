# Python Learning Path - Progress Tracker

## Status: In Progress 🔥

---

## Phase 1 — Python Fundamentals ✅

### What I learned

- Functions, parameters, return vs print
- Input validation — clean data before validating
- String methods — strip(), lower(), in operator
- Lists and loops — filter, count, append
- Dictionaries — structured data with key/value pairs
- File I/O — reading/writing files, "w" vs "a", try/except
- OOP — classes, **init**, self, methods

### What I built

- Discount calculator
- Username formatter
- Registration validator
- Grade processor
- Note saver
- Contact book (two classes working together)

---

## Phase 2 — APIs & CLI Projects ✅

### What I learned

- requests library — fetching live data from the internet
- JSON — reading nested data
- f-strings — building dynamic URLs
- CLI tools — while True loops, input(), menu interfaces
- Timestamps — datetime.now() and strftime()
- Append vs overwrite — "a" vs "w"

### What I built

- Crypto Price Checker CLI
  - Fetches live BTC/ETH prices from Coinbase API
  - Saves price history with timestamps
  - Clean menu interface

---

## Phase 3 — REST API with FastAPI ✅

### What I learned

- FastAPI — creating an app, running a server
- Decorators — @app.get, @app.post, @app.delete
- Pydantic — data validation with BaseModel
- Path parameters — /todos/{id}
- SQLAlchemy — connecting to database, creating models
- SQLite — persistent storage
- CRUD — Create, Read, Update, Delete
- Virtual environments — venv
- Git & GitHub — pushing projects to portfolio
- CORS — allowing frontend to talk to API
- JWT — JSON Web Tokens for authentication
- Password hashing — never store plain passwords
- Protected routes — Depends(oauth2_scheme)

### What I built

- Todo REST API
  - GET /todos — returns all todos
  - POST /todos — protected, requires JWT token
  - DELETE /todos/{id} — deletes a todo
  - SQLite database — data persists on restart

- Auth System
  - POST /register — creates account, hashes password
  - POST /login — verifies password, returns JWT token
  - GET /me — protected route, returns logged in user

- Todo Frontend
  - HTML + CSS + JavaScript
  - Talks directly to FastAPI backend
  - Add and delete todos visually

---

## Key Concepts to Remember

| Concept                 | What it means                                      |
| ----------------------- | -------------------------------------------------- |
| return vs print         | return sends value back, print just displays       |
| Clean before validate   | Always strip/lowercase before checking length      |
| db.add() vs db.commit() | add queues it, commit saves it permanently         |
| JWT token               | Contains username + expiry, signed with SECRET_KEY |
| Password hashing        | One-way scramble, use verify() to check            |
| 401 vs 400              | 401 = not authenticated, 400 = bad request         |

---

## Projects on GitHub

- crypto_checker.py — Crypto Price Checker CLI
- api.py — Todo REST API with database
- auth.py — JWT Authentication System
- index.html — Todo Frontend

---

## What's Next 🎯

- [ ] Done/undone toggle for todos
- [ ] Connect frontend login to auth system
- [ ] Deploy API online
- [ ] Build a full project from scratch independently

---

## How to Run Projects

### Todo API

```bash
cd PythonFullCourseforBeginners
source venv/bin/activate
uvicorn api:app --reload --port 8000
```

### Auth System

```bash
source venv/bin/activate
uvicorn auth:app --reload --port 8001
```

### Crypto Checker

```bash
source venv/bin/activate
python3 crypto_checker.py
```
