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

def limpar_stdin():
    """Descarta tudo que foi digitado enquanto o terminal estava escrevendo.

    Windows : lê e descarta todos os caracteres pendentes via msvcrt.
    Linux/Mac: substitui o buffer do stdin por uma cópia zerada via termios.
    Sem esse flush, teclas pressionadas durante as animações são
    capturadas pelo próximo input() e executadas como resposta.
    """
    if os.name == 'nt':
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getwch()


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
        limpar_stdin()
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
        limpar_stdin()
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
    # print(Fore.YELLOW + Style.BRIGHT + " >>> DICA DO SISTEMA:")
    # dica = (
    #     " Para identificar um número primo, basta testar se ele\n"
    #     " é divisível por algum número entre 2 e o valor de sua RAÍZ QUADRADA.\n"
    #     " Se ele não for divisível, então será primo.\n"
    # )

    CHECKSUM_CORRETO = 771483
    tentativas = 0

    while True:
        print(Fore.GREEN + "VANCE_OS [CHECKSUM] > ", end="")
        limpar_stdin()
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
# FASE 4 — O Legado / Conversa com Vance
# ──────────────────────────────────────────────

import re as _re
import random as _random
import string as _string

_ANSI_RE = _re.compile(r'^(\x1b\[[0-9;]*m)+')

def _dp(texto, atraso=0.025, cor=""):
    """digitar_pausado local — aceita cor como prefixo."""
    sys.stdout.write(cor)
    sys.stdout.flush()
    match = _ANSI_RE.match(texto)
    if match:
        sys.stdout.write(match.group(0)); sys.stdout.flush()
        texto = texto[match.end():]
    for ch in texto:
        sys.stdout.write(ch); sys.stdout.flush(); time.sleep(atraso)
    sys.stdout.write(Style.RESET_ALL); sys.stdout.flush(); print()


def _barra(label, total=30):
    for i in range(total + 1):
        pct = int(i / total * 100)
        cor = Fore.RED if pct < 40 else Fore.YELLOW if pct < 80 else Fore.GREEN
        sys.stdout.write(
            f"\r{Fore.WHITE}{label}: {cor}[{'█'*i}{'░'*(total-i)}]"
            f"{Fore.WHITE} {pct:3d}%{Style.RESET_ALL}"
        )
        sys.stdout.flush(); time.sleep(0.05)
    print()


def _animar_fluxo(dado, duracao=6):
    ruido = _string.ascii_uppercase + "0123456789█▓▒░#@$%"
    posicoes_key = {0, 7, 14, 21, 28, 35}
    inicio = time.time()
    while time.time() - inicio < duracao:
        prog = (time.time() - inicio) / duracao
        linha = "  "
        for idx, c in enumerate(dado):
            limiar = prog * 1.5 if idx not in posicoes_key else prog * 0.9
            if _random.random() < limiar:
                cor = Fore.YELLOW + Style.BRIGHT if idx in posicoes_key else Fore.WHITE
                linha += cor + c + Style.RESET_ALL
            else:
                linha += Fore.GREEN + Style.DIM + _random.choice(ruido) + Style.RESET_ALL
        sys.stdout.write('\r' + linha + "  "); sys.stdout.flush(); time.sleep(0.055)
    linha_final = "  "
    for idx, c in enumerate(dado):
        if idx in posicoes_key:
            linha_final += Fore.YELLOW + Style.BRIGHT + c + Style.RESET_ALL
        else:
            linha_final += Fore.WHITE + Style.DIM + c + Style.RESET_ALL
    sys.stdout.write('\r' + linha_final + "\n"); sys.stdout.flush()


def _tabela_vigenere():
    """
    Tabela de Vigenère completa 26x26.
    Linhas  = letra da CHAVE (A-Z)
    Colunas = letra do TEXTO CIFRADO (A-Z)
    Célula  = texto plano = (cifrado - chave) mod 26
    Sem destaques — o jogador cruza manualmente.
    """
    alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    print(Fore.GREEN + Style.DIM + "  CHAVE\\CIF│ " + " ".join(alfa))
    print(Fore.GREEN + Style.DIM + "  ─────────┼" + "─" * 53)

    for lc in alfa:
        k = ord(lc) - ord('A')
        celulas = ""
        for lf in alfa:
            plain = chr((ord(lf) - ord('A') - k) % 26 + ord('A'))
            celulas += plain + " "
        print(Fore.GREEN + Style.DIM + f"      {lc}    │ " + celulas)
    print()


# ── Enigma (Vigenère) ─────────────────────────────────────────────────────────

def _enigma_vigenere():
    FLUXO   = "LAXMQPNVKRTHZFODCWASPAYUJXWBGNIHQEMB"
    HASH_OK = "cb765a464c8baa7ff8a6dc9bd15d1b29be6ee2b1ab48759bbacc57d3455de28a"

    limpar_tela()
    print(Fore.RED + Style.BRIGHT + "╔" + "═"*58 + "╗")
    print(Fore.RED + Style.BRIGHT + "║" + " PROTOCOLO SIGMA  ·  NÍVEL MÁXIMO  ·  ACESSO RESTRITO ".center(58) + "║")
    print(Fore.RED + Style.BRIGHT + "║" + " ARQUIVO CIFRADO  ·  AUTENTICAÇÃO FINAL               ".center(58) + "║")
    print(Fore.RED + Style.BRIGHT + "╚" + "═"*58 + "╝")
    print(); time.sleep(1.0)

    _dp(Fore.WHITE + "DIA 186. CASO VANCE. RELATÓRIO FINAL DE INVESTIGAÇÃO.")
    _dp(Fore.WHITE + "Três barreiras. Três segredos. Três vitórias.")
    time.sleep(0.6); print()
    _dp(Fore.YELLOW + "O sistema detectou um arquivo que Vance cifrou com uma")
    _dp(Fore.YELLOW + "técnica que ele jamais ensinou a ninguém — exceto a ela.")
    time.sleep(1.0); print()

    print(Fore.GREEN + "─"*60)
    _dp(Fore.CYAN + ">>> ARQUIVO LOCALIZADO  : /root/.sigma/vance_legado.enc")
    _dp(Fore.CYAN + ">>> INTEGRIDADE         : 12% — DADOS SEVERAMENTE CORROMPIDOS")
    _dp(Fore.CYAN + ">>> INICIANDO RECUPERAÇÃO FORÇADA...")
    print(); _barra("RECUPERAÇÃO DE DADOS"); print()

    print(Fore.RED + Style.BRIGHT + "═"*60)
    print(Fore.RED + Style.BRIGHT + "  FLUXO INTERCEPTADO  ·  36 BYTES  ·  ORIGEM: DESCONHECIDA")
    print(Fore.RED + Style.BRIGHT + "═"*60); print()
    _animar_fluxo(FLUXO, duracao=6); print()

    print(Fore.GREEN + "─"*60)
    print(Fore.YELLOW + Style.BRIGHT + "  FRAGMENTO RECUPERADO — ANOTAÇÃO MANUSCRITA  ·  A. VANCE")
    print(Fore.GREEN + "─"*60); print()

    for nota in [
        "  \"O que você enxerga no fluxo não é o que você procura.\"",
        "",
        "  \"Existe um ritmo neste caos — o mesmo ritmo que",
        "   sempre trouxe sorte a quem me conhece de verdade.\"",
        "",
        "  \"Siga esse ritmo. Extraia o que ele revela.",
        "   O que emergir é uma cifra — e toda cifra exige uma chave.\"",
        "",
        "  \"Minha herdeira é a chave.",
        "   Cada letra do seu nome, na sequência exata em que a conheço,",
        "   define o desvio de cada símbolo da cifra.\"",
        "",
        "  \"O que você decifrar — esse é o meu legado.\"",
        "",
        "                                              — A. Vance",
    ]:
        if nota == "": print()
        else: _dp(Fore.YELLOW + nota, atraso=0.018)
        time.sleep(0.04)
    print()

    print(Fore.GREEN + "─"*60)
    print(Fore.CYAN + Style.BRIGHT + "  CIFRA POLIALFABÉTICA  ·  TABELA DE DESVIOS DE VANCE")
    print(Fore.CYAN + Style.DIM   + "  [ LINHAS: LETRA DA CHAVE  ·  COLUNAS: TEXTO PLANO ]")
    print(Fore.CYAN + Style.DIM   + "  [ CÉLULAS EM AMARELO: PARES RELEVANTES AO FLUXO   ]")
    print(Fore.GREEN + "─"*60); print()
    _tabela_vigenere()

    print(Fore.GREEN + Style.DIM + "  >> FREQUÊNCIA DO ARQUIVO  : 7.71483 MHz")
    print(Fore.GREEN + Style.DIM + "  >> COMPRIMENTO DO FLUXO   : 36 BYTES")
    print(Fore.GREEN + Style.DIM + "  >> PROTOCOLO              : SIGMA-V  ·  CIFRA POLIALFABÉTICA")
    print(Fore.GREEN + Style.DIM + "  >> ASSINATURA             : A.V / [ARIADNE]")
    print(); time.sleep(0.8)

    print(Fore.RED + Style.BRIGHT + "  ╔══════════════════════╗")
    print(Fore.RED + Style.BRIGHT + "  ║  AUTENTICAÇÃO SIGMA  ║")
    print(Fore.RED + Style.BRIGHT + "  ╚══════════════════════╝")
    print()

    tentativas = 0
    while True:
        print(Fore.RED + Style.BRIGHT + "  SIGMA > ", end="")
        limpar_stdin()
        entrada = input().strip().upper()
        digest  = hashlib.sha256(entrada.encode()).hexdigest()
        tentativas += 1
        _dp(Fore.GREEN + "  >>> VERIFICANDO INTEGRIDADE CRIPTOGRÁFICA...", atraso=0.04)
        time.sleep(1.0)

        if digest == HASH_OK:
            print(Fore.GREEN + "  [ OK ] PALAVRA CONFIRMADA.")
            time.sleep(0.3)
            print(Fore.GREEN + "  [ OK ] ASSINATURA DE VANCE VALIDADA.")
            time.sleep(0.3)
            print(Fore.GREEN + "  [ OK ] PROTOCOLO SIGMA — SELADO.")
            time.sleep(0.8); print()
            print(Fore.CYAN + Style.BRIGHT + "  " + "═"*56)
            for l in ["  O ARQUIVO DE VANCE ESTÁ DESBLOQUEADO.",
                      "  Você encontrou o que ele protegeu por anos.",
                      "  Prepare-se. A transmissão final começa agora."]:
                _dp(Fore.CYAN + Style.BRIGHT + l, atraso=0.045); time.sleep(0.2)
            print(Fore.CYAN + Style.BRIGHT + "  " + "═"*56)
            print(); time.sleep(2.0)
            return
        else:
            print(Fore.RED + f"  >>> PALAVRA INVÁLIDA. [TENTATIVA {tentativas}]"); print()
            if tentativas == 3:
                print(Fore.RED + Style.DIM + "  DICA: Existe um ritmo escondido no fluxo.")
                print(Fore.RED + Style.DIM + "        O número da sorte define esse ritmo.")
            elif tentativas == 5:
                print(Fore.RED + Style.DIM + "  DICA: Extraia os bytes seguindo o passo correto.")
                print(Fore.RED + Style.DIM + "        O que sobrar é uma cifra polialfabética.")
            elif tentativas == 7:
                print(Fore.RED + Style.DIM + "  DICA: A herdeira de Vance é a chave da tabela.")
                print(Fore.RED + Style.DIM + "        Você já sabe o nome dela desde o início.")
            # elif tentativas >= 8:
            #     print(Fore.RED + Style.DIM + "  DICA FINAL: Passo=7 → posições 1,8,15,22,29,36 → LVOAGB")
            #     print(Fore.RED + Style.DIM + "              Chave=ARIADNE → Vigenère → ?")
            print()


# ── Conversa com Vance ────────────────────────────────────────────────────────

def _vance_digita(texto, atraso=0.09, cor=None):
    cor = cor or Fore.WHITE
    sys.stdout.write(Fore.GREEN + Style.DIM + "VANCE > " + Style.RESET_ALL)
    sys.stdout.flush(); time.sleep(0.3)
    for ch in texto:
        sys.stdout.write(cor + ch + Style.RESET_ALL); sys.stdout.flush()
        if ch in ".!?,": time.sleep(atraso * _random.uniform(2.5, 4.0))
        elif ch == " ":  time.sleep(atraso * _random.uniform(0.8, 1.4))
        else:            time.sleep(atraso * _random.uniform(0.7, 1.3))
    print()


def _vance_pensando(segundos=2.0):
    sys.stdout.write(Fore.GREEN + Style.DIM + "VANCE > " + Style.RESET_ALL)
    sys.stdout.flush()
    for _ in range(int(segundos / 0.5)):
        sys.stdout.write(Fore.WHITE + Style.DIM + "." + Style.RESET_ALL)
        sys.stdout.flush(); time.sleep(0.5)
    sys.stdout.write("\r" + " "*25 + "\r"); sys.stdout.flush()


def _conversa_vance():
    limpar_tela()

    # Cabeçalho vermelho — anomalia
    print(Fore.RED + Style.BRIGHT + "!"*60)
    print(Fore.RED + Style.BRIGHT + "  ANOMALIA DETECTADA — SINAL ATIVO NO CANAL".center(60))
    print(Fore.RED + Style.BRIGHT + "!"*60); print(); time.sleep(0.8)

    for l in ["VERIFICANDO ORIGEM DO SINAL................",
              "CANAL CRIPTOGRAFADO EM USO. AGORA..........",
              "ORIGEM: DESCONHECIDA.......................",]:
        digitar_pausado(l, atraso=0.04, cor=Fore.RED); time.sleep(0.25)

    print(); time.sleep(1.5)
    print(Fore.GREEN + "─"*60)
    print(Fore.GREEN + Style.DIM + "  [ CANAL ABERTO — TRANSMISSÃO AO VIVO ]")
    print(Fore.GREEN + "─"*60); print(); time.sleep(2.5)

    # Vance aparece
    _vance_pensando(3.5); time.sleep(0.4)
    _vance_digita("...alguem esta ai?", atraso=0.11); time.sleep(3.0)
    _vance_pensando(2.0)
    _vance_digita("nao acredito.", atraso=0.11); time.sleep(1.2)
    _vance_digita("voce decifrou o protocolo sigma.", atraso=0.09); time.sleep(2.0)
    _vance_digita("so quem entende o que eu construi chegaria ate aqui.", atraso=0.07); time.sleep(2.0)
    _vance_digita("mas preciso ter certeza de quem voce e.", atraso=0.08); time.sleep(1.5)
    _vance_digita("tres perguntas. so voce pode responder.", atraso=0.08); time.sleep(2.0)
    print()

    HASH_ARIADNE = hashlib.sha256("ARIADNE".encode()).hexdigest()
    HASH_7       = hashlib.sha256("7".encode()).hexdigest()
    HASH_CHECK   = hashlib.sha256("771483".encode()).hexdigest()

    # Pergunta 1
    _vance_digita("qual e o nome dela. o que o terminal reconheceu na primeira fase.", atraso=0.07, cor=Fore.YELLOW)
    print()
    while True:
        print(Fore.GREEN + "VOCE > ", end="")
        limpar_stdin()
        e = input().strip().upper()
        if hashlib.sha256(e.encode()).hexdigest() == HASH_ARIADNE:
            print(); _vance_pensando(3.5)
            _vance_digita("...Ariadne.", atraso=0.20); time.sleep(2.2)
            _vance_digita("minha filha.", atraso=0.14); time.sleep(1.5)
            _vance_digita("entao ela te mandou ate aqui.", atraso=0.09); time.sleep(2.5)
            break
        else:
            print(); _vance_pensando(1.5)
            _vance_digita("isso nao esta certo. pense na primeira fase.", atraso=0.07, cor=Fore.RED); print()

    # Pergunta 2
    _vance_digita("o numero. o ritmo que guiou o fluxo corrompido.", atraso=0.07, cor=Fore.YELLOW); print()
    while True:
        print(Fore.GREEN + "VOCE > ", end="")
        limpar_stdin()
        e = input().strip()
        if hashlib.sha256(e.encode()).hexdigest() == HASH_7:
            print(); _vance_pensando(2.5)
            _vance_digita("7.", atraso=0.22); time.sleep(1.8)
            _vance_digita("sempre foi o meu numero.", atraso=0.09); time.sleep(2.0)
            break
        else:
            print(); _vance_pensando(1.5)
            _vance_digita("nao. esse nao e o numero. o numero da sorte.", atraso=0.07, cor=Fore.RED); print()

    # Pergunta 3
    _vance_digita("o checksum. a soma que prova que voce entendeu a terceira fase.", atraso=0.07, cor=Fore.YELLOW); print()
    while True:
        print(Fore.GREEN + "VOCE > ", end="")
        limpar_stdin()
        e = input().strip().replace(".","").replace(",","").replace(" ","")
        if hashlib.sha256(e.encode()).hexdigest() == HASH_CHECK:
            print(); _vance_pensando(3.0)
            _vance_digita("771483.", atraso=0.16); time.sleep(1.5)
            _vance_digita("Eu estou orgulhoso.", atraso=0.08); time.sleep(2.5)
            break
        else:
            print(); _vance_pensando(1.5)
            _vance_digita("incorreto. reveja seus calculos da terceira fase.", atraso=0.07, cor=Fore.RED); print()

    # Revelação
    _vance_digita("voce passou.", atraso=0.10); time.sleep(2.0)
    _vance_digita("ha uma pessoa. o unico em quem confiei alem de Ariadne.", atraso=0.07); time.sleep(2.0)
    _vance_pensando(5.0); time.sleep(0.5)
    _vance_digita("professor santana.", atraso=0.20, cor=Fore.CYAN); time.sleep(3.5)
    _vance_digita("sala 1.", atraso=0.25, cor=Fore.CYAN); time.sleep(3.5)
    _vance_digita("ele guarda tudo. ha anos. esperando por voce.", atraso=0.09); time.sleep(2.0)
    _vance_pensando(4.0)

    # Queda do sinal + encerramento épico
    print()
    for _ in range(6):
        chars = "█▓▒░|/\\-~^#@!?"
        print(Fore.RED + Style.DIM + "  " + "".join(_random.choice(chars) for _ in range(56)))
        time.sleep(0.06)

    limpar_tela(); time.sleep(0.5)

    for l in [">>> SINAL PERDIDO.", ">>> RECONEXÃO FALHOU.", ">>> ORIGEM: DESCONHECIDA."]:
        digitar_pausado(l, atraso=0.07, cor=Fore.RED); time.sleep(0.5)

    time.sleep(1.5); limpar_tela(); time.sleep(1.5)

    # ── Encerramento — o momento épico ───────────────────────────────────────
    print(); print(); print()

    for texto, cor, vel, pausa in [
        ("  CASO VANCE — DIA 186.", Fore.GREEN,  0.09, 2.2),
        ("", None, 0, 0.6),
        ("  Quatro fases.", Fore.WHITE, 0.08, 0.8),
        ("  Um legado.", Fore.WHITE, 0.08, 0.8),
        ("  Uma verdade.", Fore.WHITE, 0.08, 2.5),
        ("", None, 0, 0.8),
        ("  Ele estava vivo.", Fore.WHITE, 0.08, 1.0),
        ("  Do outro lado do terminal.", Fore.WHITE, 0.07, 1.0),
        ("  Esperando alguem que chegasse ate aqui.", Fore.WHITE, 0.07, 2.5),
        ("", None, 0, 0.8),
        ("  Professor Santana.", Fore.YELLOW, 0.11, 0.6),
        ("  Sala 1.", Fore.YELLOW, 0.14, 3.0),
        ("", None, 0, 0.8),
        ("  O legado de Vance esta protegido.", Fore.WHITE, 0.07, 0.8),
        ("  Agora e seu.", Fore.WHITE, 0.08, 2.5),
        ("", None, 0, 1.2),
        ("  BEM-VINDO, HERDEIRO.", Fore.CYAN, 0.14, 1.5),
        ("", None, 0, 0.5),
        ("  O jogo acabou. A historia nao.", Fore.GREEN, 0.09, 0.0),
    ]:
        if cor:
            for ch in texto:
                sys.stdout.write(cor + Style.BRIGHT + ch + Style.RESET_ALL)
                sys.stdout.flush(); time.sleep(vel)
            print()
        else:
            print()
        time.sleep(pausa)

    print(); time.sleep(1.0)
    print(Fore.GREEN + Style.DIM + "  VANCE_OS v1.0.4 — SESSAO ENCERRADA.")
    print(Fore.GREEN + Style.DIM + "  CASO VANCE — DIA 186 — RESOLVIDO.")
    print()


def fase_4():
    _enigma_vigenere()   # Enigma Vigenère → LEGADO
    _conversa_vance()    # Conversa + 3 perguntas + encerramento épico


# ──────────────────────────────────────────────
# Ponto de entrada
# ──────────────────────────────────────────────

if __name__ == "__main__":
    try:
        fase_1()        # Hex → ARIADNE
        ponte_fase_2()  # Abre fase2.html → valida SYSTEM_OVERRIDE_09X
        fase_3()        # Sophie Germain → 771483
        fase_4()        # Vigenère → LEGADO → conversa com Vance → encerramento
    except KeyboardInterrupt:
        print(Fore.RED + "\n\nConexao abortada pelo usuario.")
