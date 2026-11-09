import unittest
from lista_hibrida import ListaHibrida

class TestListaHibrida(unittest.TestCase):

    def setUp(self):
        self.lh = ListaHibrida(seed=42, tamanho_inicial=1024)

    def test_01_inicializacao_reprodutivel(self):
        self.assertEqual(len(self.lh.regiao_ordenada), 1024)
        self.assertEqual(len(self.lh.cauda), 0)
        self.assertEqual(self.lh.regiao_ordenada, sorted(self.lh.regiao_ordenada))
        outra_lh = ListaHibrida(seed=42, tamanho_inicial=1024)
        self.assertEqual(self.lh.regiao_ordenada, outra_lh.regiao_ordenada)

    def test_02_insercao_e_rejeicao_duplicados(self):
        chave_nova = 999999
        sucesso, msg = self.lh.inserir(chave_nova)
        self.assertTrue(sucesso)
        self.assertIn(chave_nova, self.lh.cauda)

        sucesso_dup, msg_dup = self.lh.inserir(chave_nova)
        self.assertFalse(sucesso_dup)
        self.assertIn("duplicada", msg_dup.lower())

        chave_existente = self.lh.regiao_ordenada[0]
        sucesso_existente, _ = self.lh.inserir(chave_existente)
        self.assertFalse(sucesso_existente)

    def test_03_busca_binaria_e_sequencial(self):
        chave_ordenada = self.lh.regiao_ordenada[500]
        res_ord = self.lh.buscar(chave_ordenada)
        self.assertTrue(res_ord["encontrado"])
        self.assertGreater(res_ord["iteracoes_binaria"], 0)
        self.assertEqual(res_ord["iteracoes_sequencial"], 0)

        chave_cauda = 888888
        self.lh.inserir(chave_cauda)
        res_cauda = self.lh.buscar(chave_cauda)
        self.assertTrue(res_cauda["encontrado"])
        self.assertGreater(res_cauda["iteracoes_binaria"], 0)
        self.assertEqual(res_cauda["iteracoes_sequencial"], 1)

        res_ausente = self.lh.buscar(-1)
        self.assertFalse(res_ausente["encontrado"])

    def test_04_intercalacao_automatica_na_decima_insercao(self):
        tamanho_inicial = len(self.lh.regiao_ordenada)
        chaves_novas = [100000 + i for i in range(10)]

        for i in range(9):
            self.lh.inserir(chaves_novas[i])
        self.assertEqual(len(self.lh.cauda), 9)

        sucesso, msg = self.lh.inserir(chaves_novas[9])
        self.assertTrue(sucesso)

        self.assertEqual(len(self.lh.cauda), 0)
        self.assertEqual(len(self.lh.regiao_ordenada), tamanho_inicial + 10)

        self.assertEqual(self.lh.regiao_ordenada, sorted(self.lh.regiao_ordenada))

if __name__ == "__main__":
    unittest.main()