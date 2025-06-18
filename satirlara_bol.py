# satirlara_bol.py

with open("lemmatize_tokenler.txt", "r", encoding="utf-8") as file:
    metin = file.read()

# Kelimelere ayır
kelimeler = metin.strip().split()

# Her 50 kelime bir satır olacak şekilde böl
satirlar = [" ".join(kelimeler[i:i+50]) for i in range(0, len(kelimeler), 50)]

# Yeni dosyaya yaz
with open("lemmatize_tokenler_duzgun.txt", "w", encoding="utf-8") as file:
    for satir in satirlar:
        file.write(satir + "\n")

print("✅ Dosya 50 kelimelik satırlara bölündü: lemmatize_tokenler_duzgun.txt")
