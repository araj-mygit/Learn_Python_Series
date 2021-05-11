"""
Python script to validate a Sample Analysis Results JSON file against,
schema written accroding to draft 6 specifications.

Input:
    Sample Analysis Results JSON file

Output:
    Returns a positive-message or a negative, depending on whether the 
    input json matches the schema or not.

 How to execute.
    1. cd to path where the script is saved.
    2. execute "python3 json_schema_validate.py --json {full path to input json file}"
"""


import os
import json
import argparse
import jsonschema
import json_schema_validate
from os.path import expanduser


class ValidateJson():

    """
    ValidateJson class contains methods to input data, read json input and validate the 
    json input aganist given SARJ schema
    """

    def __init__(self, jdata):
        self.jdata = jdata

    def get_schema(self):

        """
        Function to read the schema as python object.
        Returns the Python object. 
        """

        path = os.getcwd()
        SARJSchema = os.path.join(path, "Schema","SARJSchema.json")
        with open(SARJSchema) as jsonfile:
            schema = json.load(jsonfile)
        return schema

    def validate_json(self):

        """
        Function to validate the input json file.
        Returns positive message if the json matches the schema and 
        negative message if the json does not matches the schema.
        """
        
        schema_to_match = self.get_schema()
        with open (self.jdata) as json_obj:
            data = json.load(json_obj)
        try:
            jsonschema.validate(instance= data, schema=schema_to_match)
        except jsonschema.exceptions.ValidationError as Verr:
            print(Verr)
            error_message = "Given Json is not valid"
            print("\n", error_message)
            return False

        passed_message = "Given JSON is valid"
        print("\n", passed_message)
        return True    


def cmd_line_args(): 

    """
    Function to pass command line arguments.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=str, required=True,
                        help="Input a jsonfile")                 
    return parser

if __name__ == '__main__':

    parser = cmd_line_args()
    args = parser.parse_args()
    try:
        json_object = ValidateJson(jdata = args.json)
    except Exception as allexce:
        print(f"Other exception: {allexce}")
    else:
        json_object.validate_json()    
    finally:
        print("Execution completed !!")
