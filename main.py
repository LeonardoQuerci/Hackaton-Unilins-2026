import time
import sys
import os
from colorama import Fore, Style, init


def digitar_pausado(texto, atraso=0.05, cor=""):
    sys.stdout.write(cor)
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(atraso)
    sys.stdout.write(Style.RESET_ALL)
    print()


def limpar_tela():
    """Limpa o terminal dependendo do Sistema Operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')

def fase_1():
    limpar_tela()
    
    # Cabeçalho de imersão
    print(Fore.GREEN + Style.BRIGHT + "="*60)
    print(Fore.GREEN + Style.BRIGHT + "SISTEMA OPERACIONAL VANCE - VERSÃO 1.0.4 - 1987")
    print(Fore.GREEN + Style.BRIGHT + "="*60)
    print("\n")

    # Storytelling
    digitar_pausado("Conectando ao terminal de fósforo verde...",cor=Fore.GREEN)
    time.sleep(1)
    digitar_pausado("Acesso físico detectado no Laboratório Particular.", cor=Fore.GREEN)
    time.sleep(1)
    narrativa_detetive = (
        "\nRELATÓRIO DE INVESTIGAÇÃO - CASO VANCE - DIA 184.\n"
        "As pistas esfriaram, a polícia desistiu, mas você não.\n"
        "Você é o último detetive que acredita que o Dr. Alistair Vance\n"
        "não 'desapareceu' simplesmente. Um gênio da criptografia não\n"
        "deixa sua vida para trás sem um plano.\n\n"
        "As lendas sobre Vance dizem que ele estava à beira de uma\n"
        "descoberta que mudaria a segurança digital global. Seus e-mails\n"
        "interceptados falavam de 'uma herança que deve ser protegida'.\n"
        "Mas protegida de quem? E para quem?\n\n"
        "Suas buscas te levaram a este laboratório esquecido. O ar está\n"
        "pesado com o cheiro de ozônio e segredos. Diante de você,\n"
        "um terminal antigo, o coração pulsante do legado de Vance.\n"
        "Para descobrir a verdade sobre seu desaparecimento, você\n"
        "precisa pensar como ele. A primeira barreira está à sua frente."
    )

    digitar_pausado(narrativa_detetive, cor=Fore.WHITE)
    digitar_pausado("A base de tudo é a memória. Identifique-se para iniciar o protocolo.", cor=Fore.YELLOW)
    
    print("\n" + Fore.GREEN + Style.BRIGHT + "-"*60)
    print(Fore.CYAN + "SEQUÊNCIA DE BYTES DETECTADA NO BUFFER DE ENTRADA:")
    print(Fore.WHITE + Style.BRIGHT + "41  52  49  41  44  4e  45")
    print(Fore.GREEN + "-"*60 + "\n")
    sys.stdout.write(Style.RESET_ALL)

    # Lógica de validação
    tentativas = 0
    while True:
        # O prompt de comando
        print(Fore.GREEN + "VANCE_OS > ", end="")
        entrada = input().strip().upper()

        if entrada == "ARIADNE":
            print("\n")
            digitar_pausado(">>> PROCESSANDO IDENTIFICAÇÃO...", atraso=0.1, cor=Fore.GREEN)
            time.sleep(1)
            print(Fore.GREEN + "[ OK ] IDENTIDADE RECONHECIDA.")
            time.sleep(0.5)
            print(Fore.GREEN + "[ OK ] SINCRONIZANDO HERANÇA DE DADOS.")
            time.sleep(0.5)
            
            print("\n" + Fore.CYAN + "*"*60)
            digitar_pausado("BEM-VINDA DE VOLTA, ARIADNE.", cor=Fore.CYAN)
            digitar_pausado("O acesso ao Nível 2 foi liberado no servidor local.", cor=Fore.CYAN)
            print(Fore.CYAN + "*"*60)
            
            print("\n" + Fore.WHITE + "Anote este nome. Você precisará dele para o filtro de integridade.")
            print(Fore.YELLOW + "Pressione ENTER para encerrar a conexão e avançar para a Fase 2...")
            input()
            break
        else:
            tentativas += 1
            digitar_pausado(">>> PROCESSANDO IDENTIFICAÇÃO...", atraso=0.1, cor=Fore.GREEN)
            time.sleep(1)
            print(Fore.RED + ">>> ACESSO NEGADO: IDENTIFICAÇÃO INVÁLIDA.")
            if tentativas >= 3:
                print(Fore.RED + Style.DIM + "DICA: O sistema fala em hexadecimal. A Tabela ASCII é a sua chave.")
                sys.stdout.write(Style.RESET_ALL)
            print("\n")

def fase_3():
    limpar_tela()

    # Cabeçalho
    print(Fore.GREEN + Style.BRIGHT + "=" * 60)
    print(Fore.GREEN + Style.BRIGHT + "SISTEMA OPERACIONAL VANCE - MÓDULO DE INTEGRIDADE v3.0")
    print(Fore.GREEN + Style.BRIGHT + "=" * 60)
    print()

    digitar_pausado("Conexão com Setor 4 iniciada...", cor=Fore.GREEN)
    time.sleep(0.8)
    digitar_pausado("Firewall de integridade detectado. Aguardando checksum...", cor=Fore.GREEN)
    time.sleep(1)

    # Narrativa
    narrativa_fase3 = (
        "\nRELATÓRIO DE INVESTIGAÇÃO - CASO VANCE - DIA 185.\n\n"
        "O acesso ao Setor 4 está protegido por um firewall que\n"
        "só aceita pacotes de dados específicos. Uma nota gravada\n"
        "no código-fonte do servidor diz o seguinte:\n"
    )
    digitar_pausado(narrativa_fase3, cor=Fore.WHITE)
    time.sleep(0.5)

    # Citação de Vance
    print(Fore.YELLOW + Style.BRIGHT + "  " + "~" * 56)
    citacao = (
        "  \"O ruído no sistema é imenso. Para encontrar a verdade,\n"
        "  você deve filtrar apenas o que é puro por natureza —\n"
        "  e capaz de gerar outra pureza. No intervalo de 1 a 10.000,\n"
        "  identifique os números que pertencem à Linhagem de\n"
        "  Sophie Germain e some todos eles.\"\n"
        "                                        — Dr. Alistair Vance"
    )
    digitar_pausado(citacao, atraso=0.03, cor=Fore.YELLOW)
    print(Fore.YELLOW + Style.BRIGHT + "  " + "~" * 56)
    print()
    time.sleep(1)

    # Enunciado técnico
    digitar_pausado(">>> PROTOCOLO DE GERMAIN CARREGADO.", atraso=0.06, cor=Fore.CYAN)
    time.sleep(0.5)
    print()
    print(Fore.GREEN + "-" * 60)
    print(Fore.CYAN + Style.BRIGHT + " REGRA DE VALIDAÇÃO — LINHAGEM DE SOPHIE GERMAIN")
    print(Fore.GREEN + "-" * 60)

    regra = (
        "\n Um número p pertence à Linhagem se atender às duas\n"
        " condições SIMULTÂNEAS:\n\n"
        "   [1]  p  deve ser um número PRIMO.\n"
        "   [2]  2p + 1  também deve ser um número PRIMO.\n\n"
        " SUA MISSÃO:\n"
        "   Escreva um programa em C ou Python que percorra o\n"
        "   intervalo de 1 a 10.000, identifique todos os números\n"
        "   que seguem essa regra e calcule a SOMA TOTAL deles.\n"
        "   Em seguida, insira o resultado neste terminal.\n"
    )
    digitar_pausado(regra, atraso=0.02, cor=Fore.WHITE)

    # Dica sobre números primos
    print(Fore.GREEN + "-" * 60)
    print(Fore.YELLOW + Style.BRIGHT + " >>> DICA DO SISTEMA:")
    dica = (
        " Para verificar se um número é primo, basta testar os\n"
        " divisores entre 2 e a RAIZ QUADRADA do número.\n"
        " Qualquer divisor encontrado nesse intervalo já descarta\n"
        " o candidato — não é necessário ir além disso.\n"
    )
    digitar_pausado(dica, atraso=0.02, cor=Fore.YELLOW)
    print(Fore.GREEN + "-" * 60)
    print()

    # Aguarda o jogador abrir o VSCode e rodar o código
    print(Fore.WHITE + " Abra o VSCode, escreva seu programa e rode-o.")
    print(Fore.WHITE + " Quando obtiver o resultado, volte aqui e insira o checksum.")
    print()

    # Validação da resposta
    CHECKSUM_CORRETO = 771483
    tentativas = 0

    while True:
        print(Fore.GREEN + "VANCE_OS [CHECKSUM] > ", end="")
        entrada = input().strip()

        # Aceita com ou sem separador de milhar
        entrada_limpa = entrada.replace(".", "").replace(",", "").replace(" ", "")

        try:
            valor = int(entrada_limpa)
        except ValueError:
            print(Fore.RED + ">>> ENTRADA INVÁLIDA: insira apenas números.")
            print()
            continue

        if valor == CHECKSUM_CORRETO:
            print()
            digitar_pausado(">>> PROCESSANDO CHECKSUM...", atraso=0.08, cor=Fore.GREEN)
            time.sleep(1.2)
            print(Fore.GREEN + "[ OK ] CHECKSUM VALIDADO: " + str(CHECKSUM_CORRETO))
            time.sleep(0.6)
            print(Fore.GREEN + "[ OK ] FILTRO APLICADO. RUÍDO ELIMINADO.")
            time.sleep(0.6)
            print(Fore.GREEN + "[ OK ] INTEGRIDADE DO PACOTE CONFIRMADA.")
            time.sleep(0.8)

            print()
            print(Fore.CYAN + Style.BRIGHT + "*" * 60)
            digitar_pausado("O resultado aponta para o  >>  SETOR 4  <<", atraso=0.07, cor=Fore.CYAN)
            print()
            digitar_pausado(
                "A segunda coordenada do legado de Vance foi revelada.",
                atraso=0.05, cor=Fore.WHITE
            )
            digitar_pausado(
                "O Setor 4 aguarda. A verdade está mais perto do que nunca.",
                atraso=0.05, cor=Fore.WHITE
            )
            print(Fore.CYAN + Style.BRIGHT + "*" * 60)
            print()
            print(Fore.YELLOW + "[ FASE 3 CONCLUÍDA ] Avance para a Fase 4.")
            print()
            break

        else:
            tentativas += 1
            digitar_pausado(">>> PROCESSANDO CHECKSUM...", atraso=0.08, cor=Fore.GREEN)
            time.sleep(1)
            print(Fore.RED + f">>> CHECKSUM INVÁLIDO. [TENTATIVA {tentativas}]")
            if tentativas >= 3:
                print(
                    Fore.RED + Style.DIM +
                    "DICA: Revise a lógica de filtragem — ambas as condições\n"
                    "      (p primo E 2p+1 primo) devem ser verdadeiras ao mesmo tempo."
                )
            print()


if __name__ == "__main__":
    try:
        fase_1()
        fase_3()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\nConexão abortada pelo usuário.")