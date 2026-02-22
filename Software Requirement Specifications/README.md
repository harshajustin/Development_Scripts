# SRS Template Generator

Professional LaTeX-based Software Requirements Specification document generator with complete folder structure and Cognic AI branding.

## 🎯 Features

- 📄 Professional LaTeX document template with corporate branding
- 📁 Automatic project folder structure creation
- 🎨 Pre-configured styling with Cognic AI theme
- 📑 Modular section organization
- 🔄 Dynamic content generation based on project name
- ✅ Ready-to-compile LaTeX files
- 🏷️ PDF metadata configuration
- 🎨 Watermark and custom headers/footers

## 📦 Installation

No installation required! Uses Python standard library only.

**Requirements:**
- Python 3.x
- LaTeX distribution (TeX Live, MiKTeX, or MacTeX) for PDF compilation

## 🚀 Usage

```bash
python3 create_srs_template.py --name <ProjectName> --version <version>
```

### Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--name` | ✅ Yes | - | The name of your project |
| `--version` | ❌ No | `1.0` | Version number |

### Examples

```bash
# Basic usage
python3 create_srs_template.py --name SequelSpeak --version v3.0

# With default version
python3 create_srs_template.py --name MyProject

# Another example
python3 create_srs_template.py --name ChatBot --version 2.1
```

## 📂 Generated Structure

The script creates a complete project folder with the following structure:

```
ProjectName_SRS/
├── main.tex                          # Main LaTeX document entry point
├── config/
│   └── metadata.tex                  # PDF metadata configuration
├── sections/                         # Modular content sections
│   ├── introduction.tex
│   ├── overall_description.tex
│   ├── external_interface_requirements.tex
│   ├── functional_requirements.tex
│   ├── non_functional_requirements.tex
│   ├── data_entities.tex
│   ├── api_endpoints.tex
│   └── input_output_contracts.tex
├── assets/                           # Directory for images and diagrams
├── README.md                         # Project-specific README
└── .gitignore                        # LaTeX build artifacts
```

## 📝 Document Sections

Each section file is pre-populated with a template structure:

1. **Introduction** - Project overview, purpose, scope, definitions
2. **Overall Description** - Product perspective, user characteristics
3. **External Interface Requirements** - UI, hardware, software interfaces
4. **Functional Requirements** - System functionality and features
5. **Non-Functional Requirements** - Performance, security, scalability
6. **Data Entities** - Database schema, data models
7. **API Endpoints** - REST API specifications
8. **Input/Output Contracts** - Data formats and protocols

## 🔨 Building the PDF

After generation, navigate to the project folder and compile:

```bash
cd ProjectName_SRS
pdflatex main.tex
pdflatex main.tex  # Run twice for table of contents
```

**Alternative using latexmk:**
```bash
latexmk -pdf main.tex
```

## 📋 Required LaTeX Packages

The template automatically loads these packages (included in most LaTeX distributions):

- `inputenc` - UTF-8 encoding support
- `geometry` - Page margins configuration
- `setspace` - Line spacing control
- `titlesec` - Section title formatting
- `xcolor` - Color definitions
- `hyperref` - PDF hyperlinks and metadata
- `enumitem` - Enhanced lists
- `fancyhdr` - Custom headers and footers
- `draftwatermark` - Watermark support
- `tabularx`, `booktabs`, `longtable` - Table formatting
- `float` - Figure positioning

## ⚙️ Customization

### Changing Corporate Branding

Edit the generated `main.tex` file:

```latex
% Change corporate color
\definecolor{corporateBlue}{RGB}{0, 51, 102}  % Modify RGB values

% Change watermark
\SetWatermarkText{Your Company}
```

### Adding New Sections

1. Create a new `.tex` file in the `sections/` folder
2. Add `\input{ProjectName_SRS/sections/your_section}` in `main.tex`

### Modifying Metadata

Edit `config/metadata.tex` to customize PDF properties:
- Title
- Author
- Subject
- Keywords

## 🎨 Styling Features

- **Corporate Blue Theme** - Professional color scheme
- **Watermark** - Subtle background branding
- **Custom Headers/Footers** - Document title and page numbers
- **Table of Contents** - Auto-generated navigation
- **Hyperlinked Cross-References** - Easy navigation in PDF

## 🐛 Troubleshooting

### LaTeX Compilation Errors

**Missing packages:**
```bash
# Ubuntu/Debian
sudo apt-get install texlive-full

# macOS (Homebrew)
brew install --cask mactex

# Windows
# Download and install MiKTeX from miktex.org
```

**Table of contents not appearing:**
- Run `pdflatex main.tex` twice

**Watermark issues:**
- Ensure `draftwatermark` package is installed

## 📄 License

[Specify your license]

## 👥 Author

Cognic AI Development Team

## 🔗 Related Tools

- [FastAPI Backend Generator](../Backend/FastAPI/README.md)
- [Research Repository Template Generator](../Research_Template/README.md)

## 📞 Support

For issues or questions, please open an issue in the [main repository](../).
