# FastAPI Backend Generator

Bootstrap script for creating a complete FastAPI backend project structure with best practices and common components.

## 🎯 Features

- 🏗️ Complete backend folder structure
- 📦 Python package organization with proper `__init__.py` files
- 🗄️ SQLAlchemy database setup
- ⚙️ Pydantic settings configuration
- 📝 Logging configuration
- 🧪 Test directory structure
- 🔒 Environment file templates
- 📋 Pre-configured `.gitignore`
- 📚 API versioning structure (v1 ready)

## 📦 Installation

No installation required! Uses Python standard library only.

## 🚀 Usage

```bash
python3 fastapi_script.py --project-name <ProjectName>
```

### Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--project-name` | ❌ No | `.` (current directory) | Root project folder name |

### Examples

```bash
# Create backend in a new project folder
python3 fastapi_script.py --project-name MyApp

# Create in current directory
python3 fastapi_script.py

# Another example
python3 fastapi_script.py --project-name ChatAPI
```

## 📂 Generated Structure

```
ProjectName/
├── backend/
│   ├── main.py                      # FastAPI application entry point
│   ├── config.py                    # Settings/configuration
│   ├── database.py                  # SQLAlchemy setup
│   ├── logging_config.py            # Logging configuration
│   ├── requirements.txt             # Python dependencies
│   ├── README.md                    # Backend-specific README
│   ├── .env                         # Environment variables (empty)
│   ├── .env.example                 # Environment template
│   │
│   ├── api/                         # API layer
│   │   ├── __init__.py
│   │   └── v1/                      # API version 1
│   │       └── __init__.py
│   │
│   ├── schemas/                     # Pydantic models/schemas
│   │   └── __init__.py
│   │
│   ├── services/                    # Business logic layer
│   │   └── __init__.py
│   │
│   ├── repositories/                # Data access layer
│   │   └── __init__.py
│   │
│   ├── models/                      # SQLAlchemy models
│   │   └── __init__.py
│   │
│   ├── utils/                       # Utility functions
│   │   └── __init__.py
│   │
│   ├── alembic/                     # Database migrations
│   ├── tests/                       # Test files
│   ├── scripts/                     # Utility scripts
│   └── logs/                        # Log files
│
└── .gitignore                       # Git ignore rules
```

## 📝 Generated Files

### `main.py`

Basic FastAPI application with a health check endpoint:

```python
from fastapi import FastAPI

app = FastAPI(title="Backend API")

@app.get("/")
async def root():
    return {"status": "ok"}
```

### `config.py`

Pydantic settings for configuration management:

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Backend"
    environment: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()
```

### `database.py`

SQLAlchemy database setup:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
```

### `requirements.txt`

Pre-configured dependencies:

```
fastapi
uvicorn
sqlalchemy
pydantic-settings
```

## 🏃 Running the Backend

After generating the structure:

```bash
cd ProjectName/backend

# Install dependencies
pip install -r requirements.txt

# Run the development server
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

Once running, access interactive documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🏗️ Architecture

The generated structure follows clean architecture principles:

### Layer Organization

1. **API Layer** (`api/`)
   - Route definitions
   - Request/response handling
   - API versioning

2. **Schema Layer** (`schemas/`)
   - Pydantic models for validation
   - Request/response DTOs

3. **Service Layer** (`services/`)
   - Business logic
   - Application workflows

4. **Repository Layer** (`repositories/`)
   - Data access abstraction
   - Database operations

5. **Model Layer** (`models/`)
   - SQLAlchemy ORM models
   - Database schema definitions

6. **Utils** (`utils/`)
   - Helper functions
   - Shared utilities

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the backend directory:

```env
APP_NAME=My FastAPI App
ENVIRONMENT=development
DATABASE_URL=sqlite:///./app.db
SECRET_KEY=your-secret-key-here
```

### Database Setup

1. Configure `DATABASE_URL` in `.env`
2. Create database models in `models/`
3. Use Alembic for migrations:

```bash
# Initialize Alembic (if needed)
alembic init alembic

# Create migration
alembic revision --autogenerate -m "Initial migration"

# Apply migration
alembic upgrade head
```

## 🧪 Testing

Add tests in the `tests/` directory:

```bash
# Install pytest
pip install pytest pytest-asyncio httpx

# Run tests
pytest
```

## 📦 Dependencies

### Core Dependencies

- **FastAPI** - Modern web framework
- **Uvicorn** - ASGI server
- **SQLAlchemy** - ORM for database operations
- **Pydantic Settings** - Configuration management

### Recommended Additional Packages

```bash
pip install alembic          # Database migrations
pip install python-multipart # Form data support
pip install python-jose      # JWT tokens
pip install passlib          # Password hashing
pip install pytest           # Testing
```

## 🔒 Security Best Practices

1. Never commit `.env` files (already in `.gitignore`)
2. Use environment variables for sensitive data
3. Implement proper authentication/authorization
4. Validate all input with Pydantic schemas
5. Use HTTPS in production

## 🚀 Production Deployment

### Using Gunicorn with Uvicorn workers:

```bash
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### Using Docker:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 📖 Next Steps

After generating the structure:

1. ✅ Install dependencies: `pip install -r requirements.txt`
2. ✅ Configure environment variables in `.env`
3. ✅ Define database models in `models/`
4. ✅ Create schemas in `schemas/`
5. ✅ Implement business logic in `services/`
6. ✅ Add API routes in `api/v1/`
7. ✅ Write tests in `tests/`
8. ✅ Run the application: `uvicorn main:app --reload`

## 🐛 Troubleshooting

### Import errors
- Ensure all `__init__.py` files exist in package directories
- Check Python path configuration

### Database connection issues
- Verify `DATABASE_URL` in `.env`
- Ensure database server is running (if using PostgreSQL/MySQL)

### Module not found
- Install dependencies: `pip install -r requirements.txt`
- Use virtual environment


## 👥 Author

Cognic AI Development Team

## 🔗 Related Tools

- [SRS Template Generator](../../Software%20Requirement%20Specifications/README.md)
- [Research Repository Template Generator](../../Research_Template/README.md)

## 📞 Support

For issues or questions, please open an issue in the [main repository](../../).
