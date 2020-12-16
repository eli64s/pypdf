from datetime import date
import fitz 
import re 

class ParsePDF: 
    # Constructor 
    def __init__(self, path, regex_date_pattern): 
        self.path = path 
        self.regex_date_pattern = regex_date_pattern

    @staticmethod
    def find_pdf_text_to_delete(lines): 
        """
        Static method working independent of the class object.
        Get all the lines of the PDF document.
        """
        for line in lines: 
            # Look for regex match in each line
            if re.search(regex_date_pattern, line, re.IGNORECASE): 
                search = re.search(regex_date_pattern, line, re.IGNORECASE) 
                # Yield creates a generator to return values in between function iterations 
                yield search.group(1) 
  
    def edit_pdf_file(self): 
        """ Sets today's date in the PDF document. """
        # Open the PDF file for editing 
        document = fitz.open(self.path) 
          
        # Iterate through the pages of the PDF document 
        for page in document: 
            # _wrapContents is needed for fixing alignment issues with rect boxes in some cases where there is alignment issue 
            page._wrapContents() 
            # geting the rect boxes which consists the matching date regex pattern
            text_date = self.find_pdf_text_to_delete(page.getText("develop").split('\n')) 

            for data in text_date: 
                areas = page.searchFor(data) 
                [page.addRedactAnnot(area) for area in areas] 
            page.apply_redactions() 
              
        # Define today's date and the coordinates to set the date in the PDF file
        page = document[0]         
        pdf_coordinates = fitz.Point(453, 58) 
        curr_date = date.today()
        todays_date = f"""{curr_date.strftime("%B")} {curr_date.day}, {curr_date.year}"""

        # Set the new text in the PDF file
        set_text = page.insertText(pdf_coordinates, todays_date, fontname = "helv", fontsize = 9.5)
        
        # Save the updated PDF file 
        document.save(path.format("PDF_After"))    


# Main method to runs the script
if __name__ == "__main__": 
    path = r"C:\Users\esalam1\Desktop\Python\Scripts\{}.pdf"
    regex_date_pattern = r"(Nov(?:ember)?\s([1-9]|([12][0-9])|(3[01])),\s\d\d\d\d)"
    parse_pdf = ParsePDF(path.format("PDF_Before"), regex_date_pattern) 
    parse_pdf.edit_pdf_file()