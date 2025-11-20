import pandas as pd

def clean_csv(df: pd.DataFrame) -> pd.DataFrame:
    # 空白除去
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # 日付を統一（例：YYYY-MM-DD）
    df["date"] = pd.to_datetime(df["date"]).dt.date

    return df