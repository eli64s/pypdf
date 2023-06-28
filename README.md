
<div align="center">
<h1 align="center">
<img src="https://img.icons8.com/?size=192&id=48191&format=png" width="100" />
<br>
pypdf
</h1>
<h3>◦ Empower your PDFs with <i>pypdf!</i></h3>
<h3>◦ Developed with the software listed below:</h3>

<p align="center">
    <img src="https://img.shields.io/badge/Markdown-000000.svg?stylee&logo=Markdown&logoColor=white" alt="Markdown" />
    <img src="https://img.shields.io/badge/Python-3776AB.svg?stylee&logo=Python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?stylee&logo=Pytest&logoColor=white" alt="pytest" />
    <img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?stylee&logo=GNU-Bash&logoColor=white" alt="Bash" />
    <img src="https://img.shields.io/badge/Anaconda-44A833.svg?&logo=Anaconda&logoColor=white" alt="Anaconda" />
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#️-features)
- [📂 Project Structure](#-project-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✔️ Prerequisites](#️-prerequisites)
  - [💻 Installation](#-installation)
  - [🎮 Using pypdf](#-using-pypdf)
  - [🧪 Running Tests](#-running-tests)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The pypdf project provides a set of Python scripts for manipulating PDF documents. It includes functionalities such as extracting data using regular expressions, searching and replacing specific values, generating test PDFs with random dates and invoices, and applying formatting and linting to the codebase. This project aims to simplify PDF processing tasks by providing easy-to-use scripts that automate various PDF-related operations. Its value proposition lies in its ability to save time and effort by streamlining PDF manipulation workflows.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase follows a modular architecture with separate files for different functionalities, such as PDF parsing, searching, and creating. It also uses a configuration file to define the application's settings, enhancing flexibility and maintainability. |
| **📑 Documentation** | The codebase lacks comprehensive documentation. While some functions and classes have inline comments, there is no overall documentation explaining the codebase's purpose, usage, or high-level architecture. Improved documentation would enhance understandability and ease of maintenance. |
| **🧩 Dependencies** | The codebase relies on several external libraries, such as pdfplumber, fitz, ReportLab, and PyPDF. These libraries provide powerful PDF processing features and save development effort. However, the codebase does not include a detailed explanation of their usage or the reasons behind their selection. |
| **♻️ Modularity** | The codebase demonstrates good modularity by separating functionality into different files. Each file handles a specific aspect of PDF processing, such as parsing, searching, or creating. However, there could be room for further modularization, such as extracting common utility functions into a shared module. |
| **✔️ Testing** | The codebase lacks comprehensive unit tests. While it includes some test files, their coverage is limited. Further testing, including unit tests for individual functions and integration tests for complete scenarios, would help ensure code correctness and maintainability. |
| **⚡️ Performance** | It is difficult to assess performance without specific requirements or benchmarks. However, the codebase makes use of efficient libraries for PDF processing, such as pdfplumber and fitz, which are known for their performance. The codebase would benefit from performance profiling and optimization if performance issues arise. |
| **🔒 Security** | There are no specific security measures mentioned in the codebase. It is important to handle user input, particularly regular expressions and file paths, with caution to mitigate potential security vulnerabilities like path traversal or code injection attacks. |
| **🔀 Version Control** | The codebase is hosted on GitHub, utilizing the Git version control system. This enables collaboration among developers, code version management, and the ability to roll back changes if necessary. The repository contains multiple commits, indicating ongoing development and iterative improvements. |
| **🔌 Integrations** | There are no explicit integrations mentioned in the codebase. However, the codebase could be integrated with other systems or APIs to enhance functionality, such as fetching PDFs from external sources or integrating with document management systems. |
| **📈 Scalability** | The codebase does not exhibit explicit scalability features, such as distributed processing or load balancing. However, its modular architecture allows for adding new functionality or extending existing features without significant code changes. It could benefit from scalability considerations if the application's requirements demand it in the future. |

---


## 📂 Project Structure


```bash
repo
├── Makefile
├── README.md
├── conf
│   └── conf.toml
├── docs
│   ├── example.pdf
│   ├── pdf_input.pdf
│   ├── pdf_updated.pdf
│   └── test_invoice.pdf
├── requirements.txt
├── scripts
│   └── clean.sh
└── src
    ├── conf.py
    ├── create_pdf_test_dates.py
    ├── create_pdf_test_invoice.py
    ├── pdf_parse_by_regex.py
    └── pdf_search_and_replace.py

5 directories, 14 files
```

---

## 🧩 Modules

<details closed><summary>Root</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Module   |
|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| Makefile | The code snippet provides a Makefile with several functionalities.-The `help` target displays a list of commands and their descriptions.-The `style` target applies formatting and linting to the code using tools like autoflake, autopep8, black, flake8, isort, and yapf.-The `clean` target calls the `style` target and then executes a clean.sh script to remove unnecessary files.-The `conda` target creates a conda environment named `pypdf` with Python 3.9 and installs the dependencies specified in requirements.txt.-The `venv` target creates a virtual environment named `pypdf`, activates it, and installs the dependencies specified in requirements.txt. | Makefile |

</details>

<details closed><summary>Scripts</summary>

| File     | Summary                                                                                                                                                                                                                                                                                                                     | Module           |
|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| clean.sh | This code snippet is a bash script that performs various clean-up tasks. It removes backup files, Python cache files, cache directories, VS Code settings, build artifacts, pytest cache, benchmarks, and specific files. This script helps maintain a clean working environment by removing unnecessary files and folders. | scripts/clean.sh |

</details>

<details closed><summary>Src</summary>

| File                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Module                         |
|:---------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------|
| pdf_parse_by_regex.py      | The provided code snippet extracts data from a PDF file using regular expressions. It takes in a PDF file, name pattern, and amount pattern as input, and returns a dictionary mapping names to their corresponding amounts. It uses the pdfplumber library to open the PDF file, and then applies the given patterns to extract the relevant data. Finally, it prints the parsed data in a formatted manner.                                                                                                                   | src/pdf_parse_by_regex.py      |
| conf.py                    | This code snippet defines a configuration file for an application. It uses the `dataclasses` module to define three data classes: `PathsConfig` for paths configuration, `RegexConfig` for regex configuration, and `AppConfig` for overall application configuration. The `read_config_file` function reads the configuration file in TOML format and returns a populated `AppConfig` object.                                                                                                                                  | src/conf.py                    |
| pdf_search_and_replace.py  | The provided code is a Python script that searches for a specific value in a PDF document, identified by a regular expression pattern, and replaces it with a new value. It utilizes the `fitz` library to open and manipulate PDF files, specifically applying redactions to remove the old value and inserting the new value at a specific location on the PDF page. The script reads the configuration from a TOML file and performs the replacement on the specified input PDF, saving the modified PDF to the output path. | src/pdf_search_and_replace.py  |
| create_pdf_test_dates.py   | This code snippet generates a PDF document with random dates displayed on each page. It uses the ReportLab library to create the PDF and the datetime module to generate random dates. The add_random_dates_to_page() function is called twice to add dates to the first and second pages of the PDF. The resulting PDF is saved as "docs/example.pdf".                                                                                                                                                                         | src/create_pdf_test_dates.py   |
| create_pdf_test_invoice.py | The provided code snippet creates a test PDF document with a random invoice. It uses the PyPDF class, which is a subclass of the FPDF library's FPDF class. The PyPDF class includes methods for setting up the header and footer of the PDF document, generating the invoice content, and saving the PDF to the specified output path. The generated invoice includes random names and amounts, which are added to a table in the PDF document.                                                                                | src/create_pdf_test_invoice.py |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
- [Python 3.7+](https://www.python.org/downloads/)
- [pdfplumber](https://github.com/jsvine/pdfplumber)

### 💻 Installation

1. Clone the pypdf repository:
```sh
git clone https://github.com/eli64s/pypdf
```

2. Change to the project directory:
```sh
cd pypdf
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🎮 Using pypdf

```sh
python3 src/pdf_parse_by_regex.py
```

### 🧪 Running Tests
```sh
pytest
```

---


## 🗺 Roadmap

- [ ] Implement more PDF parsing functionalities.
- [ ] Add unit tests for each module.

---

## 🤝 Contributing

[Contributing Guidelines](./CONTRIBUTING.md)

---

## 📄 License

[MIT](./LICENSE)

---

## 👏 Acknowledgments

- [pdfplumber](https://github.com/jsvine/pdfplumber)

---
