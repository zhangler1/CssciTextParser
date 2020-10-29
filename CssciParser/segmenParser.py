import re
import os
import pandas as pd
from CssciParser.parserPaper import parserPaper
def segmenParser(DataDir,outDir):
    for dirpath, dirnames, filenames in os.walk(DataDir):
        for file in filenames:
            filepath=os.path.join(dirpath,file
            )
            paperInfor=pd.DataFrame(columns=["作者","第一机构","关键词"])
            with open(filepath, "r", encoding="utf-8-sig") as f:
                sourceRawText = f.readlines()
            start=0
            end=0
            for i,line in enumerate(sourceRawText):
                if re.match(r"【来源篇名】",line):
                    start=i
                if re.match(r"-----------------------------------------------------------------------",line):
                    end=i
                    paper=parserPaper(sourceRawText[start:end])
                    paperInfor=paperInfor.append(paper,ignore_index=True)

            paperInfor.to_excel(os.path.join(outDir,file.replace(".txt",".xlsx")))








