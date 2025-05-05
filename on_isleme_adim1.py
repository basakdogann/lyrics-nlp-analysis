import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string


nltk.download("punkt")
nltk.download("stopwords")

# 1. Dosyayı oku
with open("turkce_sarki_corpus.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 2. Küçük harfe çevir
text = text.lower()

# 3. Noktalama işaretlerini temizle
text = text.translate(str.maketrans("", "", string.punctuation))

# 4. Kelimelere ayır (tokenization)
tokens = word_tokenize(text, preserve_line=True)

# 5. Türkçe stopwords listesini al
stop_words = set(stopwords.words("turkish"))

# 6. Stopword olmayan kelimeleri filtrele
filtered_tokens = [word for word in tokens if word not in stop_words and word.isalpha()]

# 7. Örnek çıktı göster
print("Örnek Tokenler (Stopword temizlenmiş):")
print(filtered_tokens[:30])  # İlk 30 kelime

# 8. Temizlenmiş tokenları dosyaya yaz
with open("temizlenmis_tokenler.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(filtered_tokens))
