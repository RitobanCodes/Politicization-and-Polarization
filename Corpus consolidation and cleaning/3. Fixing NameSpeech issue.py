import os
import pandas as pd

os.chdir("C:/Ritoban/IIMK")

Year = 2002
folder_location = "Corpus Preprocessing/" + str(Year) + "/" + str(Year) + " Combined.csv"

df = pd.read_csv(folder_location)


