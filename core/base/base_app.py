import platform
import pyautogui
import time
import random
from abc import ABC, abstractmethod
from .utils import evitar_bloqueio_tela

class BaseApp(ABC):
    """Classe base para todos os aplicativos."""

    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def verificar_processo(self):
        """Verifica se o processo do aplicativo está ativo."""
        pass

    @abstractmethod
    def obter_posicao_janela(self):
        """Retorna posição (x, y, largura, altura) da janela."""
        pass

    def manter_online(self):
        """Executa a rotina de movimentação e prevenção de bloqueio."""
        while True:
            posicao = self.obter_posicao_janela()
            if posicao:
                if isinstance(posicao, tuple):
                    x, y, largura, altura = posicao
                    novo_x = random.randint(x + 10, x + largura - 10)
                    novo_y = random.randint(y + 10, y + altura - 10)
                else:
                    novo_x, novo_y = 800, 500  # fallback padrão

                pyautogui.moveTo(novo_x, novo_y, duration=0.5)
                print(f"🖱️ {self.nome}: mouse movido para ({novo_x}, {novo_y})")
            else:
                print(f"⚠️ {self.nome}: janela não encontrada.")

            evitar_bloqueio_tela()
            time.sleep(60)
