# Backend Mission 

Day 1: Initial FastAPI Setup

## Tech Stack
- Python
- FastAPI
- Uvicorn

## How to Run

uvicorn main:app --reload

Server runs at:
http://127.0.0.1:8000

# Backend-Mission: FastAPI CRUD Project

This is a simple **FastAPI backend** project implementing full CRUD operations for items with SQLite database.

## Features

- Full CRUD endpoints:
  - `POST /items` – Create an item
  - `GET /items` – Read all items
  - `GET /items/{id}` – Read a single item
  - `PUT /items/{id}` – Full update
  - `PATCH /items/{id}` – Partial update
  - `DELETE /items/{id}` – Delete an item
- SQLite database support
- Automatic Swagger UI documentation
- GitHub version control

## Setup

1. Clone the repository:

```bash
git clone https://github.com/ShreyasHManju/backend-mission.git
cd backend-mission
