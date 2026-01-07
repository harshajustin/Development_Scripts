import argparse
from pathlib import Path

# -----------------------------
# Templates
# -----------------------------
MAIN_PY = """from fastapi import FastAPI

app = FastAPI(title="Backend API")

@app.get("/")
async def root():
    return {"status": "ok"}
"""

CONFIG_PY = """from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Backend"
    environment: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()
"""

DATABASE_PY = """from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
"""

LOGGING_PY = """import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
"""

GITIGNORE = """__pycache__/
*.pyc
.env
.env.*
logs/
.alembic/
.vscode/
.idea/
"""

README_MD = """# Backend Service

FastAPI backend generated using a bootstrap script.
"""

REQUIREMENTS = """fastapi
uvicorn
sqlalchemy
pydantic-settings
"""

# -----------------------------
# Folder structure
# -----------------------------
PACKAGE_DIRS = [
    "api",
    "api/v1",
    "schemas",
    "services",
    "repositories",
    "models",
    "utils",
]

PLAIN_DIRS = [
    "alembic",
    "tests",
    "scripts",
    "logs",
]

# -----------------------------
# Helper functions
# -----------------------------
def create_file(path: Path, content: str = ""):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content)
        print(f"📄 Created file: {path}")

def create_init_py(path: Path):
    init_file = path / "__init__.py"
    if not init_file.exists():
        init_file.touch()
        print(f"🐍 Added __init__.py: {init_file}")

# -----------------------------
# Main generator
# -----------------------------
def generate_backend(project_name: str):
    base = Path(project_name).resolve()
    backend = base / "backend"

    print(f"\n🚀 Creating backend structure in: {backend}\n")

    # Base folder
    backend.mkdir(parents=True, exist_ok=True)

    # Create package directories (with __init__.py)
    for folder in PACKAGE_DIRS:
        path = backend / folder
        path.mkdir(parents=True, exist_ok=True)
        create_init_py(path)

    # Create plain directories (NO __init__.py)
    for folder in PLAIN_DIRS:
        (backend / folder).mkdir(parents=True, exist_ok=True)

    # Core files
    create_file(backend / "main.py", MAIN_PY)
    create_file(backend / "config.py", CONFIG_PY)
    create_file(backend / "database.py", DATABASE_PY)
    create_file(backend / "logging_config.py", LOGGING_PY)

    # Root-level files
    create_file(backend / ".env")
    create_file(backend / ".env.example")
    create_file(backend / "requirements.txt", REQUIREMENTS)
    create_file(backend / "README.md", README_MD)
    create_file(base / ".gitignore", GITIGNORE)

    print("\n✅ Backend structure created successfully!\n")

# -----------------------------
# CLI Entry
# -----------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate FastAPI backend folder structure"
    )
    parser.add_argument(
        "--project-name",
        type=str,
        default=".",
        help="Root project folder name (default: current directory)",
    )

    args = parser.parse_args()
    generate_backend(args.project_name)
