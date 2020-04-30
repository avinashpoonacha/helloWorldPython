import shutil
from zipfile import ZipFile
import os

fromlocation= '/Users/Developer/Downloads/The Data Science Course 2020 - All Resources'
tolocation= '/Users/Developer/Documents/Data Science Learning'


# move from Downloads to New Location
if (os.path.exists(fromlocation)):
    if os.path.exists(tolocation):
        shutil.move(fromlocation,tolocation)
    else:
        print('path does not exist , hence creating one ')
        os.makedirs(tolocation)
        shutil.move(fromlocation,tolocation)
else:
    print(' from path specified is wrong !!')



def get_all_file_paths(directory):
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths

def main():
    file_paths = get_all_file_paths(tolocation)

    with ZipFile('/Users/Developer/Documents/my_files.zip','w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)
            print("Successfully Zipped")


if __name__ == "__main__":
    main()