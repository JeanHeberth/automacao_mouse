import platform
import pyautogui
import time
import random
import psutil
import subprocess

try:
    import pygetwindow as gw
except ImportError:
    gw = None


# ======================================================
# 🔍 Funções genéricas
# ======================================================

def evitar_bloqueio_tela():
    """Simula a pressão de uma tecla para evitar o bloqueio da tela."""
    if platform.system() == "Windows":
        pyautogui.press("shift")
    else:
        pyautogui.press("ctrl")
    print("🔄 Tecla pressionada para evitar bloqueio de tela.")


# ======================================================
# 💬 Funções para Microsoft Teams
# ======================================================

def verificar_teams():
    """Verifica se o processo do Microsoft Teams está rodando."""
    for processo in psutil.process_iter(attrs=['name']):
        if 'Teams' in processo.info['name']:
            return True
    return False


def obter_posicao_teams():
    """Obtém a posição e dimensões da janela do Microsoft Teams."""
    sistema = platform.system()

    if sistema == "Windows" and gw:
        janelas = gw.getWindowsWithTitle("Microsoft Teams")
        if janelas:
            janela = janelas[0]
            return janela.left, janela.top, janela.width, janela.height

    elif sistema == "Darwin":
        try:
            subprocess.run(["osascript", "-e", 'tell application "Microsoft Teams" to activate'], check=True)
            print("✅ Teams trazido para frente no macOS.")
            return True
        except subprocess.CalledProcessError:
            print("⚠️ Erro ao tentar ativar o Microsoft Teams no macOS.")

    return None


# ======================================================
# 💬 Funções para Google Chat (PWA)
# ======================================================

def verificar_chat():
    """Verifica se o processo do Google Chat (PWA) está rodando."""
    for processo in psutil.process_iter(attrs=['name']):
        nome = processo.info['name']
        if nome and ('Chat' in nome or 'Google Chat' in nome):
            return True
    return False


def obter_posicao_chat():
    """Obtém a posição e dimensões da janela do Google Chat (PWA)."""
    sistema = platform.system()

    if sistema == "Windows" and gw:
        # Pode aparecer com títulos levemente diferentes
        janelas = gw.getWindowsWithTitle("Google Chat")
        if not janelas:
            janelas = gw.getWindowsWithTitle("Chat")
        if janelas:
            janela = janelas[0]
            return janela.left, janela.top, janela.width, janela.height

    elif sistema == "Darwin":
        try:
            subprocess.run(["osascript", "-e", 'tell application "Google Chat" to activate'], check=True)
            print("✅ Google Chat trazido para frente no macOS.")
            return True
        except subprocess.CalledProcessError:
            print("⚠️ Erro ao tentar ativar o Google Chat no macOS.")

    return None


# ======================================================
# 🚀 Função principal
# ======================================================

def detectar_app_ativo():
    """Detecta automaticamente qual aplicativo está em uso."""
    if verificar_chat():
        return "chat"
    elif verificar_teams():
        return "teams"
    return None


def movimentar_mouse(app):
    """Move o mouse dentro do aplicativo especificado."""
    while True:
        posicao = None

        if app == "teams":
            posicao = obter_posicao_teams()
        elif app == "chat":
            posicao = obter_posicao_chat()

        if posicao:
            if isinstance(posicao, tuple):
                x, y, largura, altura = posicao
                novo_x = random.randint(x + 10, x + largura - 10)
                novo_y = random.randint(y + 10, y + altura - 10)
            else:
                # fallback para quando não temos coordenadas (ex: macOS)
                novo_x, novo_y = 800, 500

            pyautogui.moveTo(novo_x, novo_y, duration=0.5)
            print(f"🖱️ Mouse movido para {novo_x}, {novo_y} dentro da área do {app.capitalize()}.")

        else:
            print(f"⚠️ {app.capitalize()} não encontrado. O mouse não foi movido.")

        evitar_bloqueio_tela()
        time.sleep(60)


# ======================================================
# 🏁 Execução principal
# ======================================================

if __name__ == "__main__":
    print("🔍 Verificando qual aplicativo está ativo (Google Chat ou Microsoft Teams)...")
    app = detectar_app_ativo()

    if app:
        print(f"✅ Aplicativo detectado: {app.capitalize()}")
        print(f"🔵 Mantendo {app.capitalize()} online e tela ativa...")
        movimentar_mouse(app)
    else:
        print("❌ Nenhum aplicativo compatível encontrado (Teams ou Google Chat).")
        print("🔁 Abra um deles e execute novamente.")
