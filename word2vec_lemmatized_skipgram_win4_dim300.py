from gensim.models import Word2Vec
import time

# Dosyayı oku ve cümle listesi oluştur
with open("lemmatize_tokenler.txt", "r", encoding="utf-8") as f:
    kelimeler = f.read().split()

# Her kelimeyi tek kelimelik cümle gibi al (şarkı sözleri olduğu için)
sentences = [[kelime] for kelime in kelimeler]

# Model eğitimi
print("Model eğitiliyor...")
start = time.time()

model = Word2Vec(
    sentences,
    vector_size=300,
    window=4,
    sg=1,  # Skip-gram
    min_count=1,
    workers=4
)

end = time.time()
print(f"Model eğitimi tamamlandı. Süre: {round(end - start, 2)} saniye")

# Modeli kaydet
model.save("word2vec_lemmatized_skipgram_win4_dim300.model")

# 'ask' kelimesine en benzer 5 kelimeyi yazdır
try:
    print("\n'ask' kelimesine en benzer 5 kelime:")
    for word, score in model.wv.most_similar("ask", topn=5):
        print(f"{word} -> {round(score, 4)}")
except KeyError:
    print("'ask' kelimesi modelde bulunamadı.")
