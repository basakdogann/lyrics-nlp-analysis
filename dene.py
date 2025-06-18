import pandas as pd

# 1. CSV dosyasını yükle
df = pd.read_csv("stemmed_tokenler.csv")

# 2. 'tokens' sütunundaki verileri temizle
df['tokens'] = df['tokens'].astype(str).str.strip()

# 3. Her satırı bir cümle olarak .txt dosyasına yaz
df['tokens'].to_csv("stemmed_tokenler.txt", index=False, header=False)
