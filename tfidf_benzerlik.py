import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Dosyayı oku
with open("lemmatize_tokenler_duzgun.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    sentences = [line.strip() for line in lines if line.strip() != ""]

# 2. Giriş cümlesini ekle
input_sentence = "kalbim kırık suskunum"
sentences_with_input = [input_sentence] + sentences

# 3. TF-IDF Vektörleme
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(sentences_with_input)

# 4. Cosine Similarity Hesapla
cos_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])[0]

# 5. En benzer 5 cümleyi bul
top_5_indices = cos_sim.argsort()[-5:][::-1]
top_5_scores = cos_sim[top_5_indices]
top_5_sentences = [sentences[i] for i in top_5_indices]

# 6. Sonuçları yazdır
for i in range(5):
    print(f"{i+1}. Cümle: {top_5_sentences[i]}")
    print(f"   Benzerlik Skoru: {top_5_scores[i]:.4f}\n")
