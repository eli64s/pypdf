# imports 
import fitz 
import re 
from datetime import date

class Redactor: 
    
    # static methods work independent of class object 
    @staticmethod
    def get_sensitive_data(lines): 
        
        """ Function to get all the lines """
          
        # email regex 
        EMAIL_REG = r'(\d+/\d+/\d+)'
        for line in lines: 
            
            # matching the regex to each line 
            if re.search(EMAIL_REG, line, re.IGNORECASE): 
                search = re.search(EMAIL_REG, line, re.IGNORECASE) 
                  
                # yields creates a generator 
                # generator is used to return 
                # values in between function iterations 
                yield search.group(1) 
  
    # constructor 
    def __init__(self, path): 
        self.path = path 
  
    def redaction(self): 
        
        """ main redactor code """
          
        # opening the pdf 
        doc = fitz.open(self.path) 
          
        # iterating through pages 
        for page in doc: 
            
            # _wrapContents is needed for fixing 
            # alignment issues with rect boxes in some 
            # cases where there is alignment issue 
            page._wrapContents() 
              
            # geting the rect boxes which consists the matching email regex 
            sensitive = self.get_sensitive_data(page.getText("develop") 
                                                .split('\n')) 
            for data in sensitive: 
                areas = page.searchFor(data) 
                  
                # drawing outline over sensitive datas 
                [page.addRedactAnnot(area) for area in areas] 
                  
            # applying the redaction 
            page.apply_redactions() 
              
        # saving it to a new pdf 
        doc.save('test2.pdf') 

# driver code for testing 
if __name__ == "__main__": 
    
    # replace it with name of the pdf file 
    path = 'test.pdf'
    redactor = Redactor(path) 
    redactor.redaction()
              
    doc = fitz.open("test2.pdf")      
    page = doc[0]         
    p = fitz.Point(525,19) 
    text = date.today().strftime("%Y-%m-%d")
    rc = page.insertText(
        p,  
        text,  
        fontname = "helv",  
        fontsize = 12,  
        rotate = 0,  
    )
    doc.save("test3.pdf")