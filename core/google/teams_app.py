import platform
import subprocess
import psutil

try:
    import pygetwindow as gw
except ImportError:
    gw = None

from .base_app import BaseApp

class TeamsApp(BaseApp):
    def __init__(self):
        super().__init__("Microsoft Teams")

    def verificar_processo(self):
        for processo in psutil.process_iter(attrs=['name']):
            if 'Teams' in processo.info['name']:
                return True
        return False

    def obter_posicao_janela(self):
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
