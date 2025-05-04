# 🌐 API Service - LLM News Aggregator

The API Service serves as the interface between the frontend and the backend database. It provides RESTful endpoints to retrieve summarized and categorized news stories stored by the Storage Service. This service allows users to query stories by category, and source.

---

## 🛠 Features

- 📥 Fetch summarized news stories from the database
- 🔍 Filter by category, or source
- 🧩 Exposes a clean RESTful API for frontend consumption
- 📦 Dockerized for deployment
- 🔐 Environment-based configuration
- 🔁 Integrated GitHub Actions CI/CD

---

## 🧱 Tech Stack

- **Python** 3.13
- **FastAPI** for REST endpoints
- **SQLAlchemy** for database access
- **PostgreSQL** backend
- **Docker** for containerization
- **GitHub Actions** for CI

---

## 🧪 Local Development

### 1. Clone the repo
```bash
git clone https://github.com/Mustapha-Innocer/api-service.git
cd api-service
```

### 2. Create `.env` file with the appropriate values
```ini
# Database
DB_URL=postgresql://username:password@host:port/dbname

# App config
HOST = localhost
PORT = 8000
ENV = "DEV"
```
### 3. Create new python virtual environment
```bash
python -m venv venv
```

### 4. Intall the python dependencies
```bash
pip install -r requirements.txt
```

### 5. Run
```bash
python server.py
```

---

## 📚 Example Endpoints

* `GET /stories?category=Politics&source=BBC` — Filtered stories
* `GET /categories` — List all categories
* `GET /sources` — List all sources

---

Interactive docs:
📘 Swagger: `host:port/api`

---

## 🧱 Related Services

This is part of a larger microservice-based system. See the [Main Project README](https://github.com/Mustapha-Innocer/news-aggregator) for architecture and links to all services.
