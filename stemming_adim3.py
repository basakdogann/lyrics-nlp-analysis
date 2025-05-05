from trnlp import TrnlpWord

# Dosyayı oku
with open("lemmatize_tokenler.txt", "r", encoding="utf-8") as file:
    kelimeler = file.read().split()

stems = []

for i, kelime in enumerate(kelimeler):
    kelime_nesne = TrnlpWord()
    kelime_nesne.setword(kelime)

    try:
        stem = kelime_nesne.get_stem if isinstance(kelime_nesne.get_stem, str) else kelime
    except:
        stem = kelime

    stems.append(stem)

    if i < 30:
        print(f"{kelime} -> {stem}")

# Dosyaya yaz
with open("stemmed_tokenler.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(stems))
