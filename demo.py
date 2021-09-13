""" Demo file """

import glob

def print_files(directory):
    files = glob.glob(directory) 
    print(files)
    for i, f in enumerate(files):
        print('file {} is {}'.format(i, f))

if __name__ == '__main__':
    directory = "/home/nenns2155/*"
    print_files(directory)
