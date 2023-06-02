from console_colorido import ConsoleColorido

class Tabuleiro:
   CARACTERE_AGUA = ConsoleColorido.BOLD_TEXT_BLUE_BG + '~' + ConsoleColorido.RESET
   CARACTERE_EMBARCACAO = 'O'
   CARACTERE_EMBARCACAO_ATINGIDA = ConsoleColorido.BOLD_TEXT_RED_BG + 'X' + ConsoleColorido.RESET

   SEPARADOR_LINHAS = "---"
   SEPARADOR_COLUNAS = '|'


   def __init__(self, linhas: int, colunas: int, embarcacoes: int):
      self._linhas = linhas
      self._colunas = colunas
      self._embarcacoes = embarcacoes

      self._tabuleiro = [[Tabuleiro.CARACTERE_AGUA] * colunas for linha in range(linhas)]


   @property
   def linhas(self) -> int:
      return self._linhas


   @property
   def colunas(self) -> int:
      return self._colunas


   @property
   def embarcacoes(self) -> int:
      return self._embarcacoes


   @property
   def tabuleiro(self) -> list[str, str]:
      return self._tabuleiro


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


   def imprimir(self) -> None:
      self._imprimirIndiceColunas()
      self._imprimirSeparadorLinhas()

      for l in range(self.linhas):
         print(f"{l} ", end='') # imprime o índice da linha
         for coluna in self.tabuleiro[l]:
            print(f"{Tabuleiro.SEPARADOR_COLUNAS} {coluna} ", end='')
         print(f"{Tabuleiro.SEPARADOR_COLUNAS} {l}") # imprime o índice da linha
         self._imprimirSeparadorLinhas()

      self._imprimirIndiceColunas()


   def posicionarEmbarcacao(self, linha: int, coluna: int) -> bool:
      if (self.tabuleiro[linha][coluna] == Tabuleiro.CARACTERE_AGUA):
         self.tabuleiro[linha][coluna] = Tabuleiro.CARACTERE_EMBARCACAO
         return True

      return False

