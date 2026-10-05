# Diagrama de classes UML

Notação: linha simples = associação, losango vazado = agregação,
losango preenchido = composição.

```mermaid
classDiagram
    direction LR

    class Escola {
        -str nome
        -str cnpj
        -bool aberta
        +criar_sala(numero, capacidade) Sala
        +buscar_sala(numero) Sala
        +remover_sala(numero)
        +listar_salas() tuple
        +capacidade_total() int
        +contratar_professor(professor)
        +dispensar_professor(professor)
        +listar_professores() tuple
        +fechar()
    }

    class Sala {
        -int numero
        -int capacidade
        -bool ocupada
        +ocupar()
        +liberar()
        +esta_disponivel() bool
        +descricao() str
    }

    class Professor {
        -str nome
        -str cpf
        -str disciplina
        +lecionar_em(escola)
        +deixar(escola)
        +listar_escolas() tuple
    }

    class Aluno {
        -str nome
        -str matricula
        -date data_nascimento
        -bool ativo
        +cadastrar() Aluno
        +mudar_endereco(novo) Endereco
        +remover() Endereco
        +idade() int
        +dados() str
    }

    class Endereco {
        -str rua
        -str numero
        -str bairro
        -str cidade
        -str estado
        -str cep
        +formatar() str
        +atualizar(campos)
    }

    Escola "1" *-- "0..*" Sala : possui (composição)
    Professor "0..*" -- "0..*" Escola : leciona em (associação)
    Aluno "1" o-- "1" Endereco : mora em (agregação)
```

O diagrama aparece renderizado direto no GitHub. Para exportar como imagem,
cole o código em https://mermaid.live.