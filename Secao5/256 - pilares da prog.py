from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: float = 0) -> None:
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
        self._limite = limite

    @abstractmethod
    def sacar(self, valor: float) -> bool: ...

    def depositar(self, valor: float) -> bool:
        self._saldo += valor
        self.mostra_saldo(f'Depósito realizado com sucesso no valor de R${valor:.2f}.')
        return True

    def mostra_saldo(self, msg: str) -> None:
        print(f'O seu saldo é R${self._saldo:.2f}. {msg}')


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo=0, limite=0) -> None:
        super().__init__(agencia, conta, saldo, limite)

    def sacar(self, valor: float) -> bool:
        saldo_final = self._saldo - valor
        if saldo_final >= - self._limite:
            self._saldo -= valor
            self.mostra_saldo(f'Saque realizado com sucesso no valor de R${valor:.2f}.')
            return True
        self.mostra_saldo(f'Não foi possível realizar o saque no valor de R${valor:.2f} porque o seu saldo final seria de R${saldo_final}. O seu limite extra é de R${self._limite}.')
        return False

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'({self._agencia!r}, {self._conta!r}, {self._saldo!r}, {self._limite!r})'
        return f'{class_name}{attr}'


class ContaPoupanca(Conta):
    def __init__(self, agencia: int, conta: int, saldo=0) -> None:
        super().__init__(agencia, conta, saldo)

    def sacar(self, valor: float) -> bool:
        saldo_final = self._saldo - valor
        if saldo_final >= 0:
            self._saldo -= valor
            self.mostra_saldo(f'Saque realizado com sucesso no valor de R${valor:.2f}.')
            return True
        self.mostra_saldo(f'Não foi possível realizar o saque no valor de R${valor:.2f} porque o seu saldo final seria de R${saldo_final}.')
        return False

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'({self._agencia!r}, {self._conta!r}, {self._saldo!r})'
        return f'{class_name}{attr}'


class Pessoa():
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome) -> None:
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade) -> None:
        self._idade = idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attr}'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, conta: None | Conta = None) -> None:
        super().__init__(nome, idade)
        self.conta = conta


class Banco():
    def __init__(self, agencias: list[int] | None = None, clientes: list[Cliente] | None = None, contas: list[Conta] | None = None) -> None:
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _check_agencia(self, conta: Conta) -> bool:
        if conta._agencia in self.agencias:
            return True
        return False

    def _check_conta(self, conta: Conta) -> bool:
        if conta in self.contas:
            return True
        return False

    def _check_cliente(self, cliente: Cliente) -> bool:
        if cliente in self.clientes:
            return True
        return False

    def _check_cliente_and_conta(self, cliente: Cliente, conta: Conta) -> bool:
        if conta is cliente.conta:
            return True
        return False

    def autenticar(self, cliente: Cliente, conta: Conta) -> bool:
        return self._check_agencia(conta) and self._check_cliente(cliente) and self._check_conta(conta) and self._check_cliente_and_conta(cliente, conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attr}'


if __name__ == '__main__':
    c1 = Cliente('Felipe', 26)
    c1.conta = ContaCorrente(agencia=1, conta=123, limite=100)

    c2 = Cliente('Carlos', 16)
    c2.conta = ContaCorrente(agencia=10, conta=11, limite=300)

    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([c1.conta, c2.conta])
    banco.agencias.extend([i for i in range(1, 11)])
    print(banco)

    if banco.autenticar(c1, c1.conta):
        c1.conta.depositar(1000)
        c1.conta.depositar(10000)
        c1.conta.sacar(10000)
