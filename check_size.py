import os

size = os.path.getsize("turkce_sarki_corpus.txt") / (1024*1024)  # MB cinsinden
print(f"Veri seti boyutu: {size:.2f} MB")
