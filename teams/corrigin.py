import platform
import pyautogui
import time
import random
import pygetwindow as gw

def obter_posicao_teams():
    """Obtém a posição e dimensões da janela do Microsoft Teams."""
    janelas = gw.getWindowsWithTitle("Microsoft Teams")  # Busca a janela do Teams
    if janelas:
        janela = janelas[0]
        return janela.left, janela.top, janela.width, janela.height
    return None

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
            x, y, largura, altura = posicao

            # Calcula uma posição aleatória dentro da janela do Teams
            novo_x = random.randint(x + 10, x + largura - 10)
            novo_y = random.randint(y + 10, y + altura - 10)

            # Move o mouse para essa posição dentro do Teams
            pyautogui.moveTo(novo_x, novo_y, duration=0.5)
            print(f"Mouse movido para {novo_x}, {novo_y} dentro do Teams.")
            
        else:
            print("⚠️ Microsoft Teams não encontrado. O mouse não foi movido.")

        # Simula o pressionamento de uma tecla para evitar bloqueio
        evitar_bloqueio_tela()

        # Aguarda 2 minutos antes de repetir
        time.sleep(60)


        

if __name__ == "__main__":
    print("🔵 Movimentação do mouse iniciada... O Teams permanecerá online e a tela não bloqueará!")
    movimentar_mouse_no_teams()
