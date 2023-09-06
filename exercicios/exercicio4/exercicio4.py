from biblioteca_virtual import adicionar_livro, listar_livros, remover_livro


def main():
    while True:
        print("Biblioteca Virtual - Opções:")
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Remover livro")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            genero = input("Gênero do livro: ")
            ano = int(input("Ano de publicação do livro: "))
            adicionar_livro(titulo, autor, genero, ano)
            print("Livro adicionado com sucesso!")
        elif escolha == "2":
            livros = listar_livros()
            if not livros:
                print("Nenhum livro na biblioteca.")
            else:
                for livro in livros:
                    print(f"Título: {livro['titulo']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Gênero: {livro['genero']}")
                    print(f"Ano de publicação: {livro['ano']}")
        elif escolha == "3":
            titulo = input("Digite o título do livro a ser removido: ")
            resultado = remover_livro(titulo)
            if resultado:
                print("Livro removido com sucesso!")
            else:
                print("Livro não encontrado na biblioteca.")
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
