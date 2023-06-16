from console_colorido import ConsoleColorido

class Tabuleiro:
   DESENHO_AGUA = ConsoleColorido.textoNegritoFundoAzul(" ~ ") # len() == 3
   DESENHO_AGUA_ATINGIDA = ConsoleColorido.textoNegritoFundoAzul(" O ") # len() == 3
   DESENHO_EMBARCACAO = ConsoleColorido.textoNegritoFundoAmarelo(" E ") # len() == 3
   DESENHO_EMBARCACAO_ATINGIDA = ConsoleColorido.textoNegritoFundoVermelho(" X ") # len() == 3

   SEPARADOR_LINHAS = "---" # len() == 3
   SEPARADOR_COLUNAS = '|' # len() == 1


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
         coluna = (f"  {c} " if (c < 10) else
                   f"  {c}")
         print(coluna, end='')
      print()


   def _imprimirSeparadorLinhas(self) -> None:
      self._imprimirIndentacao()
      print(f" {Tabuleiro.SEPARADOR_LINHAS}" * self.colunas)


   def _imprimirLinha(self, linha: list[str], indiceLinha: int) -> None:
      print(f"{indiceLinha} ", end='')
      for coluna in linha:
         print(f"{Tabuleiro.SEPARADOR_COLUNAS}{coluna}", end='')
      print(f"{Tabuleiro.SEPARADOR_COLUNAS} {indiceLinha}")


   def imprimir(self) -> None:
      self._imprimirIndiceColunas()
      self._imprimirSeparadorLinhas()

      for i in range(self.linhas):
         self._imprimirLinha(self[i], i)
         self._imprimirSeparadorLinhas()

      self._imprimirIndiceColunas()


   def posicionarEmbarcacao(self, linhaColuna: tuple[int, int]) -> bool:
      linha, coluna = linhaColuna
      if ((linha < 0 or linha >= self.linhas) or
          (coluna < 0 or coluna >= self.colunas)):
         return False

      if (self[linha][coluna] != Tabuleiro.DESENHO_AGUA):
         return False

      self[linha][coluna] = Tabuleiro.DESENHO_EMBARCACAO
      return True
