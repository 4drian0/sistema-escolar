"""Classe Sala: parte da composição Escola <>-- Sala."""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .escola import Escola


class Sala:
    """Sala de aula.

    Não deve ser instanciada diretamente: quem cria e destrói salas é a
    Escola (método ``Escola.criar_sala``). Sem escola, a sala deixa de existir.
    """

    def __init__(self, numero: int, capacidade: int, escola: Escola) -> None:
        if capacidade <= 0:
            raise ValueError("A capacidade deve ser maior que zero.")
        self.numero = numero
        self.capacidade = capacidade
        self._escola: Optional[Escola] = escola
        self._ocupada = False

    @property
    def escola(self) -> Optional[Escola]:
        return self._escola

    @property
    def ativa(self) -> bool:
        """Uma sala só está ativa enquanto pertence a uma escola."""
        return self._escola is not None

    def ocupar(self) -> None:
        self._exigir_ativa()
        if self._ocupada:
            raise RuntimeError(f"A sala {self.numero} já está ocupada.")
        self._ocupada = True

    def liberar(self) -> None:
        self._exigir_ativa()
        self._ocupada = False

    def esta_disponivel(self) -> bool:
        return self.ativa and not self._ocupada

    def descricao(self) -> str:
        if not self.ativa:
            return f"Sala {self.numero} (inexistente: escola encerrada)"
        return f"Sala {self.numero} (capacidade {self.capacidade}) - {self._escola.nome}"

    def _invalidar(self) -> None:
        """Chamado apenas pela Escola quando a sala é removida ou a escola fecha."""
        self._escola = None
        self._ocupada = False

    def _exigir_ativa(self) -> None:
        if not self.ativa:
            raise RuntimeError("Esta sala não existe mais no sistema.")

    def __str__(self) -> str:
        return self.descricao()