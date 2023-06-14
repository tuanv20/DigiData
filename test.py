#!/usr/bin/env python 
import csv 
import matplotlib.pyplot as plt
# import seaborn as sns
import pandas as pd

digiDic = {"Name" : [], 
           "Attribute" : [],
           "Stats": []}
with open("./DigiDB_digimonlist.csv", 'r') as digiFile:
    digiReader = csv.reader(digiFile)
    next(digiReader)
    for digimon in digiReader:
        digiDic["Name"].append(digimon[1])
        digiDic["Attribute"].append(digimon[4])
        digiDic["Stats"].append(digimon[7:])

digiDF = pd.DataFrame(digiDic, columns=["Name", "Attribute", "Stats"])
# print(digiDF.to_string())

# Names = ["Number","Name","Stage","Type","Attribute","Memory","Equip Slots","HP","SP","ATK","DEF","INT","SPD"]
# digiDF = pd.read_csv("./DigiDB_digimonlist.csv", names= Names, usecols=["Name","HP","SP","ATK","DEF","INT","SPD"], skiprows=1)
# print(digiDF.to_string())

def handle_input(reqstr):
    match reqstr:
        case "number":
            digi_name = input("Enter a digimon: ")
            show_digi(digi_name)
        case "bar":
            show_bar()

def show_digi(name):
    digimon = digiDF.loc[digiDF["Name"] == name]
    digi_data = digimon.iloc[0]["Stats"]
    # digi_data = [int(x) for x in digi_data]
    digi_labels = ["HP", "SP", "ATK", "DEF", "INT", "SPD"]
    plt.pie(digi_data, labels = digi_labels)
    plt.title(digimon.iloc[0]["Name"])
    plt.show()

def show_bar():
    Attributes = ['Electric', 'Water', 'Wind', 'Dark', 'Earth', 'Fire', 'Light', 'Neutral', 'Plant']
    attrDic = {attr : 0 for attr in Attributes}
    for i in digiDF.index:
        attr = digiDF.iloc[i]["Attribute"]
        attrDic[attr] += 1
    plt.bar(list(attrDic.keys()), list(attrDic.values()))
    plt.title("Number of Digimon of Each Element")
    plt.show()

request = input("What would you like to do? ")
handle_input(request)





