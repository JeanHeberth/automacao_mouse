import platform
import pyautogui

def evitar_bloqueio_tela():
    """Simula a pressão de uma tecla para evitar o bloqueio da tela."""
    if platform.system() == "Windows":
        pyautogui.press("shift")
    else:
        pyautogui.press("ctrl")
    print("🔄 Tecla pressionada para evitar bloqueio de tela.")
