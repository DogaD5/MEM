meme_sozlugu = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "ROFL bir şakaya karşılıktır, LOL gibidir"
}

while True:
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

    if word in meme_sozlugu:
        print(meme_sozlugu[word])
    else:
        print("Henüz bu kelimeye sahip değiliz... Ama üzerinde çalışıyoruz!")
