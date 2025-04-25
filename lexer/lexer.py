import re
import typing

# Tokens
TOKEN_REGEX = [
    ("CONSTANTE", r"\btrue\b|\bfalse\b"),
    ("OPERADORUNARIO", r"\\neg"),
    ("OPERADORBINARIO", r"\\wedge|\\vee|\\rightarrow|\\leftrightarrow"),
    ("ABREPAREN", r"\("),
    ("FECHAPAREN", r"\)"),
    ("PROPOSICAO", r"\b[0-9][0-9a-z]*\b"),
    ("ESPACO", r"\s+"),
]


class Token:
    def __init__(self, tipo: str, value: typing.Any):
        self.tipo = tipo
        self.value = value

    # For printing
    def __repr__(self):
        return f"Token({self.tipo}, {repr(self.value)})"


def lexer(exp: str):
    tokens = []
    pos = 0
    while pos < len(exp):
        match = None
        for token_type, regex in TOKEN_REGEX:
            pattern = re.compile(regex)
            match = pattern.match(exp, pos)
            if match:
                if token_type != "ESPACO":
                    valor = match.group(0)
                    tokens.append(Token(token_type, valor))
                pos = match.end()
                break
        if not match:
            raise SyntaxError(f"Token inválido na posição {pos}: {exp[pos]}")
    return tokens


if __name__ == "__main__":
    # Teste do lexer
    exp = r"(\wedge 1x true)"
    tokens = lexer(exp)
    for t in tokens:
        print(t)
