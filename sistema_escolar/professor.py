"""Classe Professor: lado da associação muitos-para-muitos com Escola."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .escola import Escola


class Professor:
    """Professor que pode lecionar em várias escolas (associação).

    Professor e Escola existem de forma independente: o vínculo entre eles
    pode ser criado e desfeito sem destruir nenhum dos dois objetos.
    """

    def __init__(self, nome: str, cpf: str, disciplina: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.disciplina = disciplina
        self._escolas: list[Escola] = []

    def lecionar_em(self, escola: Escola) -> None:
        """Cria o vínculo nos dois sentidos (Professor <-> Escola)."""
        if not escola.aberta:
            raise RuntimeError("Não é possível lecionar em uma escola fechada.")
        if escola not in self._escolas:
            self._escolas.append(escola)
            escola._registrar_professor(self)

    def deixar(self, escola: Escola) -> None:
        """Desfaz o vínculo nos dois sentidos, sem destruir ninguém."""
        if escola in self._escolas:
            self._escolas.remove(escola)
            escola._remover_professor(self)

    def listar_escolas(self) -> tuple[Escola, ...]:
        return tuple(self._escolas)

    def __str__(self) -> str:
        nomes = ", ".join(escola.nome for escola in self._escolas) or "nenhuma escola"
        return f"Prof. {self.nome} ({self.disciplina}) - leciona em: {nomes}"