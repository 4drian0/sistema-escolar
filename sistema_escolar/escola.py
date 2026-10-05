"""Classe Escola: todo da composição com Sala e lado da associação com Professor."""
from __future__ import annotations

from typing import TYPE_CHECKING

from .sala import Sala

if TYPE_CHECKING:
    from .professor import Professor


class Escola:
    """Escola que cria, possui e destrói suas salas (composição)
    e se relaciona com professores de forma independente (associação)."""

    def __init__(self, nome: str, cnpj: str) -> None:
        self.nome = nome
        self.cnpj = cnpj
        self._salas: list[Sala] = []
        self._professores: list[Professor] = []
        self._aberta = True

    @property
    def aberta(self) -> bool:
        return self._aberta

    # ---- Composição: Escola <>-- Sala ------------------------------------
    def criar_sala(self, numero: int, capacidade: int) -> Sala:
        if not self._aberta:
            raise RuntimeError("Uma escola fechada não pode criar salas.")
        if any(sala.numero == numero for sala in self._salas):
            raise ValueError(f"Já existe a sala {numero} nesta escola.")
        sala = Sala(numero, capacidade, self)
        self._salas.append(sala)
        return sala

    def buscar_sala(self, numero: int) -> Sala:
        for sala in self._salas:
            if sala.numero == numero:
                return sala
        raise LookupError(f"Sala {numero} não encontrada.")

    def remover_sala(self, numero: int) -> None:
        sala = self.buscar_sala(numero)
        self._salas.remove(sala)
        sala._invalidar()

    def listar_salas(self) -> tuple[Sala, ...]:
        return tuple(self._salas)

    def capacidade_total(self) -> int:
        return sum(sala.capacidade for sala in self._salas)

    # ---- Associação: Professor *--* Escola -------------------------------
    def contratar_professor(self, professor: Professor) -> None:
        professor.lecionar_em(self)

    def dispensar_professor(self, professor: Professor) -> None:
        professor.deixar(self)

    def listar_professores(self) -> tuple[Professor, ...]:
        return tuple(self._professores)

    def _registrar_professor(self, professor: Professor) -> None:
        if professor not in self._professores:
            self._professores.append(professor)

    def _remover_professor(self, professor: Professor) -> None:
        if professor in self._professores:
            self._professores.remove(professor)

    # ---- Encerramento ----------------------------------------------------
    def fechar(self) -> None:
        """Salas deixam de existir; professores apenas perdem o vínculo."""
        for sala in self._salas:
            sala._invalidar()
        self._salas.clear()
        for professor in list(self._professores):
            professor.deixar(self)
        self._aberta = False

    def __str__(self) -> str:
        situacao = "aberta" if self._aberta else "fechada"
        return (f"{self.nome} ({situacao}, {len(self._salas)} salas, "
                f"{len(self._professores)} professores)")