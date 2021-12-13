import pandas
db=pandas.read_excel("poor3-no-rep.xlsx")
del db['Unnamed: 0']
fl=[]
fk=[]
nm=[]
for i in db.Num:
    nm.append(int(str(i).replace(" ","")))
db.Num=nm
for j in db.Num:
    if len(str(j))==9:
        fl.append(True)
    else:
        fl.append(False)
for j in db.Num:
    if len(str(j))==9:
        fk.append(False)
    else:
        fk.append(True)
db[fk].to_excel("poor3-no-probs-out_target.xlsx")
db[fl].to_excel("poor3-no-probs-final.xlsx")