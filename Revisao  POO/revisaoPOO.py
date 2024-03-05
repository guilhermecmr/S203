class Filme:
    def __init__(self, titulo, duracao, diretor, ano, genero):
        self.titulo = titulo
        self.ano = ano
        self.diretor = diretor
        self.genero = genero
        self.duracao = duracao
        
    def mostraInfo(self):
        print("\nTítulo:", self.titulo)
        print("Ano:", self.ano)
        print("Diretor:", self.diretor)
        print("Gênero:", self.genero)
        print("Duração:", self.duracao)

def listarAno(filmes):
    for i in range(len(filmes)):
        for j in range(len(filmes)):
            if filmes[i].ano < filmes[j].ano:
                temp = filmes[i]
                filmes[i] = filmes[j]
                filmes[j] = temp
    return filmes

def listarGenero(filmes):
    for i in range(len(filmes)):
        for j in range(len(filmes)):
            if filmes[i].genero < filmes[j].genero:
                temp = filmes[i]
                filmes[i] = filmes[j]
                filmes[j] = temp
    return filmes

def listarDiretor(filmes):
    for i in range(len(filmes)):
        for j in range(len(filmes)):
            if filmes[i].diretor < filmes[j].diretor:
                temp = filmes[i]
                filmes[i] = filmes[j]
                filmes[j] = temp
    return filmes

def filtrarAno(filmes, ano):
    for i in range(len(filmes)):
        if filmes[i].ano == ano:
            filmes[i].mostraInfo()
    return

def filtrarGenero(filmes, genero):
    for i in range(len(filmes)):
        if filmes[i].genero == genero:
            filmes[i].mostraInfo()
    return

def filtrarDiretor(filmes, diretor):
    for i in range(len(filmes)):
        if filmes[i].diretor == diretor:
            filmes[i].mostraInfo()
    return
    
def main(): 
    filmes = []
    opcao_menu = 0
    opcao_lista = 0
    opcao_filtro = 0
    
    while opcao_menu != 4:
        print("\n1 - Cadastrar um novo filme \n2 - Listar filmes  \n3 - Filtrar filmes \n4 - Sair")
        opcao_menu = int(input("Opção: "))
        
        if opcao_menu == 1:
            titulo = input("\nTítulo: ")
            duracao = input("Duração: ")
            diretor = input("Diretor: ")
            ano = input("Ano: ")
            genero = input("Gênero: ")
            filme = Filme(titulo, duracao, diretor, ano, genero)
            filmes.append(filme)
        
        elif opcao_menu == 2:
            print("\n1 - Listar por ano \n2 - Listar por gênero \n3 - Listar por diretor")
            opcao_lista = int(input("Opção: "))
            
            if opcao_lista == 1:
                filmes = listarAno(filmes)
                for i in range(len(filmes)):
                    filmes[i].mostraInfo()
            
            elif opcao_lista == 2:
                filmes = listarGenero(filmes)
                for i in range(len(filmes)):
                    filmes[i].mostraInfo()
                    
            elif opcao_lista == 3:
                filmes = listarDiretor(filmes)
                for i in range(len(filmes)):
                    filmes[i].mostraInfo()
            
            else:
                print("Opção inválida.")
                
        elif opcao_menu == 3:
            print("\n1 - Filtrar por ano \n2 - Filtrar por gênero \n3 - Filtrar por diretor")
            opcao_filtro = int(input("Opção: "))
            
            if opcao_filtro == 1:
                ano = input("Ano: ")
                filtrarAno(filmes, ano)
            
            elif opcao_filtro == 2:
                genero = input("Gênero: ")
                filtrarGenero(filmes, genero)
                
            elif opcao_filtro == 3:
                diretor = input("Diretor: ")
                filtrarDiretor(filmes, diretor)
            
            else:
                print("Opção inválida.")
                
        elif opcao_menu == 4:
            print("Saindo...")
            
        else:
            print("Opção inválida.")
            
    return 0
    
if __name__ == "__main__":  
    main()