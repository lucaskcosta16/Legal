print('Bem-Vindo ao dicion[ario da internet!!!')
meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            'VC': "Abreviacao da palavra voce",
            'HATER': "Pessoa que esta constantemente criticando os outros",
            'BISCOTAR': "Postar algo apenas para chamar atencao",
            }

word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Eu nao sei o que essa palavra significa")
