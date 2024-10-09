meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "GG": "Good Game",
            "FF": "Surrender",
            }
word = input("Введите непонятное слово (большими буквами!): ")
while  True:
    if word in meme_dict.keys():
        print(meme_dict[word])    
    else:
        print("not found")
    break
