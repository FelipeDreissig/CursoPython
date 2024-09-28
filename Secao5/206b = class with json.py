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
    # Read the JSON file
    with open('206 - pessoas.json', 'r') as json_file:
        data = json.load(json_file)
    
    # Create Pessoa instances from JSON data
    loaded_pessoas = [Pessoa(**pessoa_dict) for pessoa_dict in data["pessoas"]]
    

    p1 = Pessoa(**vars(loaded_pessoas[0]))
    p2 = Pessoa(**vars(loaded_pessoas[1]))
    p3 = Pessoa(**vars(loaded_pessoas[2]))
    p4 = Pessoa(**vars(loaded_pessoas[3]))
    
