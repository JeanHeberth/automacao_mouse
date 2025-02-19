# 🖱️ Automação para Manter o Microsoft Teams Online

Este script mantém o Microsoft Teams sempre **online** e impede que a tela do computador **bloqueie automaticamente**. Ele funciona tanto no **Windows** quanto no **macOS**.

---

## 🚀 **Funcionalidades**
✅ Mantém o **Microsoft Teams ativo** automaticamente.  
✅ **Impede** que o computador bloqueie a tela.  
✅ **Funciona no Windows e macOS** sem modificações.  
✅ **Movimenta o mouse periodicamente** dentro do Teams.  
✅ **Traz o Teams para frente** (no macOS usa AppleScript).  

---

## 🛠 **Instalação e Configuração**
### 1️⃣ **Clone o repositório**
```sh
git clone https://github.com/seu-usuario/automacao-teams.git
cd automacao-teams


2️⃣ Crie e ative um ambiente virtual (opcional, mas recomendado)
No Windows:


python -m venv venv
venv\Scripts\activate
No macOS:

python3 -m venv venv
source venv/bin/activate

3️⃣ Instale as dependências
pip install -r requirements.txt

4️⃣ Execute o script
python execute.py
💻 Requisitos
📌 Windows: Python 3.7+
📌 macOS: Python 3.7+ (com osascript já instalado)

📢 IMPORTANTE: No macOS, se houver erro ao instalar pyobjc, tente:

pip install pyobjc

📜 Como Funciona
🔹 No Windows, o script encontra a janela do Microsoft Teams e movimenta o mouse dentro dela.
🔹 No macOS, o script usa AppleScript (osascript) para trazer o Teams para frente.
🔹 Em ambos os sistemas, o script simula o pressionamento de uma tecla (Shift no Windows, Ctrl no macOS) para evitar bloqueio de tela.


🎯 Problemas e Soluções
🔹 O Teams não fica online?
➡️ Certifique-se de que ele está aberto antes de rodar o script.

🔹 Erro ao instalar dependências no macOS?
➡️ Rode manualmente:


pip install pyobjc
🔹 O script não funciona no Windows?
➡️ Verifique se o Python e o pip estão instalados corretamente.

✨ Contribuições
Contribuições são bem-vindas! Se encontrar um bug ou tiver uma melhoria, abra um Pull Request ou envie uma issue. 🚀

📄 Licença
Este projeto é distribuído sob a licença Jean Heberth. Você pode usá-lo e modificá-lo livremente.

