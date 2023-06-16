from console_colorido import ConsoleColorido

class Tabuleiro:
   DESENHO_AGUA = ConsoleColorido.textoNegritoFundoAzul(" ~ ") # len() == 3
   DESENHO_AGUA_ATINGIDA = ConsoleColorido.textoNegritoFundoAmarelo(" O ") # len() == 3
   DESENHO_EMBARCACAO = ConsoleColorido.textoNegritoFundoAmarelo(" E ") # len() == 3
   DESENHO_EMBARCACAO_ATINGIDA = ConsoleColorido.textoNegritoFundoVermelho(" X ") # len() == 3

   SEPARADOR_LINHAS = "---" # len() == 3
   SEPARADOR_COLUNAS = '|' # len() == 1


   @staticmethod
   def corIndiceLinha(linha: str) -> str:
      return ConsoleColorido.textoVermelho(linha)


   @staticmethod
   def corIndiceColuna(coluna: str) -> str:
      return ConsoleColorido.textoVerde(coluna)


   def __init__(self, linhas: int, colunas: int):
      self._linhas = linhas
      self._colunas = colunas

      self._tabuleiro = [[Tabuleiro.DESENHO_AGUA] * colunas for linha in range(linhas)]


   def __getitem__(self, linha: int) -> list[str]:
         return self._tabuleiro[linha]


   @property
   def linhas(self) -> int:
      return self._linhas


   @property
   def colunas(self) -> int:
      return self._colunas


   def _imprimirIndentacao(self) -> None:
      print("  ", end='')


   def _imprimirIndiceColunas(self) -> None:
      self._imprimirIndentacao()
      for c in range(self.colunas):
         C_COLORIDO = Tabuleiro.corIndiceColuna(str(c))
         coluna = (f"  {C_COLORIDO} " if (c < 10) else
                   f"  {C_COLORIDO}")
         print(coluna, end='')
      print()


   def _imprimirSeparadorLinhas(self) -> None:
      self._imprimirIndentacao()
      print(f" {Tabuleiro.SEPARADOR_LINHAS}" * self.colunas)


   def _imprimirLinha(self, linha: list[str], indiceLinha: int) -> None:
      INDICE_LINHA_COLORIDO = Tabuleiro.corIndiceLinha(str(indiceLinha))
      print(f"{INDICE_LINHA_COLORIDO} ", end='')
      for coluna in linha:
         print(f"{Tabuleiro.SEPARADOR_COLUNAS}{coluna}", end='')
      print(f"{Tabuleiro.SEPARADOR_COLUNAS} {INDICE_LINHA_COLORIDO}")


   def posicaoValida(self, linhaColuna: tuple[int, int]) -> bool:
      linha, coluna = linhaColuna
      return ((linha >= 0 and linha < self.linhas) and
              (coluna >= 0 and coluna < self.colunas))


   def em(self, linhaColuna: tuple[int, int]) -> str:
      if (not self.posicaoValida(linhaColuna)):
         return ""

      linha, coluna = linhaColuna
      return self[linha][coluna]


   def imprimir(self) -> None:
      self._imprimirIndiceColunas()
      self._imprimirSeparadorLinhas()

      for i in range(self.linhas):
         self._imprimirLinha(self[i], i)
         self._imprimirSeparadorLinhas()

      self._imprimirIndiceColunas()
