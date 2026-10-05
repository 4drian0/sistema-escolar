"""Classe Escola: todo da composição com Sala."""
from __future__ import annotations

from .sala import Sala


class Escola:
    """Escola que cria, possui e destrói suas salas (composição)."""

    def __init__(self, nome: str, cnpj: str) -> None:
        self.nome = nome
        self.cnpj = cnpj
        self._salas: list[Sala] = []
        self._aberta = True

    @property
    def aberta(self) -> bool:
        return self._aberta

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

    def fechar(self) -> None:
        """Ao fechar, todas as salas deixam de existir no sistema."""
        for sala in self._salas:
            sala._invalidar()
        self._salas.clear()
        self._aberta = False

    def __str__(self) -> str:
        situacao = "aberta" if self._aberta else "fechada"
        return f"{self.nome} ({situacao}, {len(self._salas)} salas)"