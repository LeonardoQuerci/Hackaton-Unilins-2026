let tentativas = 0;

// --- HONEYPOT ---
function LIBERAR_ACESSO(senha_fase2) {
  // Mapa de referências hexadecimais (Disfarce)
  const _0x1a2b = ['\x66\x65\x65\x64\x62\x61\x63\x6b', '\x63\x6c\x61\x73\x73\x4e\x61\x6d\x65', '\x73\x68\x6f\x77', '\x65\x72\x72\x6f', '\x72\x65\x73\x70\x6f\x73\x74\x61', '\x76\x61\x6c\x75\x65'];

  // O HTML da pegadinha codificado
  const _0x55cf = '\x3e\x3e\x3e\x20\x50\x52\x4f\x54\x4f\x43\x4f\x4c\x4f\x20\x44\x45\x20\x53\x45\x47\x55\x52\x41\x4e\x43\x41\x20\x41\x54\x49\x56\x41\x44\x4f\x2e\x3c\x62\x72\x3e\x54\x45\x4e\x54\x41\x54\x49\x56\x41\x20\x44\x45\x20\x42\x59\x50\x41\x53\x53\x20\x52\x45\x47\x49\x53\x54\x52\x41\x44\x41\x2e\x20\x41\x43\x45\x53\x53\x4f\x20\x42\x4c\x4f\x51\x55\x45\x41\x44\x4f\x2e\x3c\x62\x72\x3e\x3c\x73\x70\x61\x6e\x20\x73\x74\x79\x6c\x65\x3d\x22\x66\x6f\x6e\x74\x2d\x73\x69\x7a\x65\x3a\x31\x32\x70\x78\x3b\x20\x63\x6f\x6c\x6f\x72\x3a\x23\x66\x66\x32\x32\x32\x32\x38\x38\x3b\x22\x3e\x56\x6f\x63\xea\x20\x61\x63\x68\x6f\x75\x20\x6d\x65\x73\x6d\x6f\x20\x71\x75\x65\x20\x73\x65\x72\x69\x61\x20\x74\xe3\x6f\x20\x66\xe1\x63\x69\x6c\x3f\x3c\x2f\x73\x70\x61\x6e\x3e';

  const _node = document.getElementById(_0x1a2b[0]);
  
  _node[_0x1a2b[1]] = ""; // Limpa classe
  _node.classList.add(_0x1a2b[2], _0x1a2b[3]); // Adiciona 'show' e 'erro'
  _node.innerHTML = _0x55cf; // Insere o texto da pegadinha

  // Limpa o campo de resposta
  document.getElementById(_0x1a2b[4])[_0x1a2b[5]] = "";
}

// Enter para enviar
document.getElementById('resposta').addEventListener('keydown', function(e) {
  if (e.key === 'Enter') verificar();
});

async function verificar() {
  const entrada = document.getElementById('resposta').value.trim().toUpperCase();
  const feedback = document.getElementById('feedback');
  const cont = document.getElementById('cont');
  const senha_fase2 = entrada;

  // Testa a senha digitada e libera o acesso
  if (senha_fase2 === "12345") {
    LIBERAR_ACESSO(senha_fase2);
    return;
  }

  tentativas++;
  cont.textContent = tentativas;

  feedback.className = '';
  feedback.classList.add('show');

  // --- VARIÁVEIS DE SEGURANÇA (GERADAS OFFLINE) ---
  const hashCorreto = "7a31b97b6ae19dd436c32ee25c66c722161f349f550651496f5855778b31b18a";
  const segredoMisto = [31, 16, 17, 17, 23, 9, 30, 11, 19, 9, 27, 16, 12, 22, 1, 30, 116, 124, 20];

  // --- FUNÇÃO CRIPTOGRÁFICA ---
  async function gerarHash(texto) {
    const encoder = new TextEncoder();
    const data = encoder.encode(texto.toUpperCase().trim());
    const hashBuffer = await crypto.subtle.digest('SHA-256', data);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  }

  const hashInput = await gerarHash(entrada);

  if (hashInput === hashCorreto) {

    let codigoFinal = "";
    for (let i = 0; i < segredoMisto.length; i++) {
      let charCodigo = entrada.charCodeAt(i % entrada.length) ^ segredoMisto[i];
      codigoFinal += String.fromCharCode(charCodigo);
    }

    tocarSomPorta();

    feedback.classList.add('sucesso');
    feedback.innerHTML = `
      ACESSO CONCEDIDO<br>
      CÓDIGO DE SISTEMA: <span style="color:#00ff00; font-weight:bold;">${codigoFinal}</span><br>
      NÚMERO DA SORTE REGISTRADO: 7<br>
      <br>
      <span style="font-size:15px; font-family:'Share Tech Mono',monospace; letter-spacing:2px; color: #00e5ff88;">
        Ariadne sempre foi rápida...<br>
        Ela deixou o rastro 7 posições à frente.<br>
        Para avançar, retroceda o caminho que ela percorreu.
      </span>
    `;
    document.getElementById('resposta').disabled = true;
    document.querySelector('button').disabled = true;

  } else {
    if (tentativas >= 3) {
      feedback.classList.add('dica');
      feedback.innerHTML = `
        >>> ACESSO NEGADO: RESPOSTA INVÁLIDA.<br>
        DICA DO SISTEMA: Ariadne sempre foi 7 passos à frente.<br>
        Para encontrá-la, você precisa retroceder.
      `;
    } else {
      feedback.classList.add('erro');
      feedback.innerHTML = `>>> ACESSO NEGADO: RESPOSTA INVÁLIDA. [TENTATIVA ${tentativas}]`;
    }
    document.getElementById('resposta').value = '';
    document.getElementById('resposta').focus();
  }
}

// Relógio
function atualizarRelogio() {
  const agora = new Date();
  const h = String(agora.getHours()).padStart(2, '0');
  const m = String(agora.getMinutes()).padStart(2, '0');
  const s = String(agora.getSeconds()).padStart(2, '0');
  document.getElementById('clock').textContent = `${h}:${m}:${s}`;
}
setInterval(atualizarRelogio, 1000);
atualizarRelogio();

function tocarSomPorta() {
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();

    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain);
    gain.connect(ctx.destination);

    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(80, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(40, ctx.currentTime + 0.8);

    gain.gain.setValueAtTime(0.3, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.9);

    osc.start(ctx.currentTime);
    osc.stop(ctx.currentTime + 0.9);

    const osc2 = ctx.createOscillator();
    const gain2 = ctx.createGain();
    osc2.connect(gain2);
    gain2.connect(ctx.destination);

    osc2.type = 'sine';
    osc2.frequency.setValueAtTime(880, ctx.currentTime + 0.9);
    osc2.frequency.setValueAtTime(1320, ctx.currentTime + 1.1);

    gain2.gain.setValueAtTime(0.2, ctx.currentTime + 0.9);
    gain2.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 1.4);

    osc2.start(ctx.currentTime + 0.9);
    osc2.stop(ctx.currentTime + 1.4);

  } catch(e) {}
}
