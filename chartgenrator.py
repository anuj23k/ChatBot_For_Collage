import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def create_chart():
    fpath="static/Knowladge_base"
    kn_df=pd.read_excel(fpath+"/CB_Knowledgebase3.xlsx")
    df=(kn_df.groupby(['Category'])['Frequency'].sum().sort_values(ascending=False))
    plt.figure(figsize=(6,4), facecolor='w')
    plt.xlabel('Category')
    plt.ylabel('Frequency')
    df.plot(kind='pie', ylabel="")
    plt.savefig("static/graph/frequency_pie.png")