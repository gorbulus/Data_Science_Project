# main.py
# William Ponton
# 2.17.19
# Exploring Pandas and visualizations for RMOTR final project.
# Wine Survey datatset

# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




# Main functino
def main():
    # Open a csv file from data folder.
    df1 = pd.read_csv("winemag-data_first150k.csv")
    df2 = pd.read_csv("winemag-data-130k-v2.csv")
    
    df1.head()

# Control initiating event
if __name__ == "__main__":
    main()
