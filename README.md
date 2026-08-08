# Knowledge Base API

A production-style backend API built with **FastAPI** that provides secure authentication and immutable document versioning.

Instead of overwriting document content, every edit creates a new version, preserving the complete history. Restoring an older version creates a brand-new latest version rather than modifying history.

---

## Features

### Authentication

- User Registration
- User Login
- JWT Access Tokens
- JWT Refresh Tokens
- Refresh Token Rotation
- Current User Endpoint

### Document Management

- Create Documents
- View Documents
- List User Documents
- Edit Documents
- Delete Documents

### Version Control

- Automatic Version 1 creation
- Immutable Version History
- View Complete Version History
- Restore Previous Versions
- Current Version Tracking

### Security

- Password hashing using bcrypt
- JWT authentication
- Ownership-based authorization
- Protected endpoints
- Session-based refresh token management

### Database

- PostgreSQL
- SQLAlchemy ORM
- Alembic Migrations
- Relational data model
- Composite unique constraints for document versions

### Testing

- FastAPI TestClient
- Integration testing of API flows
- Authentication flow validation
- Database verification during development

---

# Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- JWT
- bcrypt
- Pytest
- TestClient

---

# Project Structure

```
app/
│
├── core/
│   ├── config.py
│   ├── security.py
│   ├── dependencies.py
│
├── db/
│   ├── database.py
│   ├── models.py
│
├── signup/
├── login/
├── refresh/
├── users/
├── documents/
│
└── main.py

tests/
├── integration/
└── Unit/
```

---

# Architecture

The project follows a layered architecture.

```
Client
    │
Routes
    │
Services
    │
Repositories
    │
PostgreSQL
```

### Responsibilities

**Routes**

- Validate requests
- Return HTTP responses
- Call business services

**Services**

- Business logic
- Version creation
- Authentication
- Authorization
- Transactions

**Repositories**

- Database operations only

---

# Authentication Flow

```
Register
      │
      ▼
Login
      │
      ▼
Access Token
Refresh Token
      │
      ▼
Protected Endpoints
      │
      ▼
Refresh Rotation
```

---

# Document Versioning

Every modification creates a completely new version.

```
Version 1

↓

Version 2

↓

Version 3

↓

Restore Version 1

↓

Version 4 (Copy of Version 1)
```

Previous versions are never modified or deleted.

---

# Database Overview

Main entities:

- User
- Artifact (credential storage)
- Session
- Document
- DocumentVersion

Relationships

```
User
 ├── Sessions
 ├── Documents
 └── Artifact

Document
 └── DocumentVersions
```

---

# Running the Project

## Clone

```bash
git clone <repository-url>
cd final_project
```

## Create virtual environment

```bash
python -m venv venv
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure environment

Create a `.env` file and provide:

```env
DATABASE_URL=...
SECRET_KEY=...
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=...
REFRESH_TOKEN_EXPIRE_DAYS=...
```

## Run migrations

```bash
alembic upgrade head
```

## Start server

```bash
uvicorn main:app --reload
```

---

# Running Tests

```bash
pytest
```

---

# API Overview

## Authentication

- Register
- Login
- Refresh Token
- Get Current User

## Documents

- Create Document
- Get Document
- List Documents
- Update Document
- Delete Document
- Get Version History
- Restore Version

---

# Design Decisions

### Immutable Version History

Documents are never updated in place.

Every edit creates a new version, ensuring complete historical tracking and allowing safe restoration.

### Refresh Token Rotation

Every refresh invalidates the previous refresh token and issues a new one, reducing the risk associated with token theft.

### Layered Architecture

Separating routes, services, and repositories keeps business logic independent from HTTP handling and database access.

---

# Future Improvements

- Docker support
- CI/CD with GitHub Actions
- Structured logging
- Custom exception hierarchy
- Soft delete
- Search functionality
- Role-Based Access Control (RBAC)
- Document sharing
- Deployment

---

# What I Learned

This project strengthened my understanding of:

- Backend architecture
- JWT authentication
- Refresh token rotation
- SQLAlchemy ORM
- Database design
- API testing with FastAPI TestClient
- Layered application design
- Immutable data modeling
- Debugging production-style backend systems