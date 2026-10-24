class Commit:
    """
    Classe que representa um commit individual no histórico do Git.
    Cada commit possui um identificador único, uma mensagem descritiva,
    um autor associado e uma referência opcional para o commit anterior (pai).
    """

    def __init__(self, id, mensagem, autor, pai=None):
        """
        Inicializa um novo commit salvando suas propriedades básicas.
        O commit pai é opcional e assume None caso seja o primeiro commit.
        """
        self.id = id
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai

    def historico(self):
        """
        Imprime as informações do commit atual e, de forma recursiva,
        solicita ao commit pai que faça o mesmo até atingir o início da linha do tempo.
        """
        print(f"#{self.id} {self.mensagem} ({self.autor})")

        if self.pai is None:
            return

        self.pai.historico()


class Repositorio:
    """
    Classe que gerencia o ciclo de vida dos commits de um projeto.
    Controla o ponteiro para o commit mais recente (head) e a quantidade
    total de alterações efetuadas através de um contador interno.
    """

    def __init__(self, nome, autor):
        """
        Cria um repositório vazio informando o nome e o autor padrão.
        A propriedade head inicia sem apontar para nenhum commit.
        """
        self.nome = nome
        self.autor = autor
        self.head = None
        self.contador_de_commits = 0

    def commitar(self, mensagem):
        """
        Cria um novo commit no repositório. Atualiza o contador de identificação,
        gera a nova instância apontando o head atual como pai e move o head
        para este novo commit criado.
        """
        self.contador_de_commits = self.contador_de_commits + 1
        novo_commit = Commit(self.contador_de_commits, mensagem, self.autor, self.head)
        self.head = novo_commit

    def log(self):
        """
        Exibe o histórico completo de commits a partir do mais recente.
        Caso o repositório não possua commits, exibe uma mensagem informativa.
        """
        if self.head is None:
            print("Nenhum commit ainda")
            return

        self.head.historico()

    def total_de_commits(self):
        """
        Percorre a corrente de commits partindo do head até o commit inicial
        para calcular e retornar o total acumulado existente.
        """
        total = 0
        atual = self.head

        while atual is not None:
            total = total + 1
            atual = atual.pai

        return total


# ==============================================================================
# Execução dos Testes (Modifique com seus dados)
# ==============================================================================

# IMPORTANTE: Substitua pelo seu Nome e seu número de RA reais
repositorio = Repositorio("meu-projeto", "Ryan Tavares de Lima - 6326226")

repositorio.log()

repositorio.commitar("Cria o projeto")
repositorio.commitar("Adiciona o README")
repositorio.commitar("Corrige o titulo do README")

repositorio.log()

print(repositorio.total_de_commits())
