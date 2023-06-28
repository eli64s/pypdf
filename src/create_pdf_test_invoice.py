"""Create a test PDF document with a random invoice."""

import random
from pathlib import Path

from fpdf import FPDF

from conf import read_config_file


class PyPDF(FPDF):

    def __init__(self, pdf_output_path: str, orientation: str = "P"):
        super().__init__(orientation=orientation)
        self.pdf_output_path = pdf_output_path

    def header(self) -> None:
        # Set up the header
        self.set_font("Arial", "B", 12)
        self.cell(80)
        self.cell(30, 10, "Random Invoice", 1, 0, "C")
        self.ln(20)

    def footer(self):
        # Page footer
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, "Page %s" % self.page_no(), 0, 0, "C")

    def generate_invoice(self):
        # Generate the invoice content
        names = ["Jane Doe", "Steve Cook", "Alice in Wonderland", "Elon"]
        amounts = ["$100", "$200", "$300", "$400", "$500"]

        # Set up the table headers
        self.set_font("Arial", "B", 10)
        self.cell(40, 10, "Name", 1)
        self.cell(40, 10, "Amount", 1)
        self.ln()

        # Add random names and amounts to the invoice
        self.set_font("Arial", "", 10)
        for _ in range(10):
            name = random.choice(names)
            amount = random.choice(amounts)
            self.cell(40, 10, name, 1)
            self.cell(40, 10, amount, 1)
            self.ln()
        self.output(self.pdf_output_path, "F")


# Test the PyPDF class
cfg_path = Path("conf/conf.toml")
cfg = read_config_file(cfg_path)
pdf = PyPDF(cfg.paths.test_pdf)
pdf.add_page()
pdf.generate_invoice()
