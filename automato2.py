# Alunos:
# Eduardo Fernandes Albuquerque
# João Pedro Vasconcelos de Lima
# Ladielma Carina Santos Teixeira
# Marcelo Malcher Gillet de Loreto Melo
# Virgilio Cardoso Dantas Neto

#código referente a questão 2

class Automato_Questao_2:
    #Construtor para inicialização do automato
    def __init__(self, estados, alfabeto, func_transicao, estado_inicial, estado_final):
        self.estados = estados
        self.alfabeto = alfabeto
        self.func_transicao = func_transicao
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final
        
    #função para execução do automato
    def executar(self, cadeia):
        #Inicialização do estado atual, contador do tamanho da cadeia e lista de possíveis posições da palavra 'computador'
        estado_atual = self.estado_inicial
        posicoes = []
        contador = 0
        #laço para percorrer os símbolos da cadeia
        for i in range(len(cadeia)):
            #Verifica se o estado atual e o símbolo estão nas transições
            if(estado_atual, (cadeia[i])) in self.func_transicao:
                #Atualiza o estado atual
                estado_atual = self.func_transicao[(estado_atual, (cadeia[i]))]
                #Veriifica se o estado atual é o estado final e se a palavra 'computador' não é a última da cadeia
                #i+1 <= len(cadeia) - 1 --> i+1 é a posição do próximo símbolo da cadeia, len(cadeia) - 1 é a última posição da cadeia
                if(estado_atual == 'q11' and i+1 <= len(cadeia) - 1):
                    #Verifica se o próximo símbolo não é uma letra
                    #Verifica se o símbolo anterior a palavra 'computador' é um espaço ou se é a primeira palavra da cadeia
                    if((cadeia[i+1]) in [' ', ',', '.', ':', ';', '!', '?'] and (cadeia[i-10] in [' ', ''] or i-10 < 0)):
                        #Adiciona as posições da palavra 'computador' na lista de posições
                        posicoes.append((contador - 9, contador))
                        #Como o automato chegou ao estado q11, o estado atual é atualizado para q0 para poder analisar a próxima palavra
                        estado_atual = 'q0'
                    else:
                        #Volta para o estado inicial para analisar a próxima palavra
                        estado_atual = 'q0'
                #Verifica se a palavra 'computador' é a última da cadeia
                #Verifica se o símbolo anterior a palavra 'computador' é um espaço ou se é a primeira palavra da cadeia
                if(estado_atual == 'q11' and i+1 > len(cadeia) - 1 and (cadeia[i-10] in [' ', ''] or i-10 < 0)):
                    #Adiciona as posições da palavra 'computador' na lista de posições
                    posicoes.append((contador - 9, contador))
                    #Como é a última palavra da cadeia, o estado atual não precisa ser atualizado
                #Incrementa o contador
                contador += 1
            #Caso o estado atual e o símbolo não estejam nas transições, o estado atual é atualizado para q0 e o contador é incrementado
            else:
                contador += 1
                estado_atual = 'q0'
                continue
        #Verifica se o estado atual é um estado final
        if estado_atual in self.estado_final:
            #Verifica se há palavras 'computador' na cadeia
            if(len(posicoes) > 0):
                print(f"A cadeia foi aceita")
                print("Posições das palavras 'computador': ")
                for j in range(len(posicoes)):
                    print(f"Posição {j+1}: {posicoes[j]}")
            else:
                print(f"A cadeia foi aceita")
                print("Não há palavras 'computador' na cadeia")
            return True
        else:
            return False
        
    #função para formatar as chamadas de execução do automato
    def questao_2(self, automato, cadeia):
        print("")
        print("")
        print(f"Cadeia: {cadeia}")
        execucao = automato.executar(cadeia)
        #Verifica se a cadeia foi aceita ou rejeitada
        if(execucao):
            pass
        else:
            print(f"A cadeia '{cadeia}' foi rejeitada")
        print("")
        print("")
    
        