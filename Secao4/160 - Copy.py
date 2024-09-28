import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

NovosProdutos = [
    {"nome": produto.get("nome"), "preco": produto.get("preco") * 1.1}
    for produto in produtos
]
print(*NovosProdutos)

produtos2 = (copy.deepcopy(produtos))
produtos2.sort(key=lambda item: item["nome"])
