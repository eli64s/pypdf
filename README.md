
<div align="center">
<h1 align="center">
<img src="https://img.icons8.com/?size=192&id=48191&format=png" width="100" />
<br>
pypdf
</h1>
<h3>◦ Empower your PDFs with <i>pypdf!</i></h3>
<h3>◦ Developed with the software and tools listed below.</h3>

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

This repository aims to provide a Python-based solution for searching, deleting, and replacing text in PDF documents. It utilizes the PyMuPDF and pdfplumber libraries to open and edit PDF files. The core functionalities include iterating through each page of the PDF, searching for text matches using a given regex pattern, and replacing them with specified content, such as today's date. This project offers a valuable tool for automating text manipulation in PDF documents, potentially saving significant time and effort for users dealing with large numbers of PDF files.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase follows a modular architecture, separating the main functionality of editing PDF documents into a separate file (`PDF_Parser.py`). The code also incorporates a configuration file (`config.py`) to define variables and settings. |
| **📑 Documentation** | The codebase includes inline comments that explain the purpose and functionality of different sections of code. However, there is room for improvement in terms of providing more detailed documentation, such as function and class-level docstrings. |
| **🧩 Dependencies** | The codebase relies on the PyMuPDF library to parse and edit PDF documents. The use of this library allows for powerful PDF manipulation capabilities. |
| **♻️ Modularity** | The codebase demonstrates modularity by separating the main functionality into a dedicated file (`PDF_Parser.py`). This approach facilitates code organization and reusability. |
| **✔️ Testing** | The codebase does not include any specific testing files or framework. It would benefit from the addition of unit tests to ensure the correctness of the implemented functionalities. |
| **⚡️ Performance** | The codebase efficiently performs text search and replacement operations on PDF documents. However, without performance benchmarks or specific optimization techniques, it is challenging to evaluate the overall performance of the codebase. |
| **🔒 Security** | The codebase does not appear to have any specific security considerations implemented. Given the nature of PDF documents, potential security vulnerabilities should be considered, such as input sanitization and handling potential malicious files. |
| **🔀 Version Control** | The codebase is hosted on GitHub, providing version control capabilities for collaboration and managing changes over time. It is important to note that the repository does not include a `README.md` file or any guidelines for contributors. |
| **🔌 Integrations** | The codebase seamlessly integrates the PyMuPDF library, enabling powerful PDF manipulation capabilities. Integration with other external services or APIs is not present in the provided codebase. |
| **📈 Scalability** | The codebase does not explicitly address scalability concerns. However, since it primarily focuses on PDF text editing, it can easily be extended to support additional PDF manipulation functionalities, such as adding or removing pages, images, or annotations. |

Overall, the codebase demonstrates a modular architecture with a focus on PDF text editing. While it lacks comprehensive documentation, testing, and security considerations, it provides a solid foundation for extending the functionality and integrating with other systems or libraries.

---


## 📂 Project Structure


```bash
repo
├── PDF_Parser.py
├── README.md
├── __pycache__
│   └── config.cpython-37.pyc
├── config.py
├── pdf_original.pdf
└── pdf_updated.pdf

2 directories, 6 files
```

---

## 🧩 Modules

<details closed><summary>Root</summary>

| File          | Summary                                                                                                                                                                                                                                                                                                                                                                                                                  | Module        |
|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------|
| PDF_Parser.py | The provided code snippet allows for the search, deletion, and replacement of text in a PDF document based on a given regex pattern. It utilizes the PyMuPDF library to open and edit the PDF file. The `replace_text_in_pdf` method iterates through each page of the PDF, searches for text matches using the regex pattern, and replaces them with today's date. The updated PDF is then saved as "pdf_updated.pdf".  | PDF_Parser.py |
| config.py     | The provided code snippet represents a configuration file for a PDF document editing application. It includes two core functionalities. First, it defines the file path for the original PDF document to be edited. Second, it sets a regular expression pattern to search for specific text patterns in the document, in this case, dates in the format "November DD, YYYY", which will be replaced by the application. | config.py     |

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
python parse_pdf_regex.py
```

### 🧪 Running Tests
```sh
pytest
```

---


## 🗺 Roadmap

- [ ] Implement more PDF parsing functionalities.
- [ ] Add unit tests.

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
