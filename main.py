# Bryan Gava Domingos, Inteligência Artificial Aplicada EAD

# Importa modulos utilizados
import random
import time
from collections import namedtuple
from itertools import chain

# Apresenta o jogo, programador e versão
print('')
print('ZOMBIE DICE por Bryan Gava Domingos')
print('')

# ‘Loop’ para definir quantia de jogadores (tem que ser 2 ou mais)
while True:
    try:
        numJog = int(input('Digite o numero de jogadores (mínimo de 2 jogadores): '))
        if numJog >= 2:
            break
    except ValueError:
        print('Valor inválido')

# Cria lista de jogadores com o nome(entrada) dos jogadores enumerados
jogadores = []

# Pergunta o nome dos jogadores por número
for i in range(numJog):
    nome = input(f'Nome do jogador {i + 1} :')
    # Adiciona nome escrito a posicao na listta de jogadores sequencialmente
    jogadores.append(nome)

# Tempo e linha para proximo evento para melhor visualizacao e acompanhamento do jogo
time.sleep(.5)
print('')

# Boas-vindas para 2 jogadores separando-os com 'e' ou ',' para mais jogadores
if numJog == 2:
    print('Bem vindos', ' e '.join(jogadores))
else:
    print('Bem vindos', ', '.join(jogadores))

time.sleep(1)
print('')

# Estrutura da tupla
Dado = namedtuple('Dado', {'cor', 'facies'})

# Definições para a tupla de cada dado
Verde = Dado(cor='\33[92mVerde\33[0m', facies='CPCTPC')
Amarelo = Dado(cor='\33[93mAmarelo\33[0m', facies='TPCTPC')
Vermelho = Dado(cor='\33[91mVermelho\33[0m', facies='TPTCPT')

# Tubo de dados
tubo = []
# Cópia do tubo para reseta-lo no fim de turnos
tubo_reset = []

# Adiciona os respectivos dados ao tubo e tubo_reset com a quantia correta
for i in range(6):
    tubo.append(Verde)
    tubo_reset.append(Verde)
for i in range(4):
    tubo.append(Amarelo)
    tubo_reset.append(Amarelo)
for i in range(3):
    tubo.append(Vermelho)
    tubo_reset.append(Vermelho)

# Define turno para determinar vez do jogador a partir da lista de jogadores
turno = 0

# Cria lista de zeros representando o placar inicial de cerebros para cada jogador no comprimento da lista de jogadores
totalcerebros = [0] * len(jogadores)

# Cerebros em risco para pontuacao para deixar na memoria caso continue turnos
cerebro_em_risco = 0

# Contabiliza o total de tiros tomados caso continue turnos
totaltiros = 0

# Direciona o ‘loop’ para jogar novamente dados que caem com facie 'passos'
fugitivos = 0

# Trigger de fim de jogo
fim = 0

# Dados passos guardados para serem jogados na proxima rodada
passos = []

# Definições fora do 'loop' para valores não ficarem indefinidos
facies = ()
removedor = ()
restantes = ()

# ‘Loop’ de turno (numero do turno ditará numero do jogador)
while True:

    # Reseta valores de cada rodada
    tiro = 0
    passo = 0
    cerebro_rodada = 0

    # Apresenta o placar de cerebros atual no início de cada rodada conforme a separacao utilizada mediante a quantia
    # de jogadores
    print('')
    print('╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗')
    print('')
    if numJog == 2:
        print('Placar atual de', ' e '.join(jogadores), ':', totalcerebros,
              'cérebro(s) devorado(s)!')
        print('')
        print(jogadores[turno], 'tem [', cerebro_em_risco,
              '] cérebro(s) a pontuar.')
    else:
        print('Placar atual de', ' , '.join(jogadores), ':', totalcerebros,
              'cérebro(s) devorado(s)!')
        print('')
        print(jogadores[turno], 'tem [', cerebro_em_risco,
              '] cérebro(s) a pontuar.')
    print('')
    print('╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝')
    print('')

    time.sleep(2)

    # Informa o jogador da vez conforme o número do turno em relacao a lista de jogadores
    print('Vez de', jogadores[turno], )
    time.sleep(2)
    print('')

    # Embaralha a lista
    random.shuffle(tubo)

    tubo.reverse()

    # Requer entrada do jogador para melhor acompanhamento do jogo
    input('Pressione \33[94mEnter\33[0m para tirar seus dados')

    # ‘Loop’ sem dados a serem lancados novamente
    if fugitivos == 0:

        # Escolhe tres dados aleatorios do tubo
        tres_dados = random.choices(tubo, k=3)

        # Função que remove dados escolhidos do tubo
        def removedor(lista_de_dados, lista_tubo):
            for dados_ in lista_de_dados:
                if dados_ in tubo:
                    lista_tubo.remove(dados_)

        removedor(tres_dados, tubo)

        print('')
        print('')
        # Informa ao jogador a cor de cada dado retirado do tubo
        print('Você tirou os seguintes dados: ', tres_dados[0].cor, ', ', tres_dados[1].cor, ' e ', tres_dados[2].cor)
        time.sleep(2.5)
        print('')
        print('')

        # Função para mostrar dados restantes no tubo
        def restantes():
            for d in range(len(tubo)):
                print(tubo[d].cor, end='   ')
            time.sleep(1.5)

        # Apresenta ao jogador os dados restantes no tubo
        print('Os dados restantes no tubo são: ')
        print('')
        restantes()
        print('')
        print('')
        print('')

        # Entrada do jogador para rolar os dados
        input('Pressione \33[94mEnter\33[0m para rolar os dados')
        print('')
        print('')

        # Escolhe aleatoriamente uma letra de cada sequência contida na lista 'tres_dados'
        facie1 = random.choice(tres_dados[0].facies)
        facie2 = random.choice(tres_dados[1].facies)
        facie3 = random.choice(tres_dados[2].facies)

        # Função para modificar as variáveis conforme o que foi sorteado
        def facies(faciex, parapassos):
            # Se a letra da facie for 'P'
            if faciex == 'P':
                # Adiciona a sequência (cor) do dado que caiu 'Passos' para se jogado novamente
                passos.append(parapassos)
                # Adiciona 1 a variavel 'fugitivos' para direcionar o ‘loop’ ao ‘loop’ onde ha dados a serem lançados
                # novamente
                global fugitivos
                fugitivos += 1
                # Adiciona passo para ser informado na rodada
                global passo
                passo += 1
            # Se letra da facie for 'C'
            elif faciex == 'C':
                # Adiciona 1 a lista de cerebros da rodada
                global cerebro_rodada
                cerebro_rodada += 1
            # Se facie for outra, no caso 'T'
            else:
                # Adiciona 1 a lista de tiros acumulados
                global totaltiros
                totaltiros += 1
                # Adiciona tiro para ser informado na rodada
                global tiro
                tiro += 1


        # Modifica as variáveis conforme o que foi sorteado
        facies(facie1, tres_dados[0])
        facies(facie2, tres_dados[1])
        facies(facie3, tres_dados[2])

    # Ocorre caso no ‘loop’ anterior algum dado ou dados tenham caido com a facie 'P', desta forma adicionando 1 ao
    # valor de 'fugitivos'
    elif fugitivos >= 1:

        # Escolhe 2 dados aleatorios do tubo
        tres_dados2 = random.choices(tubo, k=2)
        # Junta os dados guardados do turno anterior na lista 'passos' na posicao 0 ou 0 e 1 com os novos aleatorios
        # (2, pois pode ter apenas 1 do anterior)
        passos_dados = list(chain(passos, tres_dados2))
        # Limita o comprimento da lista para 3 dados
        passos_dados = passos_dados[:3]

        # Lista criada somente para remover o(s) novo(s) dado(s) aleatorio(s) realmente utilizados no lancamento
        remover = []
        # Copia da lista de 3 dados a serem jogados (passos_dados)
        remover.extend(passos_dados)

        # Copia lista 'passos' para apresentar os dados, pois ela sera resetada ao remover dados do tubo
        num_passos = []
        num_passos.extend(passos)

        # Remove itens da lista 'remover' conforme a qunantia de 'passos' da rodada anteriror para nao removelos do
        # tubo novamente
        for i in range(len(passos)):
            remover.pop(0)

        # Remove do tubo dados da lista remover processada com o comprimento da lista passos
        removedor(remover, tubo)

        print('')
        print('')

        # Informa os dados a serem rolados e o(s) dado(s) sendo rolados novamente com a devida separacao
        # Se houver apenas 1 dado sendo jogado novamente
        for i in range(len(passos_dados)):
            if len(num_passos) == 1:
                print('Você tirou os seguintes dados: ', passos_dados[0].cor, ', ', passos_dados[1].cor, ' e ',
                      passos_dados[2].cor, ', sendo', num_passos[0].cor,
                      'um dado do turno anterior')
                break
            # Se houverem 2 dados sendo jogados novamente
            elif len(num_passos) == 2:
                print('Você tirou os seguintes dados: ', passos_dados[0].cor, ', ', passos_dados[1].cor, ' e ',
                      passos_dados[2].cor, ', sendo', num_passos[0].cor, ' e ',
                      num_passos[1].cor, 'dados do turno anterior')
                break
            # Se houverem 3 dados sendo jogados novamente
            elif len(num_passos) == 3:
                print('Você tirou os seguintes dados: ', num_passos[0].cor, ', ', num_passos[1].cor, ' e ',
                      num_passos[2].cor, ', sendo todos dados do turno anterior')
                break

        time.sleep(2.5)
        print('')
        print('')

        # Apresenta ao jogador os dados restantes no tubo
        print('Os dados restantes no tubo são: ')
        print('')
        restantes()
        print('')
        print('')
        print('')

        input('Pressione \33[94mEnter\33[0m para rolar os dados')
        print('')
        print('')

        # Escolhe aleatoriamente uma letra de cada sequência contida na lista
        facie1 = random.choice(passos_dados[0].facies)
        facie2 = random.choice(passos_dados[1].facies)
        facie3 = random.choice(passos_dados[2].facies)

        # Zera a variavel 'fugitivos' caso o próximo lançamento não tenha 'P'
        fugitivos = 0
        # Reseta (lista) 'passos' para próxima rodadada
        passos.clear()

        # Modifica as variáveis conforme o que foi sorteado
        facies(facie1, passos_dados[0])
        facies(facie2, passos_dados[1])
        facies(facie3, passos_dados[2])

    # -----------------------------------------------------------------------------------------------------------------

    # Informa ao jogador a facie de cada dado retirado do tubo atravez das variaveis coletadas na rodada
    time.sleep(.5)
    print('Você comeu', cerebro_rodada, 'cérebro(s)')
    time.sleep(.5)
    print('')
    print('Você levou', tiro, 'tiro(s)')
    time.sleep(.5)
    print('')
    print('Você teve', passo, 'fugitivo(s)')
    time.sleep(1.5)
    print('')
    print('')

    # Possiveis desfechos da rodada
    while True:

        def reset():
            # Perde os cerebros acumulados
            global cerebro_em_risco
            cerebro_em_risco = 0
            # Reseta total de tiros para a proxima rodada
            global totaltiros
            totaltiros = 0
            # Transforma a lista tubo modificada numa (lista) tubo original
            global tubo
            tubo = tubo_reset[:]
            # Variavel fugitivos zerada
            global fugitivos
            fugitivos = 0
            # Lista 'passos' contendo dados ja removidos do tubo limpa
            global passos
            passos.clear()


        # Determina fim da rodada de um jogador por levar 3 tiros ou mais
        if totaltiros >= 3:
            print(jogadores[turno], 'levou', totaltiros, 'tiros e foi abatido(a)! Não pontuou.')
            time.sleep(2)
            # Repeticao do turno dos jogadores (nao permite que o número de turnos extrapole o comprimento da lista
            # de jogadores)
            if turno == len(jogadores) - 1:
                # Volta ao primeiro turno (0) ao passar a vez no ultimo turno e reseta valores para a proxima rodada
                turno = 0
                # Função que reseta diversos valores
                reset()
                break
            # Quando jogador nao é o último da lista de jogadores
            else:
                # Adiciona 1 ao turno, assim mudando o ‘loop’ para ocorrer para o proximo jogador na lista de jogadores
                turno += 1
                # Função que reseta diversos valores
                reset()
                break
        # Determina vitoria de um jogador se o seu placar passar ≥ 13 durante a contagem
        elif totalcerebros[turno] + cerebro_em_risco + cerebro_rodada >= 13:
            print('Você devorou 13 cérebros e venceu! Parabéns', jogadores[turno], '!')
            # Adiciona valor ao gatilho 'fim' para efetuar nova pergunta
            fim += 1
            time.sleep(2)
            break

        # Informa ao jogador o total de tiros que ele ja levou durante todas as rodadas seguidas que jogou
        # Se levou nenhum tiro
        if totaltiros == 0:
            print('Você não levou nenhum tiro!')
            # Se levou 1 tiro
        elif totaltiros == 1:
            print('Você já foi baleado', totaltiros, 'vez!')
            # Se levou 2 tiros
        elif totaltiros == 2:
            print('Cuidado! Você já foi baleado', totaltiros, 'vezes!')
            # Se levou 3 ou mais tiros
        else:
            print('Você foi baleado', totaltiros, 'vezes!')

        time.sleep(1.5)
        print('')
        print('')

        # Avisa o jogador que ele possui cerebros ainda nao pontuados
        if cerebro_rodada >= 1:
            print('Você tem', cerebro_em_risco + cerebro_rodada,
                  'cérebro(s) acumulado(s). Passe sua vez antes de levar 3 tiros para pontuar.')
        elif cerebro_em_risco >= 1 and cerebro_rodada == 0:
            print('Você tem', cerebro_em_risco,
                  'cérebro(s) acumulado(s). Passe sua vez antes de levar 3 tiros para pontuar.')
        else:
            print('Você ainda não devourou nenhum cérebro.')

        time.sleep(2)
        print('')
        print('')

        # Coloca os dados de volta no tubo se não tiver dados suficientes no tubo para completar a mão
        if len(tubo) + len(passos) < 3:
            # Transforma a lista tubo modificada numa (lista) tubo original
            tubo = tubo_reset[:]
            print('Não há dados suficientes no tubo, você colocou dados devolta no tubo')
            # Não adiciona os dados na mão devolta ao tubo
            for i in range(len(passos)):
                tubo.remove(passos[0])
            time.sleep(2)
            print('')

        # Caso o jogador nao tenha sido abatido, pergunta se deseja continuar o seu turno ou passar a vez
        pergunta = input('Você deseja jogar mais um turno? s/n: ')
        if pergunta == 's':
            # Adiciona cerebros da rodada para uma lista cerebros em risco para ser pontuada somente ao passar a vez
            # em proximas oportunidades
            cerebro_em_risco += cerebro_rodada
            # Mantem o turno atual
            turno += 0
            # Termina loop
            break
        # Se a resposta for nao
        elif pergunta == 'n':
            # Repeticao do turno dos jogadores (nao permite que o número de turnos extrapole o comprimento da lista
            # de jogadores)
            if turno == len(jogadores) - 1:
                # Adiciona cerebros da rodada aos cerebros em risco
                cerebro_em_risco += cerebro_rodada
                # Adiciona valor de todos os cerebros obtidos na(s) rodada(s) para a lista de placar total na posicao
                # do turno do jogador
                totalcerebros[turno] += cerebro_em_risco
                # Volta ao turno zero(1) ao passar a vez no último turno possivel e reseta valores para a proxima rodada
                turno = 0
                # Função que reseta diversos valores
                reset()
                break
            # Se o jogador nao for o último da lista de jogadores
            else:
                # Adiciona cerebros da rodada aos cerebros em risco
                cerebro_em_risco += cerebro_rodada
                # Adiciona valor de todos os cerebros obtidos na(s) rodada(s) para a lista de placar total na posição
                # do turno do jogador
                totalcerebros[turno] += cerebro_em_risco
                # Muda turno
                turno += 1
                # Função que reseta diversos valores
                reset()
                break

    # Ocorre caso um jogador ganhe a partida
    if fim == 1:
        print('')
        print('')

        while True:
            # Pergunta se desejam jogar novamente
            pergunta2 = input('Desejam jogar novamente? s/n')
            if pergunta2 == 's':
                # Reseta placar conforme o comprimento dos jogadores
                totalcerebros = [0] * len(jogadores)
                # Zera turno para comecar do inicio
                turno = 0
                # Função que reseta diversos valores
                reset()
                # Se o número de jogadores for 2, utiliza 'e' para separalos
                if numJog == 2:
                    print('')
                    print('')
                    print('Boa sorte', ' e '.join(jogadores))
                # Se o número de jogadores for maior que 2, utiliza ',' para separalos
                else:
                    print('')
                    print('')
                    print('Boa sorte', ', '.join(jogadores))

                # Detarmina que o fim do jogo nao ocorreu a retornar o valor para 0
                fim -= 1
                # Termina o loop
                break
            # Caso os jogadores nao desejarem jogar mais uma partida
            elif pergunta2 == 'n':
                # Determina que o fim do jogo ocorreu ao transformar o valor de 'fim' em 2
                fim += 1
                break

    # Determina fim do jogo quando fim(0) + vitoria de jogador(1) + resposta nao(1) = 2
    if fim == 2:
        print('')
        print('')
        print('FIM DE JOGO')
        # Encerra o loop/jogo
        break
