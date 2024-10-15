import tkinter as tk
from tkinter import messagebox
import random

#começo
def iniciar_jogo():
    global rodadas
    try:
        rodadas = int(entry_rodadas.get())
        if rodadas <= 0:
            messagebox.showerror("Erro", "O número de rodadas deve ser maior que zero.")
            return
        iniciar_rod(rodadas)
    except ValueError:
        messagebox.showerror("Erro", 'Informe um valor inteiro para o número de rodadas.')

def iniciar_rod(rodadas):
    global pontos, rodada_atual, rng_number
    pontos = 0
    rodada_atual = 1
    rng_number = random.randint(1, 10)
    entry_rodadas.config(state='disabled')
    label_status.config(text=f'{rodada_atual}ª Rodada: Adivinhe o número, está entre 1 e 10!')
    entry_numero.config(state='normal')
    button_adivinhar.config(state='normal')

def adivinhar_num():
    global pontos, rodada_atual, rng_number
    try:
        num = int(entry_numero.get())
        if num < 1 or num > 10:
            messagebox.showerror("Erro", "Digite um número entre 1 e 10.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor inteiro.")
        return

    if num == rng_number:
        pontos += 3
        messagebox.showinfo("Correto!", f"Correto! Seus pontos: {pontos}")
    else:
        if pontos > 0:
            pontos -= 1
        messagebox.showinfo("Errado!", f"Errado, o número era: {rng_number}. Seus pontos: {pontos}")

    if rodada_atual == rodadas:
        finalizar_jogo()
    else:
        rodada_atual += 1
        rng_number = random.randint(1, 10)
        label_status.config(text=f'{rodada_atual}ª Rodada: Adivinhe o número, está entre 1 e 10!')
        entry_numero.delete(0, tk.END)

def finalizar_jogo():
    messagebox.showinfo("Fim de jogo", f'Fim de jogo.\nPontos finais: {pontos}')
    entry_rodadas.config(state='normal')
    entry_numero.config(state='disabled')
    button_adivinhar.config(state='disabled')
    label_status.config(text='Insira o número de rodadas e clique em "Iniciar Jogo".')

#interface grafica aqui
root = tk.Tk()
root.title("Jogo de Adivinhação")

frame = tk.Frame(root)
frame.pack(pady=20)

label_rodadas = tk.Label(frame, text="Número de rodadas:")
label_rodadas.grid(row=0, column=0, padx=15)

entry_rodadas = tk.Entry(frame)
entry_rodadas.grid(row=0, column=1, padx=15)

button_iniciar = tk.Button(frame, text="Iniciar Jogo", command=iniciar_jogo)
button_iniciar.grid(row=0, column=2, padx=30)

label_status = tk.Label(root, text='Insira o número de rodadas e clique em "Iniciar Jogo".')
label_status.pack(pady=20)

entry_numero = tk.Entry(root, state='disabled')
entry_numero.pack(pady=5)

button_adivinhar = tk.Button(root, text="Adivinhar", state='disabled', command=adivinhar_num)
button_adivinhar.pack(pady=5)

root.mainloop()
