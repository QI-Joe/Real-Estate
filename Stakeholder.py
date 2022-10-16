import pandas as pd
# import gensim
from estnltk import Text

stakepos: list = [r"D:\Study\大三上\Real Estate\Stakeholder\savedrecs.xls"]

def combination(stakepos: list)-> pd.DataFrame:
    stakepos = [*stakepos, *[r"D:\Study\大三上\Real Estate\Stakeholder\savedrecs ({}).xls".format(abst) for abst in range(1, 37)]]
    record: list = []
    for allwork in stakepos:
        record.append(pd.read_excel(allwork))
    allrecord: pd.DataFrame = pd.concat(record)
    return allrecord

def furtherProcess():
    recording = pd.read_csv(r"D:\Study\大三上\Real Estate\Stakeholder\reading.csv")
    recording = recording.Abstract
