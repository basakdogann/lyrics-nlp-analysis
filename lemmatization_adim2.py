from trnlp import TrnlpWord

# Temizlenmiş tokenları oku
with open("temizlenmis_tokenler.txt", "r", encoding="utf-8") as file:
    kelimeler = file.read().split()

print(f"Toplam kelime sayısı: {len(kelimeler)}")  # ⬅️ kontrol için ekle

lemmalar = []
for kelime in kelimeler:
    kelime_nesne = TrnlpWord()
    kelime_nesne.setword(kelime)
    if kelime_nesne.get_stem:
        lemmalar.append(kelime_nesne.get_stem)
    else:
        lemmalar.append(kelime)

# Örnek çıktı
print("Örnek Lemmatize edilmiş kelimeler:", lemmalar[:30])

# Sonuçları kaydet
with open("lemmatize_tokenler.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(lemmalar))
