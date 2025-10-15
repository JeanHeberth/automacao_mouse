import platform
import subprocess
import psutil

try:
    import pygetwindow as gw
except ImportError:
    gw = None

from .base_app import BaseApp

class ChatGoogleApp(BaseApp):
    def __init__(self):
        super().__init__("Google Chat")

    def verificar_processo(self):
        for processo in psutil.process_iter(attrs=['name']):
            nome = processo.info['name']
            if nome and ('Chat' in nome or 'Google Chat' in nome):
                return True
        return False

    def obter_posicao_janela(self):
        sistema = platform.system()

        if sistema == "Windows" and gw:
            janelas = gw.getWindowsWithTitle("Google Chat")
            if not janelas:
                janelas = gw.getWindowsWithTitle("Chat")
            if janelas:
                janela = janelas[0]
                return janela.left, janela.top, janela.width, janela.height

        elif sistema == "Darwin":
            try:
                subprocess.run(["osascript", "-e", 'tell application \"Google Chat\" to activate'], check=True)
                print("✅ Google Chat trazido para frente no macOS.")
                return True
            except subprocess.CalledProcessError:
                print("⚠️ Erro ao tentar ativar o Google Chat no macOS.")
        return None
