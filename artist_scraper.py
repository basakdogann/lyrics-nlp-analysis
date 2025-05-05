import lyricsgenius
# Access Token'ını buraya yazıyorsun
genius = lyricsgenius.Genius("FlXKfVagzqE8tzXnYgshOhlF3QPXkFGjkWS-0t823DQkewU0ZyGZrV8ICj-5Ylll", timeout=30)

# Sanatçıyı arıyoruz
try:
    artist = genius.search_artist("Tarkan", max_songs=100, sort="title")
except Exception as e:
    print(f"Hata oluştu: {e}")

# Çekilen verileri dosyaya kaydedelim
with open("tarkan_sarkilari.txt", "w", encoding="utf-8") as file:
    for song in artist.songs:
        file.write(f"Şarkı Adı: {song.title}\n")
        file.write(song.lyrics)
        file.write("\n" + "="*50 + "\n\n")

print("Tüm şarkılar kaydedildi!")
