from biblioteca_virtual import adicionar_livro, listar_livros, remover_livro


def test_adicionar_livro():
    resultado = adicionar_livro(
        "Neuromancer", "William Gibson", "Ficção Científica", 1984
    )
    assert resultado == True


def test_listar_livros():
    adicionar_livro("Dune", "Frank Herbert", "Ficção Científica", 1965)

    livros = listar_livros()
    assert len(livros) == 2
    assert livros[0]["titulo"] == "Neuromancer"
    assert livros[1]["titulo"] == "Dune"


def test_remover_livro():
    resultado = remover_livro("Neuromancer")
    assert resultado == True

    livros = listar_livros()
    assert len(livros) == 1
    assert livros[0]["titulo"] == "Dune"
