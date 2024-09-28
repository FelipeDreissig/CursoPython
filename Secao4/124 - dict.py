
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertou = 0
for i in perguntas:
    while True:
        print(f'Pergunta: {i["Pergunta"]}')
        print("Opções:")
        for chave, j in enumerate(i.get("Opções")):
            print(f'{chave + 1}) {j}')
        try:
            escolha = int(input("Escolha uma opção: "))
            opc = i.get("Opções")[escolha-1]
            if int(opc) == int(i.get("Resposta")):
                print("Acertou", "\U0001F44B")
                acertou += 1
                break
            else:
                print("Errou", "\U0001F44E")
                break
        except Exception:
            print("Opção inválida, tente novamente!", "\U0001F621")
print(f"você acertou {acertou} de {len(perguntas)}!", "\U0001F92F")
