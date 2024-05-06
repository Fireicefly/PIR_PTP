import numpy as np
import matplotlib.pyplot as plt
import os
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def main():
    print(read_file('hardware.log'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
