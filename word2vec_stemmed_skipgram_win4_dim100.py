from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
import time

# Başlangıç zamanı
start_time = time.time()

# Veri dosyasını oku
with open("stemmed_tokenler.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Metni satır bazında cümlelere ayır ve tokenize et
sentences = [simple_preprocess(line) for line in text.splitlines() if line.strip()]

# Word2Vec modeli: skip-gram, window=4, vector_size=100
model = Word2Vec(
    sentences,
    vector_size=100,
    window=4,
    sg=1,  # Skip-gram
    min_count=1,
    workers=4
)

# Modeli kaydet
model.save("word2vec_stemmed_skipgram_win4_dim100.model")

# Eğitim süresi
end_time = time.time()
print(f"Model eğitimi tamamlandı. Süre: {round(end_time - start_time, 2)} saniye")

# Örnek benzer kelimeleri yazdır
target_word = "ask"
if target_word in model.wv:
    print(f"\n'{target_word}' kelimesine en benzer 5 kelime:")
    for word, similarity in model.wv.most_similar(target_word, topn=5):
        print(f"{word} -> {round(similarity, 4)}")
else:
    print(f"\n'{target_word}' kelimesi modelde bulunamadı.")
