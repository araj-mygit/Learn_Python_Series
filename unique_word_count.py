import re
import argparse
import sys
import csv

class FindUniqueWordCount:

    """
    class containing methods to find the unique words from a 
    given text file.

    Input : File with .txt format
    
    Output : Dispalys all the unique words and their count.
    """

    def __init__(self, text):

        """
        Intakes a text file
        """
        self.text = text


    def check_file_extension(self):

        """
        Function checks whether the input file is of .txt extension.
        """
        
        if self.text.endswith('.txt'):
            print("Input file matches the extension")
            return True 
        else: raise ValueError         
        

    def remove_tooltip_reference(self): 

        """
        Function to remove all the tooltip references and periods from the
        text file. 

        Input: Reads the given txt file.
        Processes : 
                1. Create sapce between each sentence after periods. (line.no 55)
                2. Removes all the tooltip references. (line.no 58)
                3. Converts the list to string and removes all the periods.
        Output : A string with no special charaters.        
        """

        self.check_file_extension()
        lines = []
        new_lines = []
        with open(self.text, 'r', encoding = 'utf-8', errors = 'ignore') as txtfile:
            for i in txtfile:
                lines.append(re.sub('\.[^ ]+ ', ' ', i))
            for each_lines in lines:    
                new_lines.append(re.sub('\[\d+\]', ' ', each_lines.strip()))
                      
        list_to_str = (''.join(new_lines))
        string_from_list = ''
        for each in list_to_str:
            if each != '(' and each != ')':
                string_from_list += each
        string_from_list =  re.sub('[\W\_]',' ', string_from_list)           
        return string_from_list 


    def remove_whitespace_from_string(self):

        """
        Removes leading and lagging whitespaces if any.
        """

        remove_whitespace_string = self.remove_tooltip_reference().strip()
        clean_string = remove_whitespace_string.casefold()
        return clean_string


    def get_set_of_unique_word(self):

        """
        Method to find all the unique words from the given text file.
        """

        unique_words =  (set(self.remove_whitespace_from_string().split()))
        #print("The unique words form the given content : \n ",unique_words)
        return unique_words


    def find_unique_word(self):

        """
        Method to count the number of unique words
        """

        set_to_list = list(self.get_set_of_unique_word())        

        with open("UniquewordCount.txt", "w") as file:
            write = csv.writer(file)
            write.writerow(set_to_list)
            file.close()   
        return set_to_list   


def create_parser(): 

    """
    Parser creation
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True,
                        help="Input a text file")                                    
    return parser

if __name__ == '__main__':

    parser = create_parser()
    args = parser.parse_args()
    class_obj = FindUniqueWordCount(text = args.text)
    try:
        class_obj.find_unique_word()
    except ValueError:
            print("Input file extension must be .txt")
            sys.exit()    