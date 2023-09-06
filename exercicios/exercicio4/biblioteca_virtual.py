livros = []


def adicionar_livro(titulo, autor, genero, ano):
    livro = {"titulo": titulo, "autor": autor, "genero": genero, "ano": ano}
    livros.append(livro)
    return True


def remover_livro(titulo):
    global livros
    livros = [livro for livro in livros if livro["titulo"] != titulo]
    return True


def listar_livros():
    return livros
