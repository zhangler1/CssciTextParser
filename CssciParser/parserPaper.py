import re
import  pandas as pd
def parserPaper(textlines)->pd.Series:
    au=""
    journal=""
    keyword=""
    for line in textlines:
        if re.match(r"【来源作者】(.+)",line):
            au=re.match(r"【来源作者】(.+)",line).group(1)
        if re.match(r"【第一机构】(.+)",line):
            journal=re.match(r"【第一机构】(.+)",line).group(1)
        if re.match(r"【关 键 词】(.+)",line):
            keyword=re.match(r"【关 键 词】(.+)",line).group(1)

    return pd.Series([au,journal,keyword],index=["作者","第一机构","关键词"])
if __name__ == '__main__':
    
    print(parserPaper(["【来源篇名】基于关键词演进的我国科技评价学科发展研究" ,
"【英文篇名】The Development of Evaluation on Science and Technology: A Theory Tree based on Keyword Evolution" ,
"【来源作者】李强/赵一方/黄岑",
"【基    金】国家自然科学基金面上项目(71373253)/创新方法工作专项项目(2013IM010100) ",
"【期    刊】科学学与科学技术管理",
"【第一机构】中国科学院科技战略咨询研究院",
"【机构名称】[李强]中国科学院科技战略咨询研究院./[赵一方]《中国学术期刊(光盘版)》电子杂志社./[黄岑]《中国学术期刊(光盘版)》电子杂志社. ",
"【第一作者】李强",
"【中图类号】G306.0" ,
"【年代卷期】2019,40(010):3-19 ",
"【关 键 词】科技评价/关键词/共词分析/学科树" ,
"【基金类别】"]))