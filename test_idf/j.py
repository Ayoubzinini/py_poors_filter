import string
import pandas
import math
criteras=string.ascii_letters+string.punctuation
db=pandas.read_excel("poor3.xlsx")
del db['Unnamed: 0']
nums=db.Num
for i in criteras:
    Filter=[]
    for n in nums:
        if str(n).find(i) != -1:
            Filter.append(False)
        elif str(n).find(i) == -1:
            Filter.append(True)
        elif math.isnan(n)==True:
            Filter.append(False)
        else:
            Filter.append(True)
    db=db[Filter]
    nums=db.Num
    db.Num=nums
db.to_excel("poor3-no-probs.xlsx")
