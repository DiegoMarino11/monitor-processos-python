import psutil
import time
import threading
import logging
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext

# Configurar o log
logging.basicConfig(filename="monitor_log.txt", level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

processos_para_monitorar = ["python.exe", "chrome.exe", "notepad.exe"]
monitorando = False

def verificar_processos(app_output):
    global monitorando
    while monitorando:
        processos_ativos = [p.name() for p in psutil.process_iter()]
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        app_output.insert(tk.END, f"\n[{timestamp}] Monitorando processos...\n")
        app_output.see(tk.END)

        for proc in processos_para_monitorar:
            if proc in processos_ativos:
                msg = f"OK: {proc} está em execução."
                logging.info(msg)
            else:
                msg = f"ALERTA: {proc} NÃO está em execução!"
                logging.warning(msg)
            app_output.insert(tk.END, msg + "\n")
            app_output.see(tk.END)

        time.sleep(10)

def iniciar_monitoramento(output_widget):
    global monitorando
    if not monitorando:
        monitorando = True
        threading.Thread(target=verificar_processos, args=(output_widget,), daemon=True).start()

def parar_monitoramento():
    global monitorando
    monitorando = False

# Interface Gráfica
janela = tk.Tk()
janela.title("Monitor de Processos")
janela.geometry("600x400")

txt_status = scrolledtext.ScrolledText(janela, wrap=tk.WORD)
txt_status.pack(expand=True, fill='both', padx=10, pady=10)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

btn_iniciar = tk.Button(frame_botoes, text="Iniciar Monitoramento", command=lambda: iniciar_monitoramento(txt_status))
btn_iniciar.grid(row=0, column=0, padx=10)

btn_parar = tk.Button(frame_botoes, text="Parar", command=parar_monitoramento)
btn_parar.grid(row=0, column=1, padx=10)

janela.mainloop()
