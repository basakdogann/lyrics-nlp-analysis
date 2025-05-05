import lyricsgenius

# Buraya kendi Access Token'ını yapıştır
genius = lyricsgenius.Genius("FlXKfVagzqE8tzXnYgshOhlF3QPXkFGjkWS-0t823DQkewU0ZyGZrV8ICj-5Ylll")

# Şarkı arayalım
song = genius.search_song("Kum Gibi", "Ahmet Kaya")

# Şarkı sözlerini yazdıralım
if song:
    print(song.lyrics)
else:
    print("Şarkı bulunamadı.")
