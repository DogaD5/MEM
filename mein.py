meme_sozlugu = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "ROFL bir şakaya karşılıktır, LOL gibidir",
    "AFK": "Klavyeden uzak, hareketsiz oyuncu",
    "GG": "İyi oyun anlamına gelir, genellikle oyun sonunda söylenir",
    "OP": "Aşırı güçlü bir karakter ya da eşya",
    "NERF": "Bir karakterin veya eşyanın gücünün azaltılması",
    "BUFF": "Bir karakterin veya eşyanın gücünün artırılması",
    "META": "Oyunda en etkili strateji veya karakterlerin genel durumu",
    "TRYHARD": "Oyunu aşırı ciddiye alan ve çok çabalayan oyuncu",
    "SUS": "Şüpheli anlamında kullanılır, Among Us oyunundan yayılmıştır",
    "MALD": "Çok sinirlenen kişiler için kullanılan bir kelime",
    "RATIO": "Sosyal medyada, bir paylaşımın cevabının daha fazla beğeni alması",
    "L + RATIO": "Birinin paylaşımına 'Kaybettin' veya 'Kötü durumdasın' anlamında yazılır",
    "BASED": "Kendi fikirlerini korkmadan savunan insanlar için kullanılan terim",
    "COPIUM": "Yenilgiyi kabul edemeyenler için alaycı bir şekilde kullanılan terim",
    "SIGMA": "Bağımsız ve güçlü kişilikleri tanımlamak için kullanılan bir terim",
    "NPC": "Sıradan hareket eden veya kendi fikirleri olmayan kişiler için alaycı bir terim"
}

while True:
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    
    if word in meme_sozlugu:
        print(meme_sozlugu[word])
    else:
        print("Henüz bu kelimeye sahip değiliz... Ama üzerinde çalışıyoruz!")
