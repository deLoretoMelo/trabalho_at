# Alunos:
# Eduardo Fernandes Albuquerque
# João Pedro Vasconcelos de Lima
# Ladielma Carina Santos Teixeira
# Marcelo Malcher Gillet de Loreto Melo
# Virgilio Cardoso Dantas Neto

#código referente a questão 3

class Transdutor:
    #Construtor para inicialização do automato
    def __init__(self, estado_inicial, estados, alfabeto_entrada, alfabeto_saida, func_transicao_transducao, estados_finais):
        self.estado_inicial = estado_inicial
        self.estados = estados
        self.alfabeto_entrada = alfabeto_entrada
        self.alfabeto_saida = alfabeto_saida
        self.func_transicao_transducao = func_transicao_transducao
        self.estados_finais = estados_finais
        
    #Execução com input do usuário
    def executar_input(self):
        #Inicialização do estado atual, listas de entradas e saídas
        entradas = []
        saidas = []
        estado_atual = self.estado_inicial
        #laço para manter o input e analise de input
        while True:
            entrada = input(f"Digite um elemento do alfabeto de entrada ({self.alfabeto_entrada}) ou 'fim' para terminar: ")
            #caso não seja 'fim', o programa acaba
            if entrada == 'fim':
                break
            #caso o elemento não esteja no alfabeto de entrada, o programa acaba
            elif entrada not in self.alfabeto_entrada:
                print("Elemento inválido")
                entradas.append(entrada)
                saidas.append("Elemento inválido")
                break
            #condição para verificar se a transição está definida
            elif (estado_atual, entrada) in self.func_transicao_transducao:
                #Atualiza o estado atual e salva a saída
                estado_atual, saida = self.func_transicao_transducao[(estado_atual, entrada)]
                #adiciona a entrada e a saída nas listas
                entradas.append(entrada)
                saidas.append(saida)
                #mostra a saída imediata ao usuário
                print(f"Resposta da máquina: {saida}\n")
            #Condição para caso a transição não esteja definida
            else:
                print("Transição não definida")
                break
        #Retorna as listas
        return entradas, saidas
    
    #Execução com testes de estresse
    def executar_teste_de_estresse(self, testes):
        #Inicialização do estado atual,contador e lista de saídas
        saidas = []
        estado_atual = self.estado_inicial
        contador = 1
        #laço para percorrer os testes
        for teste in testes:
            #mostra o teste de estresse, inicializa a saída do teste que está sendo percorrido
            print(f"Teste de estresse {contador}: {teste}")
            saida = []
            #laço para percorrer os elementos do teste
            for simbolos in teste:
                #condição para verificar se o elemento não está no alfabeto de entrada, caso não esteja, o programa acaba
                if simbolos not in self.alfabeto_entrada:
                    print(f"Elemento '{simbolos}' inválido, cadeia: {teste} inváldia")
                    saida = ["Cadeia inválida"]
                    break
                #condição para verificar se a transição está definida
                elif (estado_atual, simbolos) in self.func_transicao_transducao:
                    #atualiza o estado atual e a saída
                    saida += self.func_transicao_transducao[(estado_atual, simbolos)][1]
                    estado_atual= self.func_transicao_transducao[(estado_atual, simbolos)][0]
                #condição para caso a transição não esteja definida
                else:
                    print(f"Transição não definida, {teste} inválido")
                    saida = ["Cadeia inválidia"]
                    break
            #mostra a saída do teste e verifica se a cadeia é válida pela saída
            if saida != ["Cadeia inválida"]:
                print(f"Resposta da máquina: {saida}")
            #contador é incrementado e a saída é adicionada na lista de saídas
            contador += 1
            saidas.append(saida)
            print("")
        #retorna a lista de saídas
        return saidas
        
        
    #função para formatar as chamadas de execução do automato
    def questao_3(self):
        #Um menu para o usuário escolher entre colocar moedas ou fazer um teste de estresse, e explicação de como a máquina funciona
        print("\n\n")
        print("Bem vindo à máquina de transdução, ao colocar moedas, a máquina irá se uma lata de refrigerante irá sair ou não, se for 0, não saíra, caso contrário, sairá")
        print("As moedar podem ser de 25, 50 ou de 100 centavos, e cada vez que for completado 100 centavos, uma lata de refrigerante sairá")
        print("A máquina funciona da seguinte forma: você pode colocar as moedas ou fazer um teste de estresse")
        print("a. Colocar moedas")
        print("b. Teste de estresse")
        escolha = input("Escolha a opção desejada (a/b): ")
        #escolha do input do usuário
        if escolha == 'a':
            sequencia, saida = self.executar_input()
            print("")
            print(f"A sequência de entrada foi: {sequencia}")
            print(f"A sequência de saída foi: {saida}")
            if "Elemento inválido" in saida:
                print(f"A sequência {sequencia} não é válida")
        #escolha do teste de estresse
        elif escolha == 'b':
            print("")
            estresse = [[], ['5', '20'], ["25", "25", "25", "25"], ["50", "50", "50", "50"], ["100", "100", "100", "100"], ["25", "50", "100", "25", "50", "100"]]
            saidas = self.executar_teste_de_estresse(estresse)
            print(f"Comparação das sequências de Entrada e de Saída:")
            print(estresse)
            print(saidas)
            
        print("")
        print("")
            
        