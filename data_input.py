from os import path
import sys
import pandas as pd

class DataInput:
    
    # all extensions supported by this project.
    supported_file_extensions = [
        '.csv',
    ]

    # function to convert all the column names of any specific dataset into lowercase.
    def change_to_lower_case(self, data):
        for column in data.columns.values:
            data.rename(columns = {column : column.lower()}, inplace = True)
        return data

    # function that takes any dataset from the input file and convert it into DataFrame.
    # The print statements are well defined and tells about the state of the errors.
    def inputFunction(self):
        try:
            filename, file_extension = path.splitext(sys.argv[1])
            if file_extension == "":
                raise SystemExit("Provide the " + "DATASET"  +" name (with extension).")

            if file_extension not in self.supported_file_extensions:
                raise SystemExit("This file extension is not " + "supported." )
        
        except IndexError:
            raise SystemExit("Provide the "  + "DATASET" +" name (with extension).")
        
        try:
            data = pd.read_csv(filename+file_extension)
        except pd.errors.EmptyDataError:
            raise SystemExit("The file is "+ "EMPTY" )

        except FileNotFoundError:
            raise SystemExit("File " + "doesn't" + " exist")

        data = self.change_to_lower_case(data)

        return data