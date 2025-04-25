import typing
from lexer import lexer


class Parser:
    def __init__(self, tokens: typing.List[lexer.Token]):
        self.tokens = tokens  # Tokens by lexer
        self.pos = 0
        self.current: lexer.Token = self.tokens[self.pos] if self.tokens else None

    # Next token
    def advance(self):
        self.pos += 1
        self.current = self.tokens[self.pos] if self.pos < len(self.tokens) else None

    # Match token with token_type (tipo)
    def match(self, expected_type: str):
        if self.current and self.current.tipo == expected_type:
            self.advance()
        else:
            raise SyntaxError(f"Esperado {expected_type}, mas encontrou {self.current}")

    # Parse method to expr
    def parse(self):
        self.formula()
        if self.current is not None:
            raise SyntaxError(f"Tokens restantes: {self.current}")

    # FORMULA = CONSTANTE | PROPOSICAO | FORMULAUNARIA | FORMULABINARIA
    def formula(self):
        if self.current.tipo in ["CONSTANTE", "PROPOSICAO"]:
            self.advance()
        elif self.current.tipo == "ABREPAREN":
            self.advance()
            if self.current.tipo == "OPERADORUNARIO":
                self.formula_unaria()
            elif self.current.tipo == "OPERADORBINARIO":
                self.formula_binaria()
            else:
                raise SyntaxError(
                    f'Esperado operador após "(", encontrou: {self.current}'
                )
        else:
            raise SyntaxError(f"Expressão mal formada, encontrou: {self.current}")

    # FORMULAUNARIA = ABREPAREN OPERADORUNARIO FORMULA FECHAPAREN
    def formula_unaria(self):
        self.match("OPERADORUNARIO")
        self.formula()
        self.match("FECHAPAREN")

    # FORMULABINARIA = ABREPAREN OPERADORBINARIO FORMULA FORMULA FECHAPAREN
    def formula_binaria(self):
        self.match("OPERADORBINARIO")
        self.formula()
        self.formula()
        self.match("FECHAPAREN")


def is_valid(expr: str):
    try:
        tokens = lexer.lexer(expr)  # Getting tokens
        parser = Parser(tokens)
        parser.parse()  # Validating tokens
        return True
    except SyntaxError:
        return False


# Teste do parser
if __name__ == "__main__":
    # Teste do parser

    exp = r"(\wedge 1x true)"
    print(is_valid(exp))
    exp = r"(\wedge (1x true)"
    print(is_valid(exp))
