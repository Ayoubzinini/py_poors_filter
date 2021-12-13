from pandas import read_excel
path=input("input file path or name : ")
header_decision=input("input header decision : ")
db=read_excel(path+".xlsx",header=header_decision)
ninp=input("Number of columns to check : ")
colnames=[]
for idx in range(1,int(ninp)+1):
  inp=input("input column name "+idx+" : ")
  colnames.append(inp)
for i in colnames:
  print(i," : ",len(db[i].dropna())-len(db[i].dropna().unique()))