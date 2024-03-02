class Filme:
    def __init__(self, titulo, ano, diretor, genero, duracao):
        # Inicializa os atributos do filme
        self.titulo = titulo
        self.ano = ano
        self.diretor = diretor
        self.genero = genero
        self.duracao = duracao

class CatalogoFilmes:
    def __init__(self):
        # Inicializa uma lista vazia para armazenar os filmes
        self.filmes = []

    def adicionar_filme(self, filme):
        # Adiciona um filme à lista de filmes
        self.filmes.append(filme)

    def listar_filmes(self, filtro=None, ordenacao=None):
        # Filtra e/ou ordena os filmes conforme solicitado
        filmes_filtrados = self.filmes

        if filtro:
            # Filtra os filmes de acordo com o critério especificado
            filmes_filtrados = [filme for filme in filmes_filtrados if getattr(filme, filtro[0]) == filtro[1]]

        if ordenacao:
            # Ordena os filmes com base no critério especificado
            filmes_filtrados.sort(key=lambda x: getattr(x, ordenacao))

        # Exibe os filmes na tela
        for filme in filmes_filtrados:
            print(f"Título: {filme.titulo}, Ano: {filme.ano}, Diretor: {filme.diretor}, Gênero: {filme.genero}, Duração: {filme.duracao} minutos")

def cadastrar_filme():
    # Solicita ao usuário informações sobre o filme e retorna um objeto Filme
    titulo = input("Título do filme: ")
    ano = int(input("Ano de lançamento: "))
    diretor = input("Diretor(a): ")
    genero = input("Gênero: ")
    duracao = int(input("Duração (em minutos): "))

    return Filme(titulo, ano, diretor, genero, duracao)

catalogo = CatalogoFilmes()

while True:
    # Menu de opções
    print("\n1. Adicionar filme")
    print("2. Listar filmes")
    print("3. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        # Adiciona um novo filme ao catálogo
        filme = cadastrar_filme()
        catalogo.adicionar_filme(filme)
        print("Filme cadastrado com sucesso!")
    elif escolha == "2":
        # Permite listar filmes com opções de filtro e ordenação
        filtro = input("Filtrar por ano, diretor ou genero: ").lower()
        ordenacao = input("Ordenar por ano, diretor ou genero: ").lower()
        catalogo.listar_filmes(filtro.split(), ordenacao)
    elif escolha == "3":
        # Encerra o programa
        print("Saindo...")
        break
    else:
        # Mensagem de opção inválida
        print("Opção inválida. Tente novamente.")
