import time
import sys
import os
import webbrowser
import hashlib
from colorama import Fore, Style, init

init(autoreset=True)

# ──────────────────────────────────────────────
# Utilitários
# ──────────────────────────────────────────────

def digitar_pausado(texto, atraso=0.0005, cor=""):
    sys.stdout.write(cor)
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(atraso)
    sys.stdout.write(Style.RESET_ALL)
    print()


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def cabecalho(titulo):
    print(Fore.GREEN + Style.BRIGHT + "=" * 60)
    print(Fore.GREEN + Style.BRIGHT + titulo.center(60))
    print(Fore.GREEN + Style.BRIGHT + "=" * 60)
    print()


def separador():
    print(Fore.GREEN + "-" * 60)


# ──────────────────────────────────────────────
# FASE 1 — Identificação Hexadecimal
# ──────────────────────────────────────────────

def fase_1():
    limpar_tela()
    cabecalho("SISTEMA OPERACIONAL VANCE - VERSÃO 1.0.4 - 1987")

    digitar_pausado("Conectando ao terminal de fósforo verde...", cor=Fore.GREEN)
    time.sleep(1)
    digitar_pausado("Acesso físico detectado no Laboratório Particular.", cor=Fore.GREEN)
    time.sleep(1)

    narrativa = (
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
    digitar_pausado(narrativa, cor=Fore.WHITE)
    digitar_pausado(
        "A base de tudo é a memória. Identifique-se para iniciar o protocolo.",
        cor=Fore.YELLOW
    )

    print()
    separador()
    print(Fore.CYAN + "SEQUÊNCIA DE BYTES DETECTADA NO BUFFER DE ENTRADA:")
    print(Fore.WHITE + Style.BRIGHT + "41  52  49  41  44  4e  45")
    separador()
    print()

    tentativas = 0
    while True:
        print(Fore.GREEN + "VANCE_OS > ", end="")
        entrada = input().strip().upper()

        if entrada == "ARIADNE":
            print()
            digitar_pausado(">>> PROCESSANDO IDENTIFICAÇÃO...", atraso=0.1, cor=Fore.GREEN)
            time.sleep(1)
            print(Fore.GREEN + "[ OK ] IDENTIDADE RECONHECIDA.")
            time.sleep(0.5)
            print(Fore.GREEN + "[ OK ] SINCRONIZANDO HERANÇA DE DADOS.")
            time.sleep(0.5)
            print()
            print(Fore.CYAN + Style.BRIGHT + "*" * 60)
            digitar_pausado("BEM-VINDA DE VOLTA, ARIADNE.", cor=Fore.CYAN)
            digitar_pausado("O acesso ao Nível 2 foi liberado no servidor local.", cor=Fore.CYAN)
            print(Fore.CYAN + Style.BRIGHT + "*" * 60)
            print()
            print(Fore.WHITE + "Anote este nome. Você precisará dele para o filtro de integridade.")
            break
        else:
            tentativas += 1
            digitar_pausado(">>> PROCESSANDO IDENTIFICAÇÃO...", atraso=0.1, cor=Fore.GREEN)
            time.sleep(1)
            print(Fore.RED + ">>> ACESSO NEGADO: IDENTIFICAÇÃO INVÁLIDA.")
            if tentativas >= 3:
                print(Fore.RED + Style.DIM +
                      "DICA: O sistema fala em hexadecimal. A Tabela ASCII é a sua chave.")
            print()


# ──────────────────────────────────────────────
# PONTE — Link para Fase 2 + validação do código
# ──────────────────────────────────────────────

def ponte_fase_2():
    """Exibe o link local para fase2.html, abre no navegador e valida o código de retorno."""

    # Caminho absoluto relativo ao próprio script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fase2_path = os.path.join(script_dir, "fase2.html")
    url_local = "file:///" + fase2_path.replace("\\", "/")

    time.sleep(0.5)
    separador()
    print(Fore.CYAN + Style.BRIGHT + " >>> SERVIDOR LOCAL DETECTADO — FASE 2 DISPONÍVEL")
    separador()
    print()
    digitar_pausado(
        "Um servidor de arquivos pessoais foi localizado na rede interna.",
        atraso=0.04, cor=Fore.WHITE
    )
    digitar_pausado(
        "Acesse o endereço abaixo para encontrar o próximo enigma:",
        atraso=0.04, cor=Fore.WHITE
    )
    print()
    print(Fore.CYAN + Style.BRIGHT + "  " + url_local)
    print()
    print(Fore.YELLOW + "  [ Arquivo local — sem necessidade de internet ]")
    print()

    # Countdown de 20 segundos antes de abrir o navegador
    print(Fore.GREEN + "-" * 60)
    digitar_pausado(
        ">>> INICIALIZANDO PROTOCOLO DE ACESSO...",
        atraso=0.05, cor=Fore.GREEN
    )
    print(Fore.WHITE + "    O navegador será aberto automaticamente em:")
    print()

    CONTAGEM = 20
    for i in range(CONTAGEM, 0, -1):
        # Apaga a linha anterior e reescreve o contador
        sys.stdout.write(
            Fore.CYAN + Style.BRIGHT +
            f"\r    [ {i:02d} ] segundos..." +
            Style.RESET_ALL
        )
        sys.stdout.flush()
        time.sleep(1)

    # Limpa a linha do contador e confirma
    sys.stdout.write("\r" + " " * 40 + "\r")
    sys.stdout.flush()
    print(Fore.GREEN + "    [ 00 ] — ACESSO LIBERADO.")
    print(Fore.GREEN + "-" * 60)
    print()

    # Abre automaticamente no navegador padrão
    try:
        webbrowser.open(url_local)
        digitar_pausado(">>> Abrindo navegador automaticamente...", atraso=0.05, cor=Fore.GREEN)
    except Exception:
        digitar_pausado(
            ">>> Abra o endereço acima manualmente no navegador.",
            atraso=0.05, cor=Fore.YELLOW
        )

    print()
    separador()
    print(Fore.WHITE + " Resolva o enigma no site e obtenha o CÓDIGO DE SISTEMA.")
    print(Fore.WHITE + " Quando tiver o código, volte aqui e insira abaixo.")
    separador()
    print()

    # Valida via hash SHA-256 — não expõe o código em texto puro no fonte
    HASH_CORRETO = hashlib.sha256("SYSTEM_OVERRIDE_09X".encode()).hexdigest()

    tentativas = 0
    while True:
        print(Fore.GREEN + "VANCE_OS [CÓDIGO FASE 2] > ", end="")
        entrada = input().strip().upper()

        hash_entrada = hashlib.sha256(entrada.encode()).hexdigest()

        if hash_entrada == HASH_CORRETO:
            print()
            digitar_pausado(">>> VALIDANDO CÓDIGO DE SISTEMA...", atraso=0.08, cor=Fore.GREEN)
            time.sleep(1.2)
            print(Fore.GREEN + "[ OK ] CÓDIGO ACEITO: SYSTEM_OVERRIDE_09X")
            time.sleep(0.5)
            print(Fore.GREEN + "[ OK ] OVERRIDE AUTORIZADO.")
            time.sleep(0.5)
            print(Fore.GREEN + "[ OK ] ACESSO AO MÓDULO DE INTEGRIDADE LIBERADO.")
            time.sleep(0.8)
            print()
            print(Fore.CYAN + Style.BRIGHT + "*" * 60)
            digitar_pausado(
                "FASE 2 CONCLUÍDA. CARREGANDO MÓDULO DE INTEGRIDADE...",
                atraso=0.06, cor=Fore.CYAN
            )
            print(Fore.CYAN + Style.BRIGHT + "*" * 60)
            print()
            time.sleep(1)
            break
        else:
            tentativas += 1
            digitar_pausado(">>> VALIDANDO CÓDIGO DE SISTEMA...", atraso=0.08, cor=Fore.GREEN)
            time.sleep(1)
            print(Fore.RED + f">>> CÓDIGO INVÁLIDO. [TENTATIVA {tentativas}]")
            if tentativas >= 3:
                print(Fore.RED + Style.DIM +
                      "DICA: O código é gerado pelo site da Fase 2 ao inserir a senha correta.")
            print()


# ──────────────────────────────────────────────
# FASE 3 — Linhagem de Sophie Germain
# ──────────────────────────────────────────────

def fase_3():
    limpar_tela()
    cabecalho("SISTEMA OPERACIONAL VANCE - MÓDULO DE INTEGRIDADE v3.0")

    digitar_pausado("Conexão com Setor 4 iniciada...", cor=Fore.GREEN)
    time.sleep(0.8)
    digitar_pausado("Firewall de integridade detectado. Aguardando checksum...", cor=Fore.GREEN)
    time.sleep(1)

    narrativa_fase3 = (
        "\nRELATÓRIO DE INVESTIGAÇÃO - CASO VANCE - DIA 185.\n\n"
        "O acesso ao Setor 4 está protegido por um firewall que\n"
        "só aceita pacotes de dados específicos. Uma nota gravada\n"
        "no código-fonte do servidor diz o seguinte:\n"
    )
    digitar_pausado(narrativa_fase3, cor=Fore.WHITE)
    time.sleep(0.5)

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

    digitar_pausado(">>> PROTOCOLO DE GERMAIN CARREGADO.", atraso=0.06, cor=Fore.CYAN)
    time.sleep(0.5)
    print()
    separador()
    print(Fore.CYAN + Style.BRIGHT + " REGRA DE VALIDAÇÃO — LINHAGEM DE SOPHIE GERMAIN")
    separador()

    regra = (
        "\n Um número p pertence à Linhagem se atender às duas\n"
        " condições SIMULTÂNEAS:\n\n"
        "   [1]  p       deve ser um número PRIMO.\n"
        "   [2]  2p + 1  também deve ser um número PRIMO.\n\n"
        " SUA MISSÃO:\n"
        "   Escreva um programa em C ou Python que percorra o\n"
        "   intervalo de 1 a 10.000, identifique todos os números\n"
        "   que seguem essa regra e calcule a SOMA TOTAL deles.\n"
        "   Em seguida, insira o resultado neste terminal.\n"
    )
    digitar_pausado(regra, atraso=0.02, cor=Fore.WHITE)

    separador()
    print(Fore.YELLOW + Style.BRIGHT + " >>> DICA DO SISTEMA:")
    dica = (
        " Para verificar se um número é primo, basta testar os\n"
        " divisores entre 2 e a RAIZ QUADRADA do número.\n"
        " Qualquer divisor encontrado nesse intervalo já descarta\n"
        " o candidato — não é necessário ir além disso.\n"
    )
    digitar_pausado(dica, atraso=0.02, cor=Fore.YELLOW)
    separador()
    print()
    print(Fore.WHITE + " Abra o VSCode, escreva seu programa e rode-o.")
    print(Fore.WHITE + " Quando obtiver o resultado, volte aqui e insira o checksum.")
    print()

    CHECKSUM_CORRETO = 771483
    tentativas = 0

    while True:
        print(Fore.GREEN + "VANCE_OS [CHECKSUM] > ", end="")
        entrada = input().strip().replace(".", "").replace(",", "").replace(" ", "")

        try:
            valor = int(entrada)
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
            digitar_pausado(
                "O resultado aponta para o  >>  SETOR 4  <<",
                atraso=0.07, cor=Fore.CYAN
            )
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
            print(Fore.YELLOW + Style.BRIGHT + "[ FASE 3 CONCLUÍDA ] Avance para a Fase 4.")
            print()
            break
        else:
            tentativas += 1
            digitar_pausado(">>> PROCESSANDO CHECKSUM...", atraso=0.08, cor=Fore.GREEN)
            time.sleep(1)
            print(Fore.RED + f">>> CHECKSUM INVÁLIDO. [TENTATIVA {tentativas}]")
            if tentativas >= 3:
                print(Fore.RED + Style.DIM +
                      "DICA: Revise a lógica de filtragem — ambas as condições\n"
                      "      (p primo E 2p+1 primo) devem ser verdadeiras ao mesmo tempo.")
            print()


# ──────────────────────────────────────────────
# Ponto de entrada
# ──────────────────────────────────────────────

if __name__ == "__main__":
    try:
        fase_1()        # Hex → ARIADNE
        ponte_fase_2()  # Abre fase2.html → valida SYSTEM_OVERRIDE_09X
        fase_3()        # Sophie Germain → 771483
    except KeyboardInterrupt:
        print(Fore.RED + "\n\nConexão abortada pelo usuário.")
