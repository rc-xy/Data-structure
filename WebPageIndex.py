import string
import AVLTreeMap 

"""
This file writes a WebPageIndex class that will contain the index representation of a web page. 
Its functionalities are implemented according to assignment descriptions.

Student number: 20146359
Student name: Xinyu Chen
Date: Mar 5, 2021
"""

class WebPageIndex:
    def __init__(self, file):
        # file type has to be .txt
        if not file.endswith('txt'):
            raise NameError("File must be a '.txt extension.")
        
        self.my_file = open(file, 'r')
        self.my_file_content = None

    def read_file(self):
        # Create a list to put the content in input text file
        content = []

        # Read lines in lower case
        line = self.my_file.readline().lower()

        # Reference to eliminating punctuations: https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
        for c in string.punctuation:
            line = line.replace(c, " ")

        while line != "":
            content += line.lower().split()
            line = self.my_file.readline().lower()

            # Delete punctuations
            for c in string.punctuation:
                line = line.replace(c, " ")

        # self.my_file.close() 
        self.my_file_content = content
        return content

    # To count the number of times the word s appeared on the page
    def getCount(self, s):
        frequency = 0
        content = self.read_file()

        for i in range(len(content)):
            if content[i] == s:
                frequency += 1
            else:
                pass
        if frequency == 0:
            # return print("The word(s) does not appear on the page.")
            return 0

        return frequency

    def main(self):
        AVL_Tree_Map = AVLTreeMap.AVLTreeMap()

        for index in range(0, len(self.my_file_content)):
            AVL_Tree_Map.put(index, self.my_file_content[index])

        return AVL_Tree_Map





if __name__ == "__main__":
    WebPageContent = WebPageIndex("./data/doc4-stack.txt")
    print("The word appears", WebPageContent.getCount("a"), "times.")
    print(WebPageContent.main())
    
    
    
    
   
    