import time
from gensim.models import Word2Vec

# 1. Lemmatize edilmiş veriyi oku
with open("lemmatize_tokenler.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 2. Cümle formatına getir (basitçe boşlukla ayır, tek cümle gibi)
sentences = [text.split()]

# 3. Model eğitimi başlat
print("Model eğitiliyor...")
start = time.time()

model = Word2Vec(
    sentences,
    vector_size=300,
    window=2,
    sg=0,  # CBOW
    min_count=1,
    workers=4
)

end = time.time()
print(f"Model eğitimi tamamlandı. Süre: {round(end - start, 2)} saniye")

# 4. Modeli kaydet
model.save("word2vec_lemmatized_cbow_win2_dim300.model")

# 5. Örnek çıktı
kelime = "ask"
if kelime in model.wv:
    print(f"\n'{kelime}' kelimesine en benzer 5 kelime:")
    for benzer, skor in model.wv.most_similar(kelime, topn=5):
        print(f"{benzer} -> {round(skor, 4)}")
else:
    print(f"Kelime bulunamadı: {kelime}")
