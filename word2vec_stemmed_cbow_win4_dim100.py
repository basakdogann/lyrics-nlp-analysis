import time
from gensim.models import Word2Vec

# Veri dosyasını oku
with open("stemmed_tokenler.txt", "r", encoding="utf-8") as f:
    metin = f.read()

# Cümleleri belgelere böl (örnek: her 1000 kelime bir belge olacak)
kelimeler = metin.split()
belge_uzunlugu = 1000
belgeler = [kelimeler[i:i + belge_uzunlugu] for i in range(0, len(kelimeler), belge_uzunlugu)]

# Modeli eğit
print("Model eğitiliyor...")
start_time = time.time()

model = Word2Vec(
    sentences=belgeler,
    vector_size=100,
    window=4,
    sg=0,  # CBOW
    min_count=1,
    workers=4,
    epochs=10
)

end_time = time.time()
print(f"Model eğitimi tamamlandı. Süre: {round(end_time - start_time, 2)} saniye")

# Modeli kaydet
model.save("word2vec_stemmed_cbow_win4_dim100.model")

# Örnek kelime için en benzer 5 kelimeyi yazdır
kelime = "ask"
if kelime in model.wv:
    print(f"\n'{kelime}' kelimesine en benzer 5 kelime:")
    for benzer, skor in model.wv.most_similar(kelime, topn=5):
        print(f"{benzer} -> {round(skor, 4)}")
else:
    print(f"Kelime '{kelime}' modelde bulunamadı.")
