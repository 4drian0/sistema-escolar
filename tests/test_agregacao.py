import unittest
from datetime import date

from sistema_escolar.aluno import Aluno
from sistema_escolar.endereco import Endereco

DADOS = dict(rua="Rua das Flores", numero="120", bairro="Centro",
             cidade="Recife", estado="PE", cep="50000-000")


class TestAgregacaoAlunoEndereco(unittest.TestCase):
    def setUp(self):
        self.aluno = Aluno.cadastrar("João Silva", "2026001", date(2012, 5, 14), **DADOS)

    def test_endereco_e_criado_junto_com_o_aluno(self):
        self.assertIsInstance(self.aluno.endereco, Endereco)
        self.assertEqual(self.aluno.endereco.cidade, "Recife")

    def test_remover_aluno_nao_destroi_o_endereco(self):
        endereco = self.aluno.remover()
        self.assertFalse(self.aluno.ativo)
        self.assertIsNone(self.aluno.endereco)
        self.assertEqual(endereco.rua, "Rua das Flores")

    def test_endereco_pode_ser_repassado_a_outro_contexto(self):
        endereco = self.aluno.remover()
        irmao = Aluno("Pedro Silva", "2026002", date(2014, 3, 2), endereco)
        self.assertIs(irmao.endereco, endereco)

    def test_mudar_endereco_devolve_o_antigo(self):
        antigo = self.aluno.endereco
        novo = Endereco("Av. Brasil", "50", "Boa Vista", "Recife", "PE", "50100-000")
        self.assertIs(self.aluno.mudar_endereco(novo), antigo)
        self.assertIs(self.aluno.endereco, novo)
        self.assertEqual(antigo.numero, "120")

    def test_aluno_removido_nao_pode_ser_alterado(self):
        self.aluno.remover()
        with self.assertRaises(RuntimeError):
            self.aluno.mudar_endereco(Endereco("A", "1", "B", "C", "D", "E"))

    def test_atualizar_campo_inexistente(self):
        with self.assertRaises(AttributeError):
            self.aluno.endereco.atualizar(pais="Brasil")

    def test_atualizar_endereco(self):
        self.aluno.endereco.atualizar(numero="130")
        self.assertIn("130", self.aluno.endereco.formatar())

    def test_idade(self):
        self.assertEqual(self.aluno.idade(date(2026, 5, 13)), 13)
        self.assertEqual(self.aluno.idade(date(2026, 5, 14)), 14)


if __name__ == "__main__":
    unittest.main()