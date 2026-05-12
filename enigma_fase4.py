import time
import sys
import os
import re
import hashlib
import random
import string
from colorama import Fore, Style, init

init(autoreset=True)

_ANSI_PREFIX_RE = re.compile(r'^(\x1b\[[0-9;]*m)+')

# ─── Utilitários (compatíveis com o main.py existente) ────────────────────────

def digitar_pausado(texto, atraso=0.05):
    match = _ANSI_PREFIX_RE.match(texto)
    if match:
        sys.stdout.write(match.group(0))
        sys.stdout.flush()
        texto = texto[match.end():]
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(atraso)
    sys.stdout.write(Style.RESET_ALL)
    sys.stdout.flush()
    print()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def separador(cor=Fore.GREEN, char="─"):
    print(cor + char * 60 + Style.RESET_ALL)

# ─── Constantes do Enigma ─────────────────────────────────────────────────────
#
#  DESIGN DO PUZZLE (3 camadas):
#
#  CAMADA 1 — Extração do fluxo corrompido
#    Fluxo de 36 bytes onde os caracteres nas posições
#    1, 8, 15, 22, 29, 36 (passo = número da sorte = 7) formam o código.
#    Posição  1 → L
#    Posição  8 → V
#    Posição 15 → O
#    Posição 22 → A
#    Posição 29 → G
#    Posição 36 → B
#    Código extraído: LVOAGB
#
#  CAMADA 2 — Identificação da cifra
#    O terminal exibe a tabela de Vigenère e nomeia o tipo de cifra.
#    Os pares relevantes são destacados em amarelo.
#
#  CAMADA 3 — Descriptografia com chave ARIADNE (Fase 1)
#    LVOAGB descriptografado com chave ARIADNE = LEGADO
#    Verificação: hashlib.sha256("LEGADO".encode()).hexdigest()
#

_FLUXO_CORROMPIDO = "LAXMQPNVKRTHZFODCWASPAYUJXWBGNIHQEMB"
#                    ^      ^      ^      ^      ^      ^
#                    1      8     15     22     29     36   (passo 7)

# SHA-256("LEGADO") — jamais compare strings em texto puro
_HASH_LEGADO = "cb765a464c8baa7ff8a6dc9bd15d1b29be6ee2b1ab48759bbacc57d3455de28a"

# ─── Componentes Visuais ──────────────────────────────────────────────────────

def _barra_progresso(label, total=30):
    """Barra de progresso animada que vai de vermelho a verde."""
    for i in range(total + 1):
        pct        = int(i / total * 100)
        preenchido = "█" * i
        vazio      = "░" * (total - i)
        cor        = Fore.RED if pct < 40 else Fore.YELLOW if pct < 80 else Fore.GREEN
        sys.stdout.write(
            f"\r{Fore.WHITE}{label}: {cor}[{preenchido}{vazio}]"
            f"{Fore.WHITE} {pct:3d}%{Style.RESET_ALL}"
        )
        sys.stdout.flush()
        time.sleep(0.055)
    print()


def _animar_fluxo(dado, duracao=5):
    """
    Efeito de recuperação estilo matrix: o fluxo começa como ruído
    puro e vai progressivamente estabilizando nos bytes corretos.
    Chars nas posições-chave (múltiplos de 7) são os últimos a fixar,
    criando um momento "eureka" visual quando aparecem em amarelo.
    """
    ruido_chars  = string.ascii_uppercase + "0123456789█▓▒░#@$%"
    posicoes_key = {0, 7, 14, 21, 28, 35}   # índices 0-based das posições-chave
    inicio       = time.time()

    while time.time() - inicio < duracao:
        progresso = (time.time() - inicio) / duracao
        linha = "  "
        for idx, c in enumerate(dado):
            # Posições-chave estabilizam por último (suspense)
            limiar = progresso * 1.5 if idx not in posicoes_key else progresso * 0.9
            if random.random() < limiar:
                cor = Fore.YELLOW + Style.BRIGHT if idx in posicoes_key else Fore.WHITE
                linha += cor + c + Style.RESET_ALL
            else:
                linha += Fore.GREEN + Style.DIM + random.choice(ruido_chars) + Style.RESET_ALL
        sys.stdout.write('\r' + linha + "  ")
        sys.stdout.flush()
        time.sleep(0.055)

    # Estabilização final: chars-chave em amarelo, restantes em branco
    linha_final = "  "
    for idx, c in enumerate(dado):
        if idx in posicoes_key:
            linha_final += Fore.YELLOW + Style.BRIGHT + c + Style.RESET_ALL
        else:
            linha_final += Fore.WHITE + Style.DIM + c + Style.RESET_ALL
    sys.stdout.write('\r' + linha_final + "\n")
    sys.stdout.flush()


def _tabela_vigenere():
    """
    Exibe a tabela de Vigenère para as 6 linhas únicas da chave ARIADNE.
    Os pares (chave × texto plano) que compõem a solução são destacados
    em amarelo brilhante — o restante fica em verde escuro.

    Mapeamento de pares a destacar:
      (A, L) → L   posição 0
      (R, E) → V   posição 1
      (I, G) → O   posição 2
      (A, A) → A   posição 3
      (D, D) → G   posição 4
      (N, O) → B   posição 5
    """
    alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Colunas de texto plano a destacar por linha de chave
    destaques = {
        'A': {'L', 'A'},
        'R': {'E'},
        'I': {'G'},
        'D': {'D'},
        'N': {'O'},
        'E': set(),
    }

    # Cabeçalho da tabela
    print(Fore.CYAN + Style.DIM + "  CHAVE  │  " + "  ".join(alfa))
    print(Fore.GREEN + Style.DIM + "  ───────┼" + "─" * 78)

    visto = set()
    for letra_chave in "ARIADNE":
        if letra_chave in visto:
            continue
        visto.add(letra_chave)

        k         = ord(letra_chave) - ord('A')
        cols_dest = destaques.get(letra_chave, set())
        linha     = Fore.CYAN + f"    {letra_chave}    " + Fore.GREEN + Style.DIM + "│  "

        for letra_plain in alfa:
            cifrado = chr((ord(letra_plain) - ord('A') + k) % 26 + ord('A'))
            if letra_plain in cols_dest:
                linha += Fore.YELLOW + Style.BRIGHT + cifrado + Style.RESET_ALL + Fore.GREEN + Style.DIM + "  "
            else:
                linha += Fore.GREEN + Style.DIM + cifrado + "  "

        print(linha + Style.RESET_ALL)
    print()


def _contador_regressivo(segundos):
    """Contador regressivo visual com cor progressiva."""
    for i in range(segundos, 0, -1):
        cor = Fore.RED if i <= 3 else Fore.YELLOW if i <= 8 else Fore.GREEN
        sys.stdout.write(f"\r  {cor}Acessando em {i:02d}s...{Style.RESET_ALL}  ")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write(f"\r  {Fore.CYAN}Acesso liberado.          {Style.RESET_ALL}\n")
    sys.stdout.flush()


# ─── Enigma Principal ─────────────────────────────────────────────────────────

def enigma_pre_fase4():
    """
    Enigma final antes da sequência de entradas da Fase 4.

    Requer conhecimento acumulado das 3 fases anteriores:
      - Fase 1: ARIADNE  → chave Vigenère
      - Fase 2: 7        → passo de extração do fluxo
      - Fase 3: 771483   → referenciado nos metadados (frequência 7.71483 MHz)

    Resposta: LEGADO
    """
    limpar_tela()

    # ── Header ──────────────────────────────────────────────────────────────
    print(Fore.RED + Style.BRIGHT + "╔" + "═" * 58 + "╗")
    print(Fore.RED + Style.BRIGHT + "║" + " PROTOCOLO SIGMA  ·  NÍVEL MÁXIMO  ·  ACESSO RESTRITO ".center(58) + "║")
    print(Fore.RED + Style.BRIGHT + "║" + " LEGADO DE VANCE  ·  AUTENTICAÇÃO FINAL               ".center(58) + "║")
    print(Fore.RED + Style.BRIGHT + "╚" + "═" * 58 + "╝")
    print()
    time.sleep(1.2)

    # ── Narrativa de abertura ────────────────────────────────────────────────
    digitar_pausado(Fore.WHITE + "DIA 186. CASO VANCE. RELATÓRIO FINAL DE INVESTIGAÇÃO.", atraso=0.03)
    time.sleep(0.4)
    digitar_pausado(Fore.WHITE + "Três barreiras. Três segredos. Três vitórias.", atraso=0.03)
    time.sleep(0.4)
    digitar_pausado(Fore.WHITE + "A herança do Dr. Alistair Vance está a um passo de você.", atraso=0.03)
    time.sleep(0.8)
    print()
    digitar_pausado(Fore.YELLOW + "O sistema detectou um arquivo que Vance cifrou com uma", atraso=0.025)
    digitar_pausado(Fore.YELLOW + "técnica que ele jamais ensinou a ninguém — exceto a ela.", atraso=0.025)
    time.sleep(1.2)
    print()

    # ── Recuperação do arquivo ───────────────────────────────────────────────
    separador()
    digitar_pausado(Fore.CYAN + ">>> ARQUIVO LOCALIZADO  : /root/.sigma/vance_legado.enc", atraso=0.02)
    time.sleep(0.2)
    digitar_pausado(Fore.CYAN + ">>> INTEGRIDADE         : 12% — DADOS SEVERAMENTE CORROMPIDOS", atraso=0.02)
    time.sleep(0.2)
    digitar_pausado(Fore.CYAN + ">>> INICIANDO RECUPERAÇÃO FORÇADA...", atraso=0.03)
    print()
    _barra_progresso("RECUPERAÇÃO DE DADOS", total=30)
    print()

    # ── Fluxo corrompido ─────────────────────────────────────────────────────
    separador(Fore.RED, "═")
    print(Fore.RED + Style.BRIGHT + "  FLUXO INTERCEPTADO  ·  36 BYTES  ·  ORIGEM: DESCONHECIDA")
    separador(Fore.RED, "═")
    print()
    _animar_fluxo(_FLUXO_CORROMPIDO, duracao=6)
    print()

    # ── Nota de Vance ────────────────────────────────────────────────────────
    separador()
    print(Fore.YELLOW + Style.BRIGHT + "  FRAGMENTO RECUPERADO — ANOTAÇÃO MANUSCRITA  ·  A. VANCE")
    separador()
    print()

    notas = [
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
    ]

    for nota in notas:
        if nota == "":
            print()
        else:
            digitar_pausado(Fore.YELLOW + nota, atraso=0.018)
        time.sleep(0.04)
    print()

    # ── Tabela de Vigenère ───────────────────────────────────────────────────
    separador()
    print(Fore.CYAN + Style.BRIGHT + "  CIFRA POLIALFABÉTICA  ·  TABELA DE DESVIOS DE VANCE")
    print(Fore.CYAN + Style.DIM   + "  [ LINHAS: LETRA DA CHAVE  ·  COLUNAS: TEXTO PLANO ]")
    print(Fore.CYAN + Style.DIM   + "  [ CÉLULAS EM AMARELO: PARES RELEVANTES AO FLUXO   ]")
    separador()
    print()
    _tabela_vigenere()

    # ── Metadados como pistas sutis ─────────────────────────────────────────
    print(Fore.GREEN + Style.DIM + "  >> FREQUÊNCIA DO ARQUIVO  : 7.71483 MHz")
    print(Fore.GREEN + Style.DIM + "  >> COMPRIMENTO DO FLUXO   : 36 BYTES")
    print(Fore.GREEN + Style.DIM + "  >> PROTOCOLO              : SIGMA-V  ·  CIFRA POLIALFABÉTICA")
    print(Fore.GREEN + Style.DIM + "  >> ASSINATURA             : A.V / [ARIADNE]")
    print()
    time.sleep(0.8)

    # ── Prompt de autenticação ───────────────────────────────────────────────
    print(Fore.RED + Style.BRIGHT + "  ╔══════════════════════════════════════════════════════════╗")
    print(Fore.RED + Style.BRIGHT + "  ║  AUTENTICAÇÃO SIGMA — INSIRA A PALAVRA DO LEGADO        ║")
    print(Fore.RED + Style.BRIGHT + "  ╚══════════════════════════════════════════════════════════╝")
    print()

    tentativas = 0
    while True:
        print(Fore.RED + Style.BRIGHT + "  SIGMA > ", end="")
        entrada = input().strip().upper()

        digest = hashlib.sha256(entrada.encode()).hexdigest()
        tentativas += 1

        digitar_pausado(Fore.GREEN + "  >>> VERIFICANDO INTEGRIDADE CRIPTOGRÁFICA...", atraso=0.04)
        time.sleep(1.0)

        if digest == _HASH_LEGADO:
            # ── Sucesso ──────────────────────────────────────────────────────
            print(Fore.GREEN + "  [ OK ] PALAVRA CONFIRMADA.")
            time.sleep(0.4)
            print(Fore.GREEN + "  [ OK ] ASSINATURA DE VANCE VALIDADA.")
            time.sleep(0.4)
            print(Fore.GREEN + "  [ OK ] PROTOCOLO SIGMA — SELADO.")
            time.sleep(0.8)
            print()
            print(Fore.CYAN + Style.BRIGHT + "  " + "═" * 56)

            linhas_sucesso = [
                "  O LEGADO DE VANCE ESTÁ DESBLOQUEADO.",
                "  Você encontrou o que ele protegeu por anos.",
                "  Prepare-se. A transmissão final começa agora.",
            ]
            for linha in linhas_sucesso:
                digitar_pausado(Fore.CYAN + Style.BRIGHT + linha, atraso=0.045)
                time.sleep(0.2)

            print(Fore.CYAN + Style.BRIGHT + "  " + "═" * 56)
            print()
            time.sleep(2)
            break

        else:
            # ── Falha com dicas progressivas ─────────────────────────────────
            print(Fore.RED + f"  >>> PALAVRA INVÁLIDA. [TENTATIVA {tentativas}]")
            print()

            if tentativas == 2:
                print(Fore.RED + Style.DIM +
                      "  DICA: Existe um ritmo escondido no fluxo.")
                print(Fore.RED + Style.DIM +
                      "        O número da sorte define esse ritmo.")
            elif tentativas == 4:
                print(Fore.RED + Style.DIM +
                      "  DICA: Extraia os bytes do fluxo seguindo o passo correto.")
                print(Fore.RED + Style.DIM +
                      "        O que sobrar é uma cifra polialfabética.")
            elif tentativas == 6:
                print(Fore.RED + Style.DIM +
                      "  DICA: A herdeira de Vance é a chave da tabela acima.")
                print(Fore.RED + Style.DIM +
                      "        Você já sabe o nome dela desde o primeiro terminal.")
            elif tentativas >= 8:
                print(Fore.RED + Style.DIM +
                      "  DICA FINAL: Passo=7 → posições 1,8,15,22,29,36 → LVOAGB")
                print(Fore.RED + Style.DIM +
                      "              Chave=ARIADNE → Vigenère → ?")
            print()


# ─── Ponto de entrada (para testes isolados) ──────────────────────────────────

if __name__ == "__main__":
    try:
        enigma_pre_fase4()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n  Conexão abortada pelo usuário.")
