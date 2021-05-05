"""
 Fibinoacci Series:
    Is a sequence, where each number is the sum of the two preceding ones, starting 
    from 0 and 1, for n > 1, where n is the user input.

    This script prints the Fibinoacci series, where the count of digits is
    equal to the user input which is of data type int.
    
        Input : Total number of integer values the series should contain.
        Output: A series of number where each number is the sum of the two preceding ones,
        starting from 0 and 1 to count (input_value)

    How to execute the script on terminal
        1. cd to path where the script is saved.
        2. execute "python3 FibinoacciSeries.py <--i> 5"
"""
import argparse

class FibinoacciSeries:
   
    def __init__(self, fnum):
        # The try...except block only works if the prraser is not able to handle the data type error.
        try: 
            if not isinstance(fnum, int):
                raise RuntimeError("Input is string, please re-try with numeric entry.")
        except ValueError as ve: 
            print(ve)
        self.fnum = fnum
            
    def to_print_fseries(self):
        """
        Function generate the series if the total number 
        to be present in series is given.

            Input: f_num(count of digits to make the series)
            Output: Fibinoacci series from 0 to count of digits given as input
        """
        
        first = 0
        second = 1
        output_list = []

        if self.fnum < 0 or self.fnum == 0 :
            print("\nWARNING: Enter a positive integer greater than 0 !! ")
        else:    
            for each_num in range(self.fnum):
                print(first)
                output_list.append(first)
                temp = first
                first = second
                second = temp + first
            return output_list    

def FSeries_Parser():
    """
    Parsing and adding command line arguments.
    """
    
    parser = argparse.ArgumentParser()
    #if type = int is not given, then the try...except in the __init__ method works. 
    parser.add_argument("--input",required=True, type=int,
                        help="Enter an integer <= 1")                 
    return parser

if __name__ == '__main__':
    parser = FSeries_Parser()
    args = parser.parse_args()
    try:
        fobject = FibinoacciSeries(args.input)
    except RuntimeError as E:
        print(f"Error occured: {E}")    
    else:    
        print(f"\nFibinocci Series of {args.input} numbers is:")  
        fobject.to_print_fseries()
    finally:
        print("Execution completed !")    

    