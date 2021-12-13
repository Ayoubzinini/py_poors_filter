from pandas import read_excel
def phone_filter(cible,db):
  Filter_06=[]
  Filter_07=[]
  strn=[]
  for i in db[cible]:
    strn.append(str(i)) 
  for j in strn:
    Filter_06.append(j.startswith("6"))
    Filter_07.append(j.startswith("7"))
  frames = [db[Filter_06], db[Filter_07]]
  result = pd.concat(frames)
  return result
path=input("input file path or name : ")
header_decision=input("input header decision : ")
db=read_excel(path+".xlsx",header=header_decision)
phone_filter("Num",db).to_excel("filtred_cellphones.xlsx")