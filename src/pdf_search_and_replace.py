# Searches for a value in a PDF document to delete and replace with a new value

import re
from datetime import date
from pathlib import Path

import fitz

from conf import read_config_file


class ParsePdf:
    """Searches for a value in a PDF document to delete and replace with a new value."""

    def __init__(self, cfg, regex_pattern):
        self.input_path = cfg.paths.input
        self.output_path = cfg.paths.output
        self.regex_pattern = regex_pattern

    @staticmethod
    def search_pdf_for_text_match(lines):
        """Search PDF for text match."""
        for line in lines:
            if re.search(regex_pattern, line, re.IGNORECASE):
                search = re.search(regex_pattern, line, re.IGNORECASE)
                yield search.group(1)

    def replace_text_in_pdf(self):
        """Replace text in PDF document."""
        document = fitz.open(self.input_path)
        for page in document:
            # Gets the rect boxes which consists of the matching regex pattern
            text_date = self.search_pdf_for_text_match(
                page.get_text("develop").split("\n"))

            for data in text_date:
                areas = page.search_for(data)
                [page.add_redact_annot(area) for area in areas]
            page.apply_redactions()

        # Set the PDF coordinates for placing the new value
        page = document[0]
        coordinates = fitz.Point(440, 58)
        todays_date = date.today()
        todays_date = (
            f"""{todays_date.strftime("%B")} {todays_date.day}, {todays_date.year}"""
        )
        update_text = page.insert_text(coordinates,
                                       todays_date,
                                       fontname="helv",
                                       fontsize=16)
        document.save(self.output_path)


if __name__ == "__main__":
    cfg_path = Path("conf/conf.toml")
    cfg = read_config_file(cfg_path)
    regex_pattern = r"(Nov(?:ember)?\s([1-9]|([12][0-9])|(3[01])),\s\d\d\d\d)"
    parse_pdf = ParsePdf(cfg, regex_pattern)
    parse_pdf.replace_text_in_pdf()
