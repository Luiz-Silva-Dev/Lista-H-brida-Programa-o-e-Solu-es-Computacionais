import random as ra

class ListaHibrida:
    def __init__(self, seed: int = 42, tamanho_inicial: int = 1024):
        self.seed = seed
        ra.seed(seed)
        self.regiao_ordenada = sorted(ra.sample(range(1, 100000), tamanho_inicial))
        self.cauda = []

    def buscar(self, chave: int) -> dict:
        iteracoes_binaria = 0
        iteracoes_sequencial = 0
        inicio = 0
        fim = len(self.regiao_ordenada) - 1
        encontrado_binario = False
        posicao_binaria = -1

        while inicio <= fim:
            iteracoes_binaria += 1
            meio = (inicio + fim) // 2

            if self.regiao_ordenada[meio] == chave:
                encontrado_binario = True
                posicao_binaria = meio
                break
            elif self.regiao_ordenada[meio] < chave:
                inicio = meio + 1
            else:
                fim = meio - 1

        if encontrado_binario:
            return {
                "encontrado": True,
                "local": f"Região Ordenada (Índice {posicao_binaria})",
                "iteracoes_binaria": iteracoes_binaria,
                "iteracoes_sequencial": 0,
                "total_iteracoes": iteracoes_binaria
            }

        encontrado_cauda = False
        posicao_cauda = -1

        for idx, valor in enumerate(self.cauda):
            iteracoes_sequencial += 1
            if valor == chave:
                encontrado_cauda = True
                posicao_cauda = idx
                break

        if encontrado_cauda:
            return {
                "encontrado": True,
                "local": f"Cauda (Índice {posicao_cauda})",
                "iteracoes_binaria": iteracoes_binaria,
                "iteracoes_sequencial": iteracoes_sequencial,
                "total_iteracoes": iteracoes_binaria + iteracoes_sequencial
            }

        return {
            "encontrado": False,
            "local": "Não encontrada",
            "iteracoes_binaria": iteracoes_binaria,
            "iteracoes_sequencial": iteracoes_sequencial,
            "total_iteracoes": iteracoes_binaria + iteracoes_sequencial
        }

    def inserir(self, chave: int) -> tuple[bool, str]:
        resultado_busca = self.buscar(chave)
        if resultado_busca["encontrado"]:
            return False, "Chave duplicada! A inserção foi rejeitada."
        
        self.cauda.append(chave)
        mensagem = f"Chave {chave} inserida na cauda."

        if len(self.cauda) == 10:
            self._intercalar()
            mensagem = f"Chave {chave} inserida. A cauda atingiu 10 elementos e foi intercalada na região ordenada!"

        return True, mensagem

    def _intercalar(self):
        cauda_ordenada = sorted(self.cauda)
        resultado = []
        i, j = 0, 0
        n1, n2 = len(self.regiao_ordenada), len(cauda_ordenada)

        while i < n1 and j < n2:
            if self.regiao_ordenada[i] <= cauda_ordenada[j]:
                resultado.append(self.regiao_ordenada[i])
                i += 1
            else:
                resultado.append(cauda_ordenada[j])
                j += 1

        while i < n1:
            resultado.append(self.regiao_ordenada[i])
            i += 1

        while j < n2:
            resultado.append(cauda_ordenada[j])
            j += 1

        self.regiao_ordenada = resultado
        self.cauda = []
