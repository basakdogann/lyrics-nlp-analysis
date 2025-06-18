# w2v_stemmed_cbow_win4_dim100.py

from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 1. Modeli yükle
model = Word2Vec.load("word2vec_stemmed_cbow_win4_dim100.model")

# 2. Veri dosyasını oku
with open("stemmed_tokenler.txt", "r", encoding="utf-8") as file:
    corpus = [line.strip().split() for line in file if line.strip()]

# 3. Giriş cümlesi
input_sentence = "kalp kır sus"
input_tokens = input_sentence.split()

# 4. Giriş token'ları modelde var mı?
print("Giriş cümlesi token'ları:", input_tokens)
print("Modelde bulunan kelimeler:")
for token in input_tokens:
    print(f"{token}: {'✅' if token in model.wv else '❌'}")

# 5. Ortalama vektör hesapla
def get_average_vector(tokens, model):
    vectors = []
    for token in tokens:
        if token in model.wv:
            vectors.append(model.wv[token])
    if not vectors:
        return None
    return np.mean(vectors, axis=0)

input_vector = get_average_vector(input_tokens, model)

# 6. Tüm cümlelerle benzerlik hesapla (ilerleme çıktısı ile)
similarities = []
for i, sentence_tokens in enumerate(corpus):
    if i % 500 == 0:
        print(f"{i}. cümle işleniyor...")
    vec = get_average_vector(sentence_tokens, model)
    if vec is not None and input_vector is not None:
        sim = cosine_similarity([input_vector], [vec])[0][0]
        similarities.append((i, sim))

# 7. En benzer 5 cümleyi sırala
top5 = sorted(similarities, key=lambda x: x[1], reverse=True)[:5]

# 8. Yazdır
print("\nWord2Vec (stemmed_cbow_win4_dim100) için en benzer 5 cümle:\n")
for idx, score in top5:
    print(f"Cümle: {' '.join(corpus[idx])}")
    print(f"Benzerlik Skoru: {score:.4f}\n")
