import argparse
import re
import logging

"""
This script checks whether the results format for Task 2 is in correct formatting. 

The correct format of the Task 2 results file is the following:
<id>{1-DDDD} <TAB> <text> <TAB> <label> without any column header
where 
    <id> is the order of the text provided in the original dataset file.
    <text> is the original text from the dataset file without editing.
    <label> indicates label of the tweet (positive, negative).
"""

tweet_pattern = re.compile('^[0-9]{1,4}\t(.*?)\t(positive|negative)$')
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)

def check_format(file_path):
    with open(file_path, encoding='UTF-8') as out:
        file_content = out.read().strip()
        for i, line in enumerate(file_content.split('\n')):
            id, text , label = line.strip().split('\t')
            if not tweet_pattern.match("%s\t%s\t%s"%(id,text, label)):
                logging.error("Wrong line format: {}".format(line))
                return False
    logging.info("File in path {} fully scanned ")
    logging.info("Format checking completed successfully. ".format(file_path))
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Checking output format.')
    parser.add_argument('--filename', dest='filename', required=True, help="The full path to the file you want to check.")

    args = parser.parse_args()
    logging.info("Task 2: Checking file: {}".format(args.filename))
    check_format(args.filename)

