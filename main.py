import random
response = ["Нутром чую, что да", "Вполне возможно", "Не знаю", "Нет","Врят-ли"]
question = ["Чо нада?","Аюшки"]
ball = ["@", "#", "%"]
game = True
while game is True:
    a = random.randint(0,4)
    b = random.randint(0,1)
    c = random.randint(0,2)
    print(f"=(\_|{ball[c]}|_/)")
    print(question[b])
    quest = input()
    print("Ответ ШАМАНА")
    if quest=="выход":
        game = False
    print(response[a])
    print("========================")
    print("=+=+=+=+=+=+=+=+=+=+=+=+")
