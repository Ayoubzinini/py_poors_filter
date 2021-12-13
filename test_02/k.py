import pandas as pd
def check_rep(file,cible,header_decision):
  df=pd.read_excel(file,header=header_decision)
  return "Nombre de fiches répetées : "+str(len(df.index)-len(df[cible].unique()))
db=pd.read_excel("poor3-no-probs.xlsx",header=0)
del db['Unnamed: 0']
db.drop_duplicates(subset=["Num"], inplace=True)
db.to_excel("poor3-no-rep.xlsx")