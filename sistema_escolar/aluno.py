"""Classe Aluno: todo da agregação com Endereco."""
from __future__ import annotations

from datetime import date
from typing import Optional

from .endereco import Endereco


class Aluno:
    """Aluno que possui um endereço (agregação).

    O endereço nasce junto com o cadastro (``Aluno.cadastrar``), mas tem ciclo
    de vida próprio: ao remover o aluno, o endereço é devolvido e segue
    existindo para ser repassado a outro contexto.
    """

    def __init__(self, nome: str, matricula: str, data_nascimento: date,
                 endereco: Endereco) -> None:
        self.nome = nome
        self.matricula = matricula
        self.data_nascimento = data_nascimento
        self._endereco: Optional[Endereco] = endereco
        self._ativo = True

    @classmethod
    def cadastrar(cls, nome: str, matricula: str, data_nascimento: date,
                  **dados_endereco: str) -> Aluno:
        """Cadastro de aluno: o endereço é criado junto com ele."""
        return cls(nome, matricula, data_nascimento, Endereco(**dados_endereco))

    @property
    def endereco(self) -> Optional[Endereco]:
        return self._endereco

    @property
    def ativo(self) -> bool:
        return self._ativo

    def mudar_endereco(self, novo: Endereco) -> Optional[Endereco]:
        """Troca o endereço e devolve o antigo, que continua existindo."""
        self._exigir_ativo()
        antigo = self._endereco
        self._endereco = novo
        return antigo

    def remover(self) -> Optional[Endereco]:
        """Remove o aluno e repassa o endereço, que não é destruído."""
        self._exigir_ativo()
        endereco = self._endereco
        self._endereco = None
        self._ativo = False
        return endereco

    def idade(self, hoje: Optional[date] = None) -> int:
        hoje = hoje or date.today()
        anos = hoje.year - self.data_nascimento.year
        if (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day):
            anos -= 1
        return anos

    def dados(self) -> str:
        local = self._endereco.formatar() if self._endereco else "sem endereço"
        return f"{self.nome} (mat. {self.matricula}) - {local}"

    def _exigir_ativo(self) -> None:
        if not self._ativo:
            raise RuntimeError("Este aluno foi removido do sistema.")

    def __str__(self) -> str:
        return self.dados()