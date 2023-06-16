class ConsoleColorido:
   RED_TEXT = "\033[31m"
   GREEN_TEXT = "\033[32m"
   YELLOW_TEXT = "\033[33m"
   BLUE_TEXT = "\033[34m"
   BOLD_TEXT = "\033[1m"
   BOLD_RED_TEXT = "\033[1;31m"
   BOLD_GREEN_TEXT = "\033[1;32m"
   BOLD_YELLOW_TEXT = "\033[1;33m"
   BOLD_BLUE_TEXT = "\033[1;34m"
   BOLD_TEXT_RED_BG = "\033[1;41m"
   BOLD_TEXT_GREEN_BG = "\033[1;42m"
   BOLD_TEXT_YELLOW_BG = "\033[1;43m"
   BOLD_TEXT_BLUE_BG = "\033[1;44m"
   UNDERLINE_YELLOW_TEXT = "\033[4;33m"
   RESET= "\033[0m"


   @staticmethod
   def textoNegrito(texto: str) -> str:
      return ConsoleColorido.BOLD_TEXT + texto + ConsoleColorido.RESET


   @staticmethod
   def textoVermelho(texto: str) -> str:
      return ConsoleColorido.RED_TEXT + texto + ConsoleColorido.RESET


   @staticmethod
   def textoVerde(texto: str) -> str:
      return ConsoleColorido.GREEN_TEXT + texto + ConsoleColorido.RESET


   @staticmethod
   def textoAmarelo(texto: str) -> str:
      return ConsoleColorido.YELLOW_TEXT + texto + ConsoleColorido.RESET


   @staticmethod
   def textoAzul(texto: str) -> str:
      return ConsoleColorido.BLUE_TEXT + texto + ConsoleColorido.RESET


   @staticmethod
   def textoNegritoVermelho(texto: str) -> str:
      return ConsoleColorido.BOLD_RED_TEXT + texto + ConsoleColorido.RESET


   @staticmethod
   def textoNegritoVerde(texto: str) -> str:
      return ConsoleColorido.BOLD_GREEN_TEXT + texto + ConsoleColorido.RESET


   @staticmethod
   def textoNegritoAmarelo(texto: str) -> str:
      return ConsoleColorido.BOLD_YELLOW_TEXT + texto + ConsoleColorido.RESET


   @staticmethod
   def textoNegritoAzul(texto: str) -> str:
      return ConsoleColorido.BOLD_BLUE_TEXT + texto + ConsoleColorido.RESET


   @staticmethod
   def textoNegritoFundoVermelho(texto: str) -> str:
      return ConsoleColorido.BOLD_TEXT_RED_BG + texto + ConsoleColorido.RESET


   @staticmethod
   def textoNegritoFundoVerde(texto: str) -> str:
      return ConsoleColorido.BOLD_TEXT_GREEN_BG + texto + ConsoleColorido.RESET


   @staticmethod
   def textoNegritoFundoAmarelo(texto: str) -> str:
      return ConsoleColorido.BOLD_TEXT_YELLOW_BG + texto + ConsoleColorido.RESET


   @staticmethod
   def textoNegritoFundoAzul(texto: str) -> str:
      return ConsoleColorido.BOLD_TEXT_BLUE_BG + texto + ConsoleColorido.RESET


   @staticmethod
   def textoSublinhadoAmarelo(texto: str) -> str:
      return ConsoleColorido.UNDERLINE_YELLOW_TEXT + texto + ConsoleColorido.RESET
