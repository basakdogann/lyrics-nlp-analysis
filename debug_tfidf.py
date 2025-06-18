import pandas as pd

# TF-IDF CSV dosyasını oku
df_lem = pd.read_csv("tfidf_lemmatized.csv", index_col=0)

# Index’teki ilk 10 değeri yazdır
print("\n📌 İlk 10 index değeri:")
print(df_lem.index[:10])

# Boş olan varsa göster
print("\n📌 Boş index (cümle) sayısı:")
print(df_lem.index[df_lem.index.isna()].shape[0])

# Dataframe’in genel bilgisi
print("\n📌 DataFrame info:")
print(df_lem.info())
