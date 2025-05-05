from gensim.models import Word2Vec
import time

# 1. Veriyi oku
with open("lemmatize_tokenler.txt", "r", encoding="utf-8") as file:
    tokens = file.read().split()

# 2. Veriyi cümle gibi grupla (her 100 kelime bir cümle gibi)
window_size = 2
vector_size = 100
sentences = [tokens[i:i+100] for i in range(0, len(tokens), 100)]

# 3. Modeli eğit
print("Model eğitiliyor...")
start = time.time()
model = Word2Vec(sentences, window=window_size, vector_size=vector_size, sg=0)
end = time.time()
print(f"Model eğitimi tamamlandı. Süre: {end - start:.2f} saniye")

# 4. Modeli kaydet
model.save("word2vec_lemmatized_cbow_win2_dim100.model")

# 5. Örnek benzer kelimeleri yazdır
print("\n'ask' kelimesine en benzer 5 kelime:")
try:
    for word, score in model.wv.most_similar("ask", topn=5):
        print(f"{word} -> {score:.4f}")
except KeyError:
    print("Kelime veri setinde bulunamadı.")
