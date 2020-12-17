# Searches for a value in a PDF document to delete and replace with a new value

import config
import fitz 
import re 
from datetime import date

class ParsePDF: 

    # Constructor 
    def __init__(self, path, regex_pattern): 
        self.path = path 
        self.regex_pattern = regex_pattern


    @staticmethod
    def search_pdf_for_text_match(lines): 
        """
        Static method working independent of the class object.
        Iterate through each line of the PDF document to search
        for text that matches the regex pattern defined in config.py
        """
        for line in lines: 
            # Check if line matches the regex pattern
            if re.search(regex_pattern, line, re.IGNORECASE): 
                search = re.search(regex_pattern, line, re.IGNORECASE) 
                # Yield creates a generator to return values in between function iterations 
                yield search.group(1) 
  

    def replace_text_in_pdf(self): 
        """
        Replaces the text matches in the PDF document
        with today's date.
        """
        # Open the PDF file for editing 
        document = fitz.open(self.path) 
        # Iterate through each page of the PDF document 
        for page in document: 
            # _wrapContents is needed for fixing alignment issues with rect boxes in some cases where there is alignment issue 
            page._wrapContents() 
            # Gets the rect boxes which consists of the matching regex pattern
            text_date = self.search_pdf_for_text_match(page.getText("develop").split('\n')) 

            for data in text_date: 
                areas = page.searchFor(data) 
                [page.addRedactAnnot(area) for area in areas] 
            page.apply_redactions() 
              
        # Define today's date as the variable to replace the deleted value
        # And set the PDF coordinates for placing the new value
        page = document[0]         
        coordinates = fitz.Point(440, 58) 
        todays_date = date.today()
        todays_date = f"""{todays_date.strftime("%B")} {todays_date.day}, {todays_date.year}"""

        # Set the new text in the PDF file
        update_text = page.insertText(coordinates, todays_date, fontname = "helv", fontsize = 16)
        
        # Save the updated PDF file 
        document.save("pdf_updated.pdf")    


# Main method
if __name__ == "__main__": 

    # File path of the unedited PDF document
    path = config.Config.FILE_PATH

    # Regex pattern string to search for specified text to be removed from the PDF
    # In this example, text is replaced if it matches the date format "November DD, YYYY"
    regex_pattern = config.Config.REGEX_PATTERN

    # Create instance of the ParsePDF class
    parse_pdf = ParsePDF(path, regex_pattern) 

    # Call edit_pdf_file method 
    parse_pdf.replace_text_in_pdf()