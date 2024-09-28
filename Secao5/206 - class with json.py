# library
import json

# Class

class Pessoa:
    def __init__(self, nome, sobrenome, idade, altura):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura


if __name__ == "__main__":
    p1 = Pessoa('Felipe', 'Dreissig', 26, 169)
    p2 = Pessoa('Joao', 'Fernandes', 28, 184)
    p3 = Pessoa('Andre', 'Vidotti', 31, 170)
    p4 = Pessoa('Juliana', 'Gameiro', 29, 160)
    
    # List to store Pessoa instances
    pessoas = [p1, p2, p3, p4]
    
    # Create a dictionary with a tag for the list of pessoas
    pessoas_data = {"pessoas": [pessoa.__dict__ for pessoa in pessoas]}
    
    # Convert the dictionary to a JSON string
    json_data = json.dumps(pessoas_data, indent=4)
    
    # Save the JSON string to a file
    with open('206 - pessoas.json', 'w') as json_file:
        json_file.write(json_data)
    

