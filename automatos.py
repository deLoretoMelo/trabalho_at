# Alunos:
# Eduardo Fernandes Albuquerque
# João Pedro Vasconcelos de Lima
# Ladielma Carina Santos Teixeira
# Marcelo Malcher Gillet de Loreto Melo
# Virgilio Cardoso Dantas Neto

#código referente a questão 1

class Automato:
    #Construtor para inicialização do automato
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
    
    #função para execução do automato
    def executar(self, cadeia):
        #inicializa o estado atual com o estado inicial (q0)
        estado_atual = self.estado_inicial
        try:
            #percorre cada simbolo da cadeia individualmente
            for simbolo in cadeia:
                #Acusa um erro de valor caso o símbolo não pertença ao alfabeto
                if simbolo not in self.alfabeto:
                    raise ValueError(f"{simbolo}")
                #Caso o estado atual e o simbolo estejam nas transições, o estado atual é atualizado
                elif(estado_atual, simbolo) in self.transicoes:
                    print(f"{estado_atual} --{simbolo}--> {self.transicoes[(estado_atual, simbolo)]} foi aceito")
                    #Atualiza o estado atual
                    estado_atual = self.transicoes[(estado_atual, simbolo)]
                #Caso o estado atual e o simbolo não estejam nas transições, um erro de chave é acusado
                else:
                    raise KeyError(f"{self.transicoes[(estado_atual, simbolo)]}")
            #Para o automato aceitar a cadeia, o estado atual deve ser um estado final
            if estado_atual in self.estados_finais:
                print(f"O estado {estado_atual} é final")
                return True
            else:
                print(f"O estado {estado_atual} não é final")
                return False
        #Caso algum dos erros acima seja acusado, a função retorna False
        except KeyError as e:
            print(f"{e} nao existe nas funções de transicoes")
            return False
        except ValueError as e:
            print(f"'{e}' não pertence ao alfabeto")
            return False
    
    #função para formatar as chamadas de execução do automato
    def questao_1(self, automato, cadeias):
        print("")
        print("")
        for cadeia in cadeias:
            print(f"Cadeia: {cadeia}")
            print("")
            execucao = automato.executar(cadeia)
            #Verifica se a cadeia foi aceita ou rejeitada
            if(execucao):
                print(f"A cadeia '{cadeia}' foi aceita")
            else:
                print(f"A cadeia '{cadeia}' foi rejeitada")
            print("")
        print("")
        print("")