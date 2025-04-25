# Leonardo Scanavacca Falango

import sys

from parser.parser import is_valid


# Formating the ouput
def validate(expr: str):
    return "válida" if is_valid(expr) else "inválida"


# Foreach testing file, foreach line use validate(line)
def parse_file(filepath: str):
    # Open and read the file
    with open(filepath, "r") as f:
        # verify if the file is valid
        n_formulas = int(f.readline())
        print(f"Arquivo: {filepath} Quantidade de validações: {n_formulas}")

        # read all lines
        lines = f.readlines()
        if n_formulas != len(lines):
            raise Exception(
                "Arquivo contendo conteudo inválido, quantidade de validações não bate com a quantidade de linhas"
            )

        # foreach formula validade
        for i in range(n_formulas):
            line = lines[i].strip()
            p = validate(line)
            print(f"[{p:<{8}}] Expressão: {line}")


if __name__ == "__main__":
    
    if "hide" not in sys.argv:
    # Test files
      parse_file("test_files/val1.txt")
      parse_file("test_files/val2.txt")
      parse_file("test_files/val3.txt")

    # para testar seu arquivo só colocar de argumento
    if len(sys.argv) > 1:
        files = [f for f in sys.argv[1:] if f.endswith(".txt") and f != "hide"]
        if not files:
            raise Exception("Arquivo inválido, deve ser .txt")
        
        for file in files:
            parse_file(file)
