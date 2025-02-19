import platform
import pyautogui
import time
import random
import psutil
import subprocess

# Para Windows
try:
    import pygetwindow as gw
except ImportError:
    gw = None

def obter_posicao_teams():
    """Obtém a posição e dimensões da janela do Microsoft Teams."""
    sistema = platform.system()

    if sistema == "Windows" and gw:
        janelas = gw.getWindowsWithTitle("Microsoft Teams")
        if janelas:
            janela = janelas[0]
            return janela.left, janela.top, janela.width, janela.height

    elif sistema == "Darwin":
        # No macOS, usar AppleScript para trazer o Teams para frente
        try:
            subprocess.run(["osascript", "-e", 'tell application "Microsoft Teams" to activate'], check=True)
            print("✅ Teams trazido para frente no macOS.")
            return True  # Simula que a janela foi encontrada
        except subprocess.CalledProcessError:
            print("⚠️ Erro ao tentar ativar o Microsoft Teams no macOS.")

    return None

def verificar_teams():
    """Verifica se o processo do Microsoft Teams está rodando."""
    for processo in psutil.process_iter(attrs=['name']):
        if 'Teams' in processo.info['name']:
            return True
    return False

def evitar_bloqueio_tela():
    """Simula a pressão de uma tecla para evitar o bloqueio da tela."""
    if platform.system() == "Windows":
        pyautogui.press("shift")  # No Windows, pressionamos Shift
    else:
        pyautogui.press("ctrl")   # No Mac/Linux, pressionamos Ctrl
    print("🔄 Tecla pressionada para evitar bloqueio de tela.")

def movimentar_mouse_no_teams():
    while True:
        posicao = obter_posicao_teams()

        if posicao:
            if isinstance(posicao, tuple):
                x, y, largura, altura = posicao
                novo_x = random.randint(x + 10, x + largura - 10)
                novo_y = random.randint(y + 10, y + altura - 10)
            else:
                # Caso esteja no macOS, escolhemos uma posição fixa (ajuste conforme necessário)
                novo_x, novo_y = 800, 500
            
            pyautogui.moveTo(novo_x, novo_y, duration=0.5)
            print(f"🖱️ Mouse movido para {novo_x}, {novo_y} dentro da área do Teams.")

        else:
            print("⚠️ Microsoft Teams não encontrado. O mouse não foi movido.")

        # Simula o pressionamento de uma tecla para evitar bloqueio
        evitar_bloqueio_tela()

        # Aguarda 1 minuto antes de repetir
        time.sleep(60)

if __name__ == "__main__":
    print("🔵 Movimentação do mouse iniciada... O Teams permanecerá online e a tela não bloqueará!")
    movimentar_mouse_no_teams()
