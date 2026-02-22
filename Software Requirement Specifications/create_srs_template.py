import argparse
from pathlib import Path
from datetime import date


def create_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")


def main():
    parser = argparse.ArgumentParser(description="Cognic AI SRS Template Generator")
    parser.add_argument("--name", required=True, help="Project name")
    parser.add_argument("--version", default="1.0", help="Version number (default: 1.0)")
    args = parser.parse_args()

    project_name = args.name
    version = args.version
    today = date.today().strftime("%B %d, %Y")
    
    # Create project folder
    project_folder = f"{project_name}_SRS"
    base_path = Path(project_folder)

    print(f"\nCreating Cognic AI SRS Template")
    print(f"Project: {project_name}")
    print(f"Version: {version}")
    print(f"Folder: {project_folder}\n")

    # ================= MAIN.TEX =================
    main_tex = f"""
\\documentclass[12pt, a4paper]{{article}}

% ---------------- PACKAGES ---------------- %
\\usepackage[utf8]{{inputenc}}
\\usepackage[margin=1in]{{geometry}}
\\usepackage{{setspace}}
\\usepackage{{titlesec}}
\\usepackage{{xcolor}}
\\usepackage{{hyperref}}
\\usepackage{{enumitem}}
\\usepackage{{fancyhdr}}
\\usepackage{{draftwatermark}}
\\usepackage{{tabularx}}
\\usepackage{{booktabs}}
\\usepackage{{float}}
\\usepackage{{longtable}}

% ---------------- CONFIG ---------------- %
\\onehalfspacing
\\setlength{{\\parskip}}{{0.5em}}
\\setlength{{\\parindent}}{{0pt}}

\\definecolor{{corporateBlue}}{{RGB}}{{0, 51, 102}}

\\input{{{project_folder}/config/metadata}}

\\pagestyle{{fancy}}
\\fancyhf{{}}
\\lhead{{\\footnotesize Software Requirements Specification}}
\\rhead{{\\footnotesize {project_name} v{version}}}
\\cfoot{{\\thepage}}

\\titleformat{{\\section}}{{\\large\\bfseries\\color{{corporateBlue}}}}{{\\thesection.}}{{0.5em}}{{}}
\\titleformat{{\\subsection}}{{\\normalsize\\bfseries}}{{\\thesubsection}}{{0.5em}}{{}}
\\titleformat{{\\subsubsection}}{{\\normalsize\\itshape}}{{\\thesubsubsection}}{{0.5em}}{{}}

% ---------------- DOCUMENT ---------------- %
\\begin{{document}}
\\SetWatermarkText{{}}

\\begin{{titlepage}}
    \\centering
    \\vspace*{{3cm}}
    {{\\Huge \\textbf{{Software Requirements Specification}}}}\\\\[0.5cm]
    {{\\Large for}}\\\\[0.8cm]
    {{\\LARGE \\textbf{{{project_name}}}}}\\\\[0.5cm]
    {{\\large Cognic AI}}\\\\[2cm]
    {{\\large Version {version}}}\\\\[0.5cm]
    {{\\large {today}}}
    \\vfill
\\end{{titlepage}}

\\SetWatermarkText{{Cognic AI}}
\\SetWatermarkScale{{5}}
\\SetWatermarkColor[gray]{{0.93}}
\\SetWatermarkAngle{{45}}
\\SetWatermarkFontSize{{5cm}}

\\tableofcontents
\\newpage

\\input{{{project_folder}/sections/introduction}}
\\input{{{project_folder}/sections/overall description}}
\\input{{{project_folder}/sections/external interface requirements}}
\\input{{{project_folder}/sections/functional requirements}}
\\input{{{project_folder}/sections/non functional requirements}}
\\input{{{project_folder}/sections/data entities}}
\\input{{{project_folder}/sections/api endpoints}}
\\input{{{project_folder}/sections/input output contracts}}

\\end{{document}}
"""

    # ================= METADATA =================
    metadata_tex = f"""
\\hypersetup{{
    colorlinks=true,
    linkcolor=corporateBlue,
    urlcolor=corporateBlue,
    citecolor=corporateBlue,
    pdftitle={{ {project_name} v{version} - Software Requirements Specification }},
    pdfauthor={{ Cognic AI }},
    pdfsubject={{ Agentic AI Software Requirements Document }},
    pdfkeywords={{ {project_name}, Cognic AI, SRS, Agentic Systems }},
    pdfcreator={{ LaTeX }},
    pdfproducer={{ pdfLaTeX }},
    pdfdisplaydoctitle=true
}}
"""

    # ================= README =================
    readme = f"""
# {project_name} - SRS

Generated using Cognic AI SRS CLI Template Generator.

## Version
{version}

## Organization
Cognic AI

## Build

pdflatex main.tex

## Structure

- main.tex → document entry
- config/metadata.tex → PDF metadata
- sections/ → modular sections
"""

    gitignore = """
*.aux
*.log
*.out
*.toc
*.pdf
*.synctex.gz
"""

    # ================= CREATE FILES =================
    create_file(base_path / "main.tex", main_tex)
    create_file(base_path / "config/metadata.tex", metadata_tex)
    create_file(base_path / "README.md", readme)
    create_file(base_path / ".gitignore", gitignore)

    section_files = [
        "Introduction.tex",
        "Overall description.tex",
        "External interface requirements.tex",
        "Functional requirements.tex",
        "Non functional requirements.tex",
        "Data entities.tex",
        "API endpoints.tex",
        "Input output contracts.tex",
    ]

    for file in section_files:
        section_name = file.replace(".tex", "")
        section_template = f"""
\\section{{{section_name}}}

Describe the section content here.
"""
        create_file(base_path / "sections" / file, section_template)

    (base_path / "assets").mkdir(parents=True, exist_ok=True)

    print(f"SRS Template Created Successfully in {project_folder}/ folder!")


if __name__ == "__main__":
    main()