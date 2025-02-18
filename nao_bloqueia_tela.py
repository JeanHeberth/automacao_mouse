import pyautogui
import time
import random
import psutil
import platform

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
        if verificar_teams():
            # Define uma área fixa da tela para mover o mouse (ajuste conforme necessário)
            x_min, x_max = 500, 1000  # Ajuste a posição horizontal
            y_min, y_max = 300, 700   # Ajuste a posição vertical

            # Calcula uma posição aleatória dentro dessa área
            novo_x = random.randint(x_min, x_max)
            novo_y = random.randint(y_min, y_max)

            # Move o mouse para essa posição
            pyautogui.moveTo(novo_x, novo_y, duration=0.5)
            print(f"🖱️ Mouse movido para {novo_x}, {novo_y} dentro da área do Teams.")

        else:
            print("⚠️ Microsoft Teams não encontrado. O mouse não foi movido.")

        # Simula o pressionamento de uma tecla para evitar bloqueio
        evitar_bloqueio_tela()

        # Aguarda 2 minutos antes de repetir
        time.sleep(120)

if __name__ == "__main__":
    print("🔵 Movimentação do mouse iniciada... O Teams permanecerá online e a tela não bloqueará!")
    movimentar_mouse_no_teams()
