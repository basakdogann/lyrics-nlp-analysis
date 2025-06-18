from gensim.models import Word2Vec 
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 1. Modeli yükle
model = Word2Vec.load("word2vec_stemmed_cbow_win2_dim100.model")

# 2. Veri dosyasını oku
with open("stem_tokenler_duzgun.txt", "r", encoding="utf-8") as file:
    corpus = [line.strip().split() for line in file if line.strip()]

# 3. Giriş cümlesi
input_sentence = "kalbim kırık suskunum"
input_tokens = input_sentence.split()

# 4. Ortalama vektör
def get_average_vector(tokens, model):
    vectors = [model.wv[token] for token in tokens if token in model.wv]
    if not vectors:
        return None
    return np.mean(vectors, axis=0)

input_vector = get_average_vector(input_tokens, model)

# 5. Benzerlik hesapla
similarities = []
for i, sentence_tokens in enumerate(corpus):
    vec = get_average_vector(sentence_tokens, model)
    if vec is not None:
        sim = cosine_similarity([input_vector], [vec])[0][0]
        similarities.append((i, sim))

# 6. En benzer 5 cümleyi sırala
top5 = sorted(similarities, key=lambda x: x[1], reverse=True)[:5]

# 7. Yazdır
print("Word2Vec (stemmed_cbow_win2_dim100) için en benzer 5 cümle:\n")
for idx, score in top5:
    print(f"Cümle: {' '.join(corpus[idx])}")
    print(f"Benzerlik Skoru: {score:.4f}\n")
