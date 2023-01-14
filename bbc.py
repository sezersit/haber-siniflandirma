import os, re, glob
import pandas as pd

file = ["business", "entertainment", "politics", "sport", "tech"]

alltext = []
alltitle = []
allfilename = []
allcategory = []

for k in file:
    print(k)

    filenames = sorted(glob.glob(
        "./bbc/" + k + "/*.txt"))
    N = len(filenames)
    print(N)

    filenames = filenames[:N]
    for f in filenames:
        f_id = re.findall("\d+", f)[0] + ".txt"

        df = pd.read_table(f, header=None, index_col=False)
        title = df.iloc[0][0]

        df = df.iloc[1:, :]
        text = []
        for i in range(len(df)):
            text.append(df.iloc[i][0])

        alltext.append(str(text)[1:])
        alltitle.append(str(title))
        allfilename.append(f_id)
        allcategory.append(k)

alldata = pd.DataFrame.from_dict({"filename": allfilename, "title": alltitle, "text": alltext, "category": allcategory})
alldata.to_csv("./bbc_news_all_category.txt", sep=" ", index=False)
