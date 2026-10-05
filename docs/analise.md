# Análise do cenário escolar

## 1. Entidades, atributos e métodos

| Classe    | Atributos                                              | Métodos                                                                                                          |
|-----------|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Escola    | nome, cnpj, salas, professores, aberta                 | criar_sala, buscar_sala, remover_sala, listar_salas, capacidade_total, contratar_professor, dispensar_professor, listar_professores, fechar |
| Sala      | numero, capacidade, escola, ocupada                    | ocupar, liberar, esta_disponivel, descricao                                                                      |
| Professor | nome, cpf, disciplina, escolas                         | lecionar_em, deixar, listar_escolas                                                                              |
| Aluno     | nome, matricula, data_nascimento, endereco, ativo      | cadastrar, mudar_endereco, remover, idade, dados                                                                 |
| Endereco  | rua, numero, bairro, cidade, estado, cep               | formatar, atualizar                                                                                              |

## 2. Classificação dos relacionamentos

| Relação            | Tipo       | Cardinalidade | Ciclo de vida                          | "Todo" exclusivo?     | Existe sozinho? |
|--------------------|------------|---------------|----------------------------------------|-----------------------|-----------------|
| Escola — Sala      | Composição | 1 — 0..*      | A sala morre com a escola              | Sim (uma escola só)   | Não             |
| Professor — Escola | Associação | 0..* — 0..*   | Independentes um do outro              | Não                   | Sim, ambos      |
| Aluno — Endereço   | Agregação  | 1 — 1         | Nasce com o aluno, sobrevive a ele     | Não é obrigatório     | Sim (após remoção) |

### Escola — Sala: composição
A sala só faz sentido dentro de uma escola. Ela é criada pela escola, pertence
a uma única escola e, se a escola fecha, as salas deixam de existir no sistema.
Há dependência total de ciclo de vida e exclusividade do "todo", que são as
marcas da composição (losango preenchido).

### Professor — Escola: associação
Um professor pode lecionar em várias escolas e uma escola pode ter vários
professores. A existência de um não depende da existência do outro, e nenhum
dos dois é "parte" do outro: é apenas um vínculo entre objetos independentes
(relação muitos-para-muitos). Por isso é uma associação simples. Se uma escola
fecha, o professor apenas perde o vínculo e continua existindo.

### Aluno — Endereço: agregação
O endereço é criado junto com o cadastro do aluno e pertence a ele, o que
caracteriza uma relação todo-parte. Porém, se o aluno for removido, o endereço
pode continuar fazendo sentido isoladamente (por exemplo, em relatórios) e ser
repassado a outro contexto. Como a parte tem ciclo de vida independente do
todo, a relação é agregação (losango vazado) e não composição.