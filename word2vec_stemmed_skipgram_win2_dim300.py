from gensim.models import Word2Vec
from time import time

# Veri dosyasını oku
with open("stemmed_tokenler.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Kelimeleri cümlelere böl (her 100 kelime = 1 belge)
words = text.split()
documents = [words[i:i+100] for i in range(0, len(words), 100)]

# Modeli eğit
start = time()
model = Word2Vec(
    sentences=documents,
    vector_size=300,
    window=2,
    sg=1,  # Skip-Gram
    min_count=2,
    workers=4
)
model.save("word2vec_stemmed_skipgram_win2_dim300.model")
print(f"Model eğitimi tamamlandı. Süre: {round(time() - start, 2)} saniye")

# Örnek çıktı
try:
    similar_words = model.wv.most_similar("ask", topn=5)
    print("\n'ask' kelimesine en benzer 5 kelime:")
    for word, score in similar_words:
        print(f"{word} -> {round(score, 4)}")
except KeyError:
    print("'ask' kelimesi modelde bulunamadı.")
