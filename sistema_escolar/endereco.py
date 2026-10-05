"""Classe Endereco: parte da agregação Aluno <>-- Endereco."""
from __future__ import annotations


class Endereco:
    """Endereço postal.

    Não conhece o Aluno. Por isso pode continuar existindo (e ser reutilizado
    em relatórios ou por outro contexto) depois que o aluno é removido.
    """

    _CAMPOS = ("rua", "numero", "bairro", "cidade", "estado", "cep")

    def __init__(self, rua: str, numero: str, bairro: str,
                 cidade: str, estado: str, cep: str) -> None:
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def formatar(self) -> str:
        return (f"{self.rua}, {self.numero} - {self.bairro}, "
                f"{self.cidade}/{self.estado} - CEP {self.cep}")

    def atualizar(self, **campos: str) -> None:
        for nome, valor in campos.items():
            if nome not in self._CAMPOS:
                raise AttributeError(f"Campo de endereço inexistente: {nome}")
            setattr(self, nome, valor)

    def __str__(self) -> str:
        return self.formatar()