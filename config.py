# Configuration file

class Config:
    
    # File path of the unedited PDF document
    FILE_PATH = "pdf_original.pdf"

    # Regex pattern string to search for matching text in the PDF document
    # In this example, text is replaced if it matches the date format "November DD, YYYY"
    REGEX_PATTERN = r"(Nov(?:ember)?\s([1-9]|([12][0-9])|(3[01])),\s\d\d\d\d)"
