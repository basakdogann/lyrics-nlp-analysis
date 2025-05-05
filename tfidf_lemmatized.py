import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Dosyayı oku
with open("lemmatize_tokenler.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Cümlelere böl (basit bölme ile)
documents = text.split('\n')  # Her satır bir belge olsun
documents = [doc.strip() for doc in documents if doc.strip() != ""]  # Boşları at

# TF-IDF hesapla
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

# DataFrame'e çevir
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# Dosyaya yaz
df.to_csv("tfidf_lemmatized.csv", index=False)
print("TF-IDF lemmatize işlemi tamamlandı.")
