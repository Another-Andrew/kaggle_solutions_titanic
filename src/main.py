import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns 
import matplotlib.pyplot as plt

import os

# Using the fancy function declaration that isn't needed.
# The only purpose is to show that the function will try to return a 'pd.DataFrame' object and that it takes a 'str' object as a parameter.
# The following is also an entirely valid function declaration:
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/
# def ingestData(data_dir):
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\

def ingestData(data_dir: str, target_filename: str) -> pd.DataFrame:
    data_dir = os.path.abspath(data_dir) # Retrieves the absolute path of the data directory.
    df_CSV = pd.DataFrame([]) # define training as empty DataFrame

    for dirname, _, filenames in os.walk(data_dir): # Loops though the data directory
        # filename is a single index value from the list filenames[]. 
        for filename in filenames:
            # '.startswith()' is a method of the python string class, it can check to see if 'filename' starts with "train" -> "train.csv" starts with "train"  
            if filename == target_filename:
                # Constructs a full path string when given a directory and the filename in that directory. 
                # Is preferred over concatenating a directory with a filename, because os.path.join() provides error handling and valid path validation.
                path = os.path.join(dirname, filename)  
                print(f'found data: {path}')
                path = os.path.join(dirname, filename) 
                df_CSV = pd.read_csv(path) # Reads training data only if a file called "train.csv" exists
    
    if df_CSV.empty: # This is looking for a bool
        raise FileNotFoundError
    
    return df_CSV

    
def main():
    
    try:
        training = ingestData("../data", "train.csv")
    except FileNotFoundError:
        print("Couldn't find test data. Exiting.")
        return None
    except Exception as e:
        print(f"Unknown error: {e}")
        return None

    print(f'Training info: {training.info()}')
    print(f'Training description: {training.describe()}')
    print(f'Training data columns. {training.describe().columns}')

    # look at numeric and categorical values separately 
    df_num = training[['Age','SibSp','Parch','Fare']]
    df_cat = training[['Survived','Pclass','Sex','Ticket','Cabin','Embarked']]


if __name__ == '__main__':
    main()