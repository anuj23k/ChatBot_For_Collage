import pandas as pd
my_df=pd.read_excel("static/Knowladge_base/CB_knowledgebase.xlsx")

question=input("Enter your query: ")

selected=my_df[["Answer"]]
for  answer in selected:
    if my_df[my_df["Question"]].str.contains(question):
        print(answer)
        break
else:
    selected=selected+1    
