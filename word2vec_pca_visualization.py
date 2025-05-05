from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 🔁 KULLANILACAK MODELİN DOSYA ADI
model_path = "word2vec_lemmatized_skipgram_win4_dim300.model"

# 🔧 MODELİ YÜKLE
model = Word2Vec.load(model_path)

# 🎯 ÖRNEK KELİME
keyword = "ask"

# ✅ EN BENZER 10 KELİMEYİ AL
similar_words = model.wv.most_similar(keyword, topn=10)
words = [keyword] + [word for word, _ in similar_words]
vectors = [model.wv[word] for word in words]

# 🧠 PCA İLE 2 BOYUTA İNDİR
pca = PCA(n_components=2)
result = pca.fit_transform(vectors)

# 📈 GÖRSELLEŞTİR
plt.figure(figsize=(10, 6))
plt.scatter(result[:, 0], result[:, 1])

for i, word in enumerate(words):
    plt.annotate(word, xy=(result[i, 0], result[i, 1]))

plt.title("Word2Vec PCA Görselleştirme — 'ask' kelimesi çevresindeki benzerler")
plt.xlabel("PCA Bileşeni 1")
plt.ylabel("PCA Bileşeni 2")
plt.grid(True)
plt.tight_layout()

# 💾 DOSYAYA KAYDET
plt.savefig("word2vec_ask_pca.png")
plt.show()
