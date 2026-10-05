import unittest

from sistema_escolar.escola import Escola
from sistema_escolar.professor import Professor


class TestAssociacaoProfessorEscola(unittest.TestCase):
    def setUp(self):
        self.e1 = Escola("Escola Aurora", "12.345.678/0001-90")
        self.e2 = Escola("Colégio Horizonte", "98.765.432/0001-10")
        self.prof = Professor("Marina Costa", "123.456.789-00", "Matemática")

    def test_vinculo_e_bidirecional(self):
        self.prof.lecionar_em(self.e1)
        self.assertIn(self.e1, self.prof.listar_escolas())
        self.assertIn(self.prof, self.e1.listar_professores())

    def test_professor_leciona_em_varias_escolas(self):
        self.prof.lecionar_em(self.e1)
        self.prof.lecionar_em(self.e2)
        self.assertEqual(len(self.prof.listar_escolas()), 2)

    def test_escola_tem_varios_professores(self):
        outro = Professor("Paulo Reis", "987.654.321-00", "História")
        self.e1.contratar_professor(self.prof)
        self.e1.contratar_professor(outro)
        self.assertEqual(len(self.e1.listar_professores()), 2)

    def test_vinculo_duplicado_nao_repete(self):
        self.prof.lecionar_em(self.e1)
        self.prof.lecionar_em(self.e1)
        self.assertEqual(len(self.e1.listar_professores()), 1)

    def test_deixar_escola_desfaz_vinculo_sem_destruir(self):
        self.prof.lecionar_em(self.e1)
        self.prof.deixar(self.e1)
        self.assertEqual(self.prof.listar_escolas(), ())
        self.assertEqual(self.e1.listar_professores(), ())
        self.assertTrue(self.e1.aberta)

    def test_fechar_escola_nao_destroi_professor(self):
        self.prof.lecionar_em(self.e1)
        self.prof.lecionar_em(self.e2)
        self.e1.fechar()
        self.assertEqual(self.prof.listar_escolas(), (self.e2,))
        self.assertEqual(self.prof.nome, "Marina Costa")

    def test_nao_leciona_em_escola_fechada(self):
        self.e1.fechar()
        with self.assertRaises(RuntimeError):
            self.prof.lecionar_em(self.e1)


if __name__ == "__main__":
    unittest.main()