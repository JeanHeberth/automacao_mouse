from core.google.teams_app import TeamsApp
from core.teams.chat_google_app import ChatGoogleApp

def detectar_app_ativo():
    """Detecta automaticamente qual app deve ser mantido ativo."""
    chat = ChatGoogleApp()
    teams = TeamsApp()

    if chat.verificar_processo():
        return chat
    elif teams.verificar_processo():
        return teams
    return None


if __name__ == "__main__":
    print("🔍 Detectando aplicativo ativo (Google Chat ou Teams)...")
    app = detectar_app_ativo()

    if app:
        print(f"✅ {app.nome} detectado! Mantendo online e evitando bloqueio de tela.")
        app.manter_online()
    else:
        print("❌ Nenhum aplicativo compatível encontrado. Abra o Chat ou o Teams e execute novamente.")
