import pandas as pd

# point these to your actual CSVs from each run
base = pd.read_csv("outputs/result_1/mapped_mentions.csv")
simp  = pd.read_csv("outputs/result_2/mapped_mentions.csv")
hg = pd.read_csv("outputs/result_3/mapped_mentions.csv")

def summary(df, name):
    print(f"\n== {name} ==")
    print("rows:", len(df))
    print("by kind:\n", df["matched_kind"].value_counts(dropna=False))
    print("unique terms:", df["matched_qname"].nunique())
    if "hg_score" in df.columns:
        print("mean hg_score:", df["hg_score"].mean())
        print("accept rate (hg):", df["hg_accept"].mean())

summary(base, "Baseline")
summary(hg,   "Hypergraphs")
summary(simp, "Simple Mode")
