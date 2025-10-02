import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

#load our dataframe
df = pd.read_csv("dataFrame2.csv")
fishmanData = pd.DataFrame(df)

print("-_"*20)
print("head of the data frame") #first five rows
print(fishmanData.head())

print("-_"*20)
print("tail of the data frame")
print(fishmanData.tail())

print("-_"*20)
print("summary of the data frame") 
print(fishmanData.info())

print("-_"*20)
print("stats of the data frame") 
print(round(fishmanData.describe()))

print("-_"*20)
print("head of the data frame")
print(fishmanData.head())

print("-_"*20)
print("first student data") 
print(fishmanData.iloc[0])

