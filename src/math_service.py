import pandas as pd
from decimal import Decimal
from difflib import SequenceMatcher


def matcher(array1,Array2):
    dataDif= {'Dif1':[],'Dif2':[],'Ratio':[]}
    for x in array1:
        for y in Array2:
            ratio = SequenceMatcher(None,x,y).ratio()
            if Decimal(ratio) >= Decimal(0.95) : 
                dataDif['Dif1'].append(x)
                dataDif['Dif2'].append(y)
                dataDif['Ratio'].append(ratio)
    dfRatio = pd.DataFrame(dataDif)
    return dfRatio

def changer(arrayBase,arrayCompare,key):
    for x in arrayBase[key]:
        for y in arrayCompare[key]:
            ratio = SequenceMatcher(None,x,y).ratio()
            if ratio >= 0.95:
                arrayCompare[key] = arrayCompare[key].str.replace(y,x)

    return arrayCompare


