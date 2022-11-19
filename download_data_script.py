"""

Downloads csv data from the given input website to a local filepath as a csv.

Usage: download_data.py --url=<url> --output_file=<output_file> 
 
Options:

--url=<url>             The URL from where the data needs to be downloaded (csv format)
--output_file=<output_file>   path in your local system where the the csv to be saved and desired name of the csv file

Example script to run in terminal: 

python download_data.py --url="https://archive.ics.uci.edu/ml/machine-learning-databases/00383/risk_factors_cervical_cancer.csv" --output_file="rfcc.csv"

"""

#import necessary libraries
import os
import pandas as pd
from docopt import docopt

# initialize docopt
dc = docopt(__doc__)

#function to read the csv and download the csv to the local system

def main(url, output_file):
    data = pd.read_csv(url, header=None)
    try:
        data.to_csv(output_file, index=False)
    except:
        os.makedirs(os.path.dirname(out_file))
        data.to_csv(output_file, index=False)


if __name__ == "__main__":
    main(dc["--url"], dc["--output_file"])