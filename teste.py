import automatos as at
import automato2 as at2
import transdutor as td

#questao 1

#letra a:
estados_a = ['q0', 'q1', 'q2', 'q3']
alfabeto_a = ['a', 'b', 'c']
func_transicao_a = {
    ('q0', 'a'): 'q1',
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q2',
    ('q1', 'c'): 'q3',
    ('q2', 'a'): 'q1',
    ('q2', 'b'): 'q2',
    ('q2', 'c'): 'q3',
    ('q3', 'a'): 'q1',
    ('q3', 'c'): 'q3'
}   
estado_inicial_a = 'q0'
estado_final_a = ['q0','q1', 'q2', 'q3']
        
automato1 = at.Automato(estados_a, alfabeto_a, func_transicao_a, estado_inicial_a, estado_final_a)
cadeias_a = ['abac', 'abacabac', 'abacabacabac', 'abacabacabacabac']
        
automato1.questao_1(automato1, cadeias_a)

# #letra b:
estados_b = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9']
alfabeto_b = ['a', 'b', 'c']
func_transicao_b = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q6',
    ('q0', 'c'): 'q6',
    ('q1', 'a'): 'q2',
    ('q2', 'a'): 'q3',
    ('q3', 'b'): 'q4',
    ('q3', 'c'): 'q4',
    ('q4', 'b'): 'q4',
    ('q4', 'c'): 'q4',
    ('q6', 'b'): 'q6',
    ('q6', 'c'): 'q6',
    ('q6', 'a'): 'q7',
    ('q7', 'a'): 'q8',
    ('q8', 'a'): 'q9'
}
estado_final_b = 'q0'
estado_final_b = ['q3', 'q4', 'q9']
automato2 = at.Automato(estados_b, alfabeto_b, func_transicao_b, estado_inicial_a, estado_final_b)
cadeias_b = ['bbbbbbcccaaa', 'abac', 'abacabac', 'abacabacabac', 'abacabacabacabac']
automato2.questao_1(automato2, cadeias_b)

# #letra c:
estados_c = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5']
alfabeto_c = ['a', 'b']
func_transicao_c = {
    ('q0', 'b'): 'q1',
    ('q0', 'a'): 'q2',
    ('q2', 'a'): 'q4',
    ('q2', 'b'): 'q3',
    ('q3', 'b'): 'q3',
    ('q4', 'a'): 'q4',
    ('q4', 'b'): 'q5'
}
estado_inicial_c = 'q0'
estado_final_c = ['q1', 'q2', 'q3', 'q5']
automato3 = at.Automato(estados_c, alfabeto_c, func_transicao_c, estado_inicial_c, estado_final_c)
cadeias_c = ['aaaab', 'ab', 'abab', 'ababab', 'abababab']
automato3.questao_1(automato3, cadeias_c)

# letra d:
estados_d = ['q1', 'q2', 'q3', 'q5']
alfabeto_d = ['a', 'b', 'c']
func_transicao_d = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q3',
    ('q1', 'a'): 'q1',
    ('q1', 'c'): 'q2',
    ('q1', 'b'): 'q3',
    ('q3', 'b'): 'q3',
    ('q3', 'a'): 'q4',
    ('q4', 'c'): 'q2',
    ('q2', 'c'): 'q2'
}
estado_inicial_d = 'q0'
estado_final_d = ['q1', 'q2', 'q3', 'q4']
automato4 = at.Automato(estados_d, alfabeto_d, func_transicao_d, estado_inicial_d, estado_final_d)
cadeias_d = ['aaaaabbbba', 'ab', 'abab', 'ababab', 'abababab']
automato4.questao_1(automato4, cadeias_d)

#automato referente a questão 2:
estados_questao_2 = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11']
alfabeto_questao_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
func_transicao_questao_2 = {
    ('q0', 'c'): 'q2',
    ('q2', 'o'): 'q3',
    ('q3', 'm'): 'q4',
    ('q4', 'p'): 'q5',
    ('q5', 'u'): 'q6',
    ('q6', 't'): 'q7',
    ('q7', 'a'): 'q8',
    ('q8', 'd'): 'q9',
    ('q9', 'o'): 'q10',
    ('q10', 'r'): 'q11',
}
cadeias_questao_2 = ["""O computador é uma máquina capaz de variados tipos de tratamento automático de
 informações ou processamento de dados. Entende-se por computador um sistema físico que
 realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são
 ícones da era da informação. O primeiro computador eletromecânico foi construído por
 Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado
 computador pessoal ou ainda computador doméstico.""", """O computador é uma máquina capaz de variados tipos de tratamento automático de""", 
 """informações ou processamento de dados. Entende-se por computador um sistema físico que""", """realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são""", """ícones da era da informação. O primeiro computador eletromecânico foi construído por""", """Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado""", """computador pessoal ou ainda computador doméstico.""", """O computador é uma máquina capaz de variados tipos de tratamento automático de""", """informações ou processamento de dados. Entende-se por computador um sistema físico que""", """realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são""", """ícones da era da informação. O primeiro computador eletromecânico foi construído por""", """Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado""", """computador pessoal ou ainda computador doméstico.""", """O computador é uma máquina capaz de variados tipos de tratamento automático de""", """informações ou processamento de dados. Entende-se por computador um sistema físico que""", """realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são""", """ícones da era da informação. O primeiro computador eletromecânico foi construído por""", """Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado""", 
 """computador pessoal ou ainda computador doméstico.""", 
 """O computador é uma máquina capaz de variados tipos de tratamento automático de""", 
 """informações ou processamento de dados. Entende-se por computador um sistema físico que""", 
 """realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são""", 
 """ícones da era da informação. O primeiro computador eletromecânico foi construído por""", 
 """Konrad Zuse (1910–1995). Atualmente, um microcomputador é também"""]
estado_inicial_questao_2 = 'q0'
estado_final_questao_2 = ['q0', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11']
automato_questao_2 = at2.Automato_Questao_2(estados_questao_2, alfabeto_questao_2, func_transicao_questao_2, estado_inicial_questao_2, estado_final_questao_2)

automato_questao_2.questao_2(automato_questao_2, cadeias_questao_2)

# questao 3:
estados_questao_3 = ['q0', 'q1', 'q2', 'q3', 'q4']
alfabeto_entrada_questao_3 = ['25', '50', '100']
alfabeto_saida_questao_3 = ['0', '1']
func_transicao_transducao = {
    ('q0', '25'): ('q1', '0'),
    ('q0', '50'): ('q3', '0'),
    ('q0', '100'): ('q4', '1'),
    ('q1', '25'): ('q3', '0'),
    ('q1', '50'): ('q2', '0'),
    ('q1', '100'): ('q1', '1'),
    ('q2', '25'): ('q4', '1'),
    ('q2', '100'): ('q2', '1',),
    ('q2', '50'): ('q1', '1'),
    ('q3', '25'): ('q2', '0'),
    ('q3', '100'): ('q3', '1'),
    ('q3', '50'): ('q4', '1'),
    ('q4', '25'): ('q1', '0'),
    ('q4', '50'): ('q3', '0'),
    ('q4', '100'): ('q4', '1')
}
estado_inicial_questao_3 = 'q0'
estados_finais_questao_3 = ['q0', 'q1', 'q2', 'q3', 'q4']
automato_questao_3 = td.Transdutor(estado_inicial_questao_3, estados_questao_3, alfabeto_entrada_questao_3, alfabeto_saida_questao_3, func_transicao_transducao, estados_finais_questao_3)

automato_questao_3.questao_3()