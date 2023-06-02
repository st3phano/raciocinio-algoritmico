class ConsoleColorido:
   BOLD_TEXT = "\033[1m"
   BOLD_TEXT_RED_BG = "\033[1;41m"
   BOLD_TEXT_BLUE_BG = "\033[1;44m"
   RESET= "\033[0m"

   @staticmethod
   def negrito(texto: str) -> str:
      return ConsoleColorido.BOLD_TEXT + texto + ConsoleColorido.RESET
   
   @staticmethod
   def negrito(inteiro: int) -> str:
      return ConsoleColorido.BOLD_TEXT + str(inteiro) + ConsoleColorido.RESET
