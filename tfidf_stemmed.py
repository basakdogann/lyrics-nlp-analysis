import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# 1. Dosyayı oku
with open("stemmed_tokenler.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 2. Cümlelere böl (basit satır bazlı bölme)
documents = text.split('\n')  # Her satırı belge olarak al
documents = [doc.strip() for doc in documents if doc.strip() != ""]  # Boş satırları çıkar

# 3. TF-IDF vektörleştirme işlemi
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

# 4. Sonucu pandas DataFrame'e çevir
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# 5. CSV dosyasına yaz
df.to_csv("tfidf_stemmed.csv", index=False)
print("TF-IDF stemmed işlemi başarıyla tamamlandı ve tfidf_stemmed.csv dosyasına kaydedildi.")
