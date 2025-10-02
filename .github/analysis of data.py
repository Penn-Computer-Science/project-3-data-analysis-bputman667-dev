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

print("-_"*20)
print("avg moxie/gustor per num of fishmen") 
print(fishmanData.groupby("numFishmen")["moxieAndGusto"].mean())

print("-_"*20)
print("avg trustworthiness by sympathy level") 
print(fishmanData.groupby("sympathetic")["trustworthy"].mean())

print("-_"*20)
print("top 3 students by sympathy") 
print(fishmanData.sort_values(by="sympathetic", ascending=False).head(3))

print("-_"*20)
print("top 3 students by moxie/gusto") 
print(fishmanData.sort_values(by="moxieAndGusto", ascending=False).head(3))