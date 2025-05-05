from gensim.models import Word2Vec
import time

# 1. Veriyi oku
with open("lemmatize_tokenler.txt", "r", encoding="utf-8") as f:
    tokens = f.read().split()

# 2. Cümle benzeri yapıya dönüştür (gerekirse 100 kelimelik parçalar)
sentences = [tokens[i:i+100] for i in range(0, len(tokens), 100)]

# 3. Model parametreleri
window = 4
vector_size = 100
sg = 0  # CBOW

# 4. Eğitimi başlat
print("Model eğitiliyor...")
start = time.time()
model = Word2Vec(sentences=sentences, vector_size=vector_size, window=window, sg=sg, min_count=1)
end = time.time()
print(f"Model eğitimi tamamlandı. Süre: {round(end - start, 2)} saniye")

# 5. Modeli kaydet
model.save("word2vec_lemmatized_cbow_win4_dim100.model")

# 6. Örnek kelime için en benzer kelimeleri göster
print("\n'ask' kelimesine en benzer 5 kelime:")
for word, score in model.wv.most_similar("ask", topn=5):
    print(f"{word} -> {round(score, 4)}")
