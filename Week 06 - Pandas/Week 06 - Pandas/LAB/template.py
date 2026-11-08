"""
RECORD CHECK  -  my version
===========================

Name  : Matthias Munyao
Lane  :  IT      
Date  : 08/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("records.csv")




df["percent"] = (df["value"] / df["limit"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)



print(df)


print(df[df["status"] != "OK"])

counts = df.groupby("status").size()
print(counts)

df.to_csv("records_report.csv", index=False)

counts.plot(kind="bar", title="Records by status")
plt.tight_layout()
plt.show()
