<div align="center">
  <img src="assests/CognicAI.png" alt="Cognic AI Logo" width="800"/>
  
  # Development Scripts
  
  <p><i>A collection of development utilities and automation scripts for project setup and documentation generation.</i></p>
</div>

## Overview

This repository contains various scripts designed to streamline development workflows, including automated template generation for software documentation and backend project initialization.

## 📚 Available Tools

### 1. Software Requirement Specifications (SRS) Template Generator

**Location**: [`Software Requirement Specifications/`](Software%20Requirement%20Specifications/)

Generates professional LaTeX-based Software Requirements Specification documents with complete folder structure and Cognic AI branding.

**Quick Start:**
```bash
cd "Software Requirement Specifications"
python3 create_srs_template.py --name MyProject --version v1.0
```

📖 **[Read Full Documentation →](Software%20Requirement%20Specifications/README.md)**

---

### 2. FastAPI Backend Generator

**Location**: [`Backend/FastAPI/`](Backend/FastAPI/)

Bootstrap script for creating a complete FastAPI backend project structure with best practices and common components.

**Quick Start:**
```bash
cd Backend/FastAPI
python3 fastapi_script.py --project-name MyApp
```

📖 **[Read Full Documentation →](Backend/FastAPI/README.md)**

---

### 3. Research Repository Template Generator

**Location**: [`Research_Template/`](Research_Template/)

Comprehensive repository structure generator for academic research papers, organizing paper writing, experiments, architecture documentation, and supplementary materials.

**Quick Start:**
```bash
cd Research_Template
mkdir MyResearchProject
cd MyResearchProject
python3 ../create_research_repo.py
```

📖 **[Read Full Documentation →](Research_Template/README.md)**

---

## 🛠️ Installation

Clone this repository:

```bash
git clone https://github.com/harshavardhan/Development_Scripts.git
cd Development_Scripts
```

**Requirements:**
- Python 3.x (standard library only)
- LaTeX distribution (for SRS generator only)

## 📚 Documentation

Each tool has its own detailed README with examples, troubleshooting, and best practices:

- 📄 [SRS Template Generator Documentation](Software%20Requirement%20Specifications/README.md)
- 🚀 [FastAPI Backend Generator Documentation](Backend/FastAPI/README.md)
- 📖 [Research Repository Template Generator Documentation](Research_Template/README.md)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs or issues
- Suggest new features
- Submit pull requests
- Improve documentation

## 👥 Author

**Cognic AI Development Team**

## 📞 Support

For questions, issues, or feature requests:
- Open an issue in this repository
- Check individual tool documentation
- Contact the development team

---

**Made with ❤️ by Cognic AI**
