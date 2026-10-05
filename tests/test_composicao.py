import unittest

from sistema_escolar.escola import Escola


class TestComposicaoEscolaSala(unittest.TestCase):
    def setUp(self):
        self.escola = Escola("Escola Aurora", "12.345.678/0001-90")

    def test_escola_cria_sala_e_e_dona_dela(self):
        sala = self.escola.criar_sala(101, 30)
        self.assertIs(sala.escola, self.escola)
        self.assertEqual(self.escola.listar_salas(), (sala,))

    def test_numero_de_sala_duplicado(self):
        self.escola.criar_sala(101, 30)
        with self.assertRaises(ValueError):
            self.escola.criar_sala(101, 20)

    def test_capacidade_invalida(self):
        with self.assertRaises(ValueError):
            self.escola.criar_sala(102, 0)

    def test_remover_sala_destroi_a_sala(self):
        sala = self.escola.criar_sala(101, 30)
        self.escola.remover_sala(101)
        self.assertFalse(sala.ativa)
        self.assertEqual(self.escola.listar_salas(), ())

    def test_fechar_escola_destroi_todas_as_salas(self):
        s1 = self.escola.criar_sala(101, 30)
        s2 = self.escola.criar_sala(102, 25)
        self.escola.fechar()
        self.assertFalse(s1.ativa)
        self.assertFalse(s2.ativa)
        self.assertEqual(self.escola.listar_salas(), ())
        self.assertFalse(self.escola.aberta)

    def test_escola_fechada_nao_cria_sala(self):
        self.escola.fechar()
        with self.assertRaises(RuntimeError):
            self.escola.criar_sala(101, 30)

    def test_ocupar_e_liberar_sala(self):
        sala = self.escola.criar_sala(101, 30)
        sala.ocupar()
        self.assertFalse(sala.esta_disponivel())
        with self.assertRaises(RuntimeError):
            sala.ocupar()
        sala.liberar()
        self.assertTrue(sala.esta_disponivel())

    def test_sala_inexistente_nao_pode_ser_ocupada(self):
        sala = self.escola.criar_sala(101, 30)
        self.escola.fechar()
        with self.assertRaises(RuntimeError):
            sala.ocupar()

    def test_capacidade_total(self):
        self.escola.criar_sala(101, 30)
        self.escola.criar_sala(102, 25)
        self.assertEqual(self.escola.capacidade_total(), 55)


if __name__ == "__main__":
    unittest.main()