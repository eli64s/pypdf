# Searches for a value in a PDF document to delete and replace with a new value

from datetime import date
import fitz 
import re 

class ParsePDF: 
    
    # Constructor 
    def __init__(self, path, regex_pattern): 
        self.path = path 
        self.regex_pattern = regex_pattern


    @staticmethod
    def find_pdf_text_to_delete(lines): 
        """
        Static method working independent of the class object.
        Get all the lines of the PDF document.
        """
        # Iterate through each line of the PDF document
        for line in lines: 
            # Look for regex pattern match in each line
            if re.search(regex_pattern, line, re.IGNORECASE): 
                search = re.search(regex_pattern, line, re.IGNORECASE) 
                # Yield creates a generator to return values in between function iterations 
                yield search.group(1) 
  

    def edit_pdf_file(self): 
        """
        Sets today's date in the PDF document.
        """
        # Open the PDF file for editing 
        document = fitz.open(self.path) 
        # Iterate through each page of the PDF document 
        for page in document: 
            # _wrapContents is needed for fixing alignment issues with rect boxes in some cases where there is alignment issue 
            page._wrapContents() 
            # Gets the rect boxes which consists of the matching regex pattern
            text_date = self.find_pdf_text_to_delete(page.getText("develop").split('\n')) 

            for data in text_date: 
                areas = page.searchFor(data) 
                [page.addRedactAnnot(area) for area in areas] 
            page.apply_redactions() 
              
        # Define today's date as the variable to replace the deleted value
        # And set the PDF coordinates for placing the new value
        page = document[0]         
        coordinates = fitz.Point(453, 58) 
        todays_date = date.today()
        todays_date = f"""{todays_date.strftime("%B")} {todays_date.day}, {todays_date.year}"""

        # Set the new text in the PDF file
        update_text = page.insertText(coordinates, todays_date, fontname = "helv", fontsize = 9.5)
        
        # Save the updated PDF file 
        document.save(path.format("PDF_After"))    


# Main method to run script
if __name__ == "__main__": 

    # File path of the unedited PDF document
    path = r"C:\Users\Eli\Desktop\Python\Scripts\{}.pdf"

    # Regex pattern string to search for specified text to be removed from the PDF
    regex_pattern = r"(Nov(?:ember)?\s([1-9]|([12][0-9])|(3[01])),\s\d\d\d\d)"

    # Create instance of the ParsePDF class
    parse_pdf = ParsePDF(path.format("test"), regex_pattern) 

    # Call edit_pdf_file method 
    parse_pdf.edit_pdf_file()