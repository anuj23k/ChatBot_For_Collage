import pandas as pd
import random
import numpy as np
def search_knowledge(query):
    fpath="static/knowladge_base"
    knowledge_df=pd.read_excel(fpath+"/CB_Knowledgebase3.xlsx")
    # filter=df[df["col_name"]condition]
    match=knowledge_df[knowledge_df["Question"].str.lower().str.contains(query.lower())]
    #blow  commented line will print all matching data
    # print(match)

    if not match.empty:
       ans_count=len(match)
       rand_index=random.randint(0, ans_count -1)
       #Updatting frequency count of current searched question
       cur_ques=match["Question"].values[rand_index]
       knowledge_df["Frequency"]=np.where(knowledge_df['Question']==cur_ques,
       knowledge_df["Frequency"]+1, knowledge_df["Frequency"])
       knowledge_df.to_excel(fpath+"/CB_knoledgebase2.xlsx", index=False)
                                                 
       return match["Answer"].values[0]
    else:
        return "Sorry, I could not understand. Please ask another question."