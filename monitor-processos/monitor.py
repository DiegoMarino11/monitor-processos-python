import psutil
import time
from datetime import datetime
from colorama import init, Fore, Back, Style

# Inicializa o colorama (para cores no Windows/Linux/Mac)
init(autoreset=True)

processos_para_monitorar = ["python.exe", "chrome.exe", "notepad.exe"]

def verificar_processos():
    processos_ativos = [p.name() for p in psutil.process_iter()]
    print(f"\n{Back.BLUE}[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Monitorando processos...{Style.RESET_ALL}\n")

    for proc in processos_para_monitorar:
        if proc in processos_ativos:
            print(f"{Fore.GREEN}✅ {proc} está em execução.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}⛔ {proc} NÃO está em execução!{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        print(f"{Fore.CYAN}=== MONITOR DE PROCESSOS INICIADO ===")
        print(f"{Fore.YELLOW}Pressione CTRL+C para parar...{Style.RESET_ALL}\n")
        while True:
            verificar_processos()
            time.sleep(10)
    except KeyboardInterrupt:
        print(f"\n{Fore.MAGENTA}=== MONITOR ENCERRADO PELO USUÁRIO ===")