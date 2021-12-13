from pandas import read_excel
del db['Unnamed: 0']
path=input("input file path or name : ")
header_decision=input("input header decision : ")
db=read_excel(path+".xlsx",header=header_decision)
db.drop_duplicates(subset=['Num'], inplace=True)
db.to_excel("no_rep.xlsx")