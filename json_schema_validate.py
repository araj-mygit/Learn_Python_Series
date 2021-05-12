"""
Python script to validate a Sample Analysis Results JSON file against,
schema written according to draft 4 specifications.

Input:
    Sample Analysis Results JSON file

Output:
    Returns a positive-message or a negative, depending on whether the 
    input json matches the schema or not.

 How to execute.
    1. cd to path where the script is saved.
    2. execute "python3 json_schema_validate.py --json {full path to input json file} 
                        --schema {full path for schema}"
"""

import json
import argparse
import jsonschema
from os.path import expanduser

class ValidateJson():

    """
    ValidateJson class contains methods to input data, read json input and validate the 
    json input aganist given SARJ schema
    """

    def __init__(self, jdata, schema):

        """
        class constructor
        """

        self.jdata = jdata
        self.schema = schema
       
    def load_json(self, file_name):

        """
        Load a json file and return the data 
        """

        with open(file_name, encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data   

    def validate_json(self):

        """
        Function to validate the input json file.
        Returns positive message if the json matches the schema and 
        negative message if the json does not matches the schema.
        """

        flag = 0
        schema_to_match = self.load_json(self.schema)
        data = self.load_json(self.jdata)
        try:
            jsonschema.validate(instance= data, schema=schema_to_match)
            flag = True
            print("\n Given JSON is valid")
        except jsonschema.exceptions.ValidationError as Verr:
            print(Verr)
            flag = False
            print("\n Given JSON is not valid")
        return flag
        
def create_parser(): 

    """
    Function to pass command line arguments.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=str, required=True,
                        help="Input a jsonfile")
    parser.add_argument("--schema", type=str, required=True,
                        help="Input a jsonfile")                                     
    return parser

if __name__ == '__main__':

    parser = create_parser()
    args = parser.parse_args()
    try:
        json_object = ValidateJson(jdata = args.json, schema = args.schema)
    except Exception as allexce:
        print(f"Other exception {allexce}")
    else:
        json_object.validate_json()    
    finally:
        print("Execution completed !!")