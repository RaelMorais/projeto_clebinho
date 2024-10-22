import random
#ANSI COLORS
ALGO = "\033[33m"
RESET = "\033[0m"
        
class testcc: 
    def __init__(self):
        self.a = "" 
    def dificil(self):
        palavras_dicas = {}
        with open ('palavras.txt', 'r', encoding='utf-8') as file:
            for linha in file:
                linha = linha.strip().lower()
                try:
                    palavra, dica = linha.split(';') #slip identa conforme a orientação
                    palavras_dicas[palavra] = dica
                except ValueError as erro_value:
                    print(erro_value)
            escolha = input(">>>Escolha abaixo<<<\n1 - Jogar\n2 - Adicionar palavra  \n3 - Remover Palavra \n4 - Sair \n")
            
            match escolha:
                case '1':
                    palavra = random.choice(list(palavras_dicas.keys()))
                    dica = palavras_dicas[palavra]#busca a chave e imprime com seu valor, ex: chave(amor)valor(sentimento profundo)
                    palavra_escondida = ['*'] * len(palavra)

                    print(dica)
                    print(f"Quantidade de palavras escondidas:", " ".join(palavra_escondida))#join serve para unir os nomes conforme identação
                    tentativas = 6
                    palavras_chutadas = []
                    while tentativas > 0:
                        chute = input("Chute uma letra: ").strip().lower() #strip = espaços em brancos e lower para tudo minusculo
                        try:
                            if chute in palavras_chutadas: #se a letra for repetida, tente outra 
                                print("tente outra letra, essa já foi")
                                continue
                            if chute in palavra: 
                                for posicao in range(len(palavra)):
                                    if palavra[posicao] == chute: #verifica se alguma letra do chute é igual na palavra e qual a posição 
                                        palavra_escondida[posicao] = chute #informa se a letra chutada é igual a da palavra e em qual posição na escondida está 
                            else:
                                tentativas -= 1
                                print(f"Letra errada, você tem {tentativas} chances")
                            print(f"Palavra: {' '.join(palavra_escondida)}")
                            if '*' not in palavra_escondida: #se '*' não estiver em palavra escondida, o jogador ganhou
                                print(f"voce ganhou, a palavra era {ALGO}{palavra}{RESET}")
                                break
                        except ValueError as value_erro:
                            print(value_erro)
                    else:
                        print(f"Voce perdeu, a palavra era {palavra}")
                case '2':    
                    """
                        O usuário é solicitado a informar quantas palavras deseja adicionar.
                        Para cada nova palavra, é pedido uma dica correspondente.
                        As novas palavras e dicas são armazenadas no dicionário `palavras_dicas`.
                        Após a coleta das informações, o dicionário é salvo no arquivo 'palavras.txt'.
                        Para salvar palavras as palavras com dicas, usa dicionario que é chave-valor
                        exemplo:
                        Médico;Saúde 
                    """
    
                    num_palavras = int(input("Qual o número de palavras a serem adicionadas? "))
                    with open('palavras.txt', 'r') as file:
                        for _ in range(num_palavras):
                            nova_palavra = input("Qual a nova palavra? ").strip().lower()
                            nova_dica = input("Qual a dica dessa palavra? ").strip().lower()
                            palavras_dicas[nova_palavra] = nova_dica
                    with open('palavras.txt', 'a') as file:
                            file.write(f'{nova_palavra};{nova_dica}\n')
                case '3':
                    while True:
                        print(">>>Entre com senha ou usuario<<<")
                        user = input("Digite seu usuario: ")
                        password = input("Digite sua senha: ")
                        if user == "admin" and password == "123456":
                            print(f"Bem vindo {user}, aqui pode remover palavra")
                            remover_palavra = input("Qual palavra vai ser removida? ").strip().lower()
                            if remover_palavra in palavras_dicas:
                                del palavras_dicas[remover_palavra]
                                with open('palavras.txt', 'a', encoding='utf-8') as file:
                                    for p, d in palavras_dicas.items():
                                        file.write(f'{p};{d}\n')
                                    print(f"Palavra {remover_palavra} foi removida.")
                            else:
                                print("Palavra não reconhecida.")
                            break
                        else:
                            print("Acesso negado")
                case '4':
                    print("Você está saindo...")
                    exit()
                case 'teste':
                    with open('palavras.txt', 'r',  encoding='utf-8') as file:
                        conteudo = file.read()
                        print(conteudo)
                case _:
                    print("Erro")