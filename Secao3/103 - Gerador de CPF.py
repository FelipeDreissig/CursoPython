import os
import re
os.system('cls')


def DigitoCPF(CPF, FatorInicial):
    Fator = FatorInicial
    soma = 0
    for value in range(FatorInicial-1):
        soma += (int(CPF[value]) * Fator)
        Fator -= 1
    soma = (soma * 10) % 11
    digito = 0 if soma > 9 else soma
    return digito


while True:
    try:
        Imput_cpf = input("Digite um CPF: ")
        cpf = re.sub(r'[^0-9]', "", Imput_cpf)
    except Exception:
        print("Digite um CPF Válido.")
        continue
    FistDigit = DigitoCPF(CPF=cpf, FatorInicial=10)
    SecondDigit = DigitoCPF(CPF=cpf, FatorInicial=11)
    if cpf[len(cpf)-2:len(cpf)] == str(FistDigit) + str(SecondDigit):
        print("CPF é Válido.")
    else:
        print("CPF é inválido.")

