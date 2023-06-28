"""Extract data from PDF using regex pattern mappings."""

import logging
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict

import pdfplumber

from conf import read_config_file


def extract_data_from_pdf(pdf_file: Path, name_pattern: str,
                          amount_pattern: str) -> Dict[str, int]:
    """
    Open the PDF file, extract names and amounts based on given patterns,
    and return a dictionary of names with their corresponding amounts.
    """
    data_dict = defaultdict(int)

    try:
        with pdfplumber.open(pdf_file) as pdf:
            pattern = re.compile(name_pattern + "[ ]+" + amount_pattern)
            for page in pdf.pages:
                text = page.extract_text()
                matches = pattern.findall(text)
                for name, amount in matches:
                    data_dict[name.strip()] += int(amount)

    except FileNotFoundError:
        logging.error(f"Error: The file {pdf_file} was not found.")
    except re.error:
        logging.error("Error: Invalid regular expression.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")

    return data_dict


# Test the extract_data_from_pdf function
config_path = Path("conf/conf.toml")
cfg = read_config_file(config_path)

name_pattern = cfg.regex.name_pattern
amount_pattern = cfg.regex.amount_pattern
pdf_path = cfg.paths.test_pdf

parsed_data = extract_data_from_pdf(pdf_path, name_pattern, amount_pattern)
print(parsed_data)
print(f'{"Name":<20} {"Amount"}')
for name, amount in parsed_data.items():
    print(f"{name:<20} ${amount}")
