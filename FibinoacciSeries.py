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

        if self.fnum < 0 or self.fnum == 0:
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
    parser.add_argument("--input",required=True, type=int,
                        help="Enter an integer <= 1", dest="fnum")                 
    return parser

if __name__ == '__main__':
    parser = FSeries_Parser()
    args = parser.parse_args()
    if args.fnum > 0:
        print(f"\nFibinocci Series of {args.fnum} numbers is:")
    fobject = FibinoacciSeries(args.fnum)
    fobject.to_print_fseries()