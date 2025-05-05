import time
from gensim.models import Word2Vec

# 1. Veriyi oku
with open("lemmatize_tokenler.txt", "r", encoding="utf-8") as f:
    tokens = f.read().split()

# 2. Veriyi cümlelere böl (Word2Vec için gereklidir)
sentences = [tokens[i:i+100] for i in range(0, len(tokens), 100)]

# 3. Modeli eğit
print("Model eğitiliyor...")
start_time = time.time()

model = Word2Vec(
    sentences,
    vector_size=100,
    window=4,
    sg=1,  # sg=1 → Skip-gram
    min_count=1,
    workers=4
)

training_time = round(time.time() - start_time, 2)
print(f"Model eğitimi tamamlandı. Süre: {training_time} saniye")

# 4. Modeli kaydet
model.save("word2vec_lemmatized_skipgram_win4_dim100.model")

# 5. Örnek kelime: 'ask'
try:
    print("\n'ask' kelimesine en benzer 5 kelime:")
    for word, score in model.wv.most_similar("ask", topn=5):
        print(f"{word} -> {round(score, 4)}")
except KeyError:
    print("'ask' kelimesi modelde bulunamadı.")
