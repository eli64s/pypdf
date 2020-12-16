from datetime import date
import fitz 
import re 

class ParsePDF: 
    # Constructor 
    def __init__(self, path, regex_date): 
        self.path = path 
        self.regex_date = regex_date
    # static methods work independent of class object 
    @staticmethod
    def find_pdf_text_to_delete(lines): 
        """ Get all the lines of the PDF document """
        for line in lines: 
            # matching the regex to each line 
            if re.search(regex_date, line, re.IGNORECASE): 
                search = re.search(regex_date, line, re.IGNORECASE) 
                # yields creates a generator to return values in between function iterations 
                yield search.group(1) 
  
    def edit_pdf_file(self): 
        """
        """
        # Open the PDF file to edit 
        document = fitz.open(self.path) 
          
        # Iterate through the pages of the PDF document 
        for page in document: 
            # _wrapContents is needed for fixing alignment issues with rect boxes in some cases where there is alignment issue 
            page._wrapContents() 
            # geting the rect boxes which consists the matching email regex 
            sensitive = self.find_pdf_text_to_delete(page.getText("develop").split('\n')) 

            for data in sensitive: 
                areas = page.searchFor(data) 
                # drawing outline over sensitive datas 
                [page.addRedactAnnot(area) for area in areas] 
            # applying the edit_pdf_file 
            page.apply_redactions() 
              
        # Insert the new date into the PDF file
        page = document[0]         
        pdf_coordinates = fitz.Point(453, 58) 
        curr_date = date.today()
        todays_date = f"""{curr_date.strftime("%B")} {curr_date.day}, {curr_date.year}"""

        rc = page.insertText(
            pdf_coordinates,  
            todays_date,  
            fontname = "helv",  
            fontsize = 9.5,  
            rotate = 0,  
        )
        
        document.save(path.format("test2"))    


# Main Function that runs the script
if __name__ == "__main__": 
    path = r"C:\Users\esalam1\Desktop\Python\Scripts\{}.pdf"
    regex_date = r"(Nov(?:ember)?\s([1-9]|([12][0-9])|(3[01])),\s\d\d\d\d)"
    parse_pdf = ParsePDF(path.format("test"), regex_date) 
    parse_pdf.edit_pdf_file()