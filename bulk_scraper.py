import lyricsgenius
import os
import glob

genius = lyricsgenius.Genius("FlXKfVagzqE8tzXnYgshOhlF3QPXkFGjkWS-0t823DQkewU0ZyGZrV8ICj-5Ylll", timeout=30)

# Yeni sanatçı listesi
sanatcilar = [
    "Zeynep Bastık", "Tuğçe Kandemir", "Melis Fis", "İkilem", "Dedublüman", "Mert Demir",
    "Canozan", "Sufle", "Adamlar", "Büyük Ev Ablukada", "Kalben", "No Land", "Perdenin Ardındakiler",
    "Nilipek", "Jabbar", "Yüzyüzeyken Konuşuruz", "Pamela", "Deniz Tekin", "Mavi Gri", "Nova Norda",
    "Pera", "Evdeki Saat", "Cem Adrian", "Can Bonomo", "Eypio", "Norm Ender", "Ayben", "Allame",
    "Kamufle", "Tankurt Manas", "Lil Zey", "Patron", "Ben Fero", "Murda", "Khontkar", "Gazapizm",
    "Uzi", "Motif", "Reckol", "Sefo", "Çağan Şengül", "Sena Şener", "Dolu Kadehi Ters Tut", "Pinhani",
    "Cihan Mürtezaoğlu", "The Away Days", "Palmiyeler", "Yaşlı Amca", "Sena Gül", "Melike Şahin",
    "Can Kazaz", "Berkay Altunyay", "Soft Analog", "Batu Akdeniz", "Batuhan Kordel", "Cem Pilevneli",
    "Suat Ateşdağlı", "Canbay & Wolker", "Arda Kemirgent", "Ufuk Beydemir"
]

# Burada dikkat: "a" modunda açıyoruz (append)
for sanatci in sanatcilar:
    try:
        print(f"{sanatci} için veri çekiliyor...")
        artist = genius.search_artist(sanatci, max_songs=100, sort="title")
        
        with open("turkce_sarki_corpus.txt", "a", encoding="utf-8") as file:
            for song in artist.songs:
                file.write(f"Şarkı Adı: {song.title}\n")
                file.write(song.lyrics)
                file.write("\n" + "="*50 + "\n\n")
        print(f"{sanatci} şarkıları eklenerek kaydedildi!")
    except Exception as e:
        print(f"{sanatci} için hata oluştu: {e}")

print("BÜTÜN YENİ ŞARKILAR TURKCE_SARKI_CORPUS ÜZERİNE EKLENDİ!")
