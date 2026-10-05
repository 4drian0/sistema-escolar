"""Demonstração dos três tipos de relacionamento do micro cenário escolar."""
import sys
from datetime import date

from sistema_escolar.aluno import Aluno
from sistema_escolar.escola import Escola
from sistema_escolar.professor import Professor

# Garante UTF-8 no terminal (evita "�" no Windows / Code Runner)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def titulo(texto: str) -> None:
    print(f"\n=== {texto} ===")


def demo_composicao() -> None:
    titulo("COMPOSIÇÃO: Escola e Sala")
    escola = Escola("Escola Municipal Aurora", "12.345.678/0001-90")
    sala = escola.criar_sala(101, 30)
    escola.criar_sala(102, 25)
    print(escola)
    for s in escola.listar_salas():
        print(" -", s)
    escola.fechar()
    print("Depois de fechar a escola:")
    print(" -", sala)
    print(" - salas cadastradas:", len(escola.listar_salas()))


def demo_associacao() -> None:
    titulo("ASSOCIAÇÃO: Professor e Escola")
    aurora = Escola("Escola Municipal Aurora", "12.345.678/0001-90")
    horizonte = Escola("Colégio Horizonte", "98.765.432/0001-10")
    marina = Professor("Marina Costa", "123.456.789-00", "Matemática")
    paulo = Professor("Paulo Reis", "987.654.321-00", "História")

    marina.lecionar_em(aurora)
    marina.lecionar_em(horizonte)
    aurora.contratar_professor(paulo)
    print(marina)
    print(paulo)
    print(aurora)

    aurora.fechar()
    print("Depois de fechar a Escola Aurora, os professores continuam existindo:")
    print(marina)
    print(paulo)


def demo_agregacao() -> None:
    titulo("AGREGAÇÃO: Aluno e Endereço")
    aluno = Aluno.cadastrar(
        "João Silva", "2026001", date(2012, 5, 14),
        rua="Rua das Flores", numero="120", bairro="Centro",
        cidade="Recife", estado="PE", cep="50000-000",
    )
    print(aluno)
    endereco = aluno.remover()
    print("Aluno removido. Ativo?", aluno.ativo)
    print("Endereço continua existindo (relatório):", endereco)

    irmao = Aluno("Pedro Silva", "2026002", date(2014, 3, 2), endereco)
    print("Endereço repassado a outro contexto:", irmao)


if __name__ == "__main__":
    demo_composicao()
    demo_associacao()
    demo_agregacao()