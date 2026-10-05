# Sistema Escolar — Trabalho Prático 01

Disciplina: Arquitetura de Software — ADS, Bloco IV (2026.2)

Micro cenário de gerenciamento escolar que demonstra os três tipos de
relacionamento da UML:

| Relação            | Tipo       |
|--------------------|------------|
| Escola — Sala      | Composição |
| Professor — Escola | Associação |
| Aluno — Endereço   | Agregação  |

## Como executar (Python 3.9+)

```bash
python main.py                  # demonstração
python -m unittest discover -v  # testes
```

## Estrutura

```
sistema_escolar/   # classes do domínio
tests/             # testes unitários
docs/              # análise e diagrama UML
main.py            # demonstração
```

## Convenção de branches

- `feature/*` — novas funcionalidades
- `docs/*` — documentação

Cada branch é integrada à `main` com `git merge --no-ff`.