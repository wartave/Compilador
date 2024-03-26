# esto es main.py klk 
import tkinter as tk
from tkinter import ttk
from antlr4 import *
from antlr4 import ParseTreeWalker
from LexerVictor import LexerVictor
from ParserVictor import ParserVictor
from antlr4.error.ErrorListener import ConsoleErrorListener
from SemanticListener import SemanticListener
from VictorToPyhtonListener import VictorToPyhtonListener

tabla_tokens =None

def analizar():
    limpiar_tabla_tokens()
    entrada = entrada_texto.get("1.0", tk.END)
    stream = InputStream(entrada)
    lexer = LexerVictor(stream)
    tokens = CommonTokenStream(lexer)
    parser = ParserVictor(tokens)
    error_listener = ErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    tree = parser.programa()

    for token in tokens.tokens:
        tipo = parser.symbolicNames[token.type]
        valor = token.text
        tabla_tokens.insert("", "end", values=(tipo, valor))


    semantico_listener = SemanticListener()
    walker = ParseTreeWalker()
    walker.walk(semantico_listener, tree)

    resultados_terminal.delete("1.0", tk.END)
    codigo_intermedio.delete("1.0", tk.END)
    codigo_python.delete("1.0", tk.END)

    if error_listener.errors:
        for error in error_listener.errors:
            resultados_terminal.insert(tk.END, f"Error sintactico: {error}\n")
    elif semantico_listener.errores:
        for error in semantico_listener.errores:
            resultados_terminal.insert(tk.END, f"Error semántico: {error}\n")        
    else:
        codigo_intermedio.insert(tk.END, tree.toStringTree(recog=parser) + '\n')
        js_listener = VictorToPyhtonListener()
        walker.walk(js_listener, tree)
        codigo_python.insert(tk.END, js_listener.output)      

class ErrorListener(ConsoleErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Linea {line}:{column} {msg}")


def compilar():
    exec(codigo_python.get("1.0",tk.END))


ventana = tk.Tk()
ventana.title("Compilador Victor Taveras 1-17-1007")

frame_entrada_tokens = tk.Frame(ventana)
frame_entrada_tokens.pack(side="top", fill=tk.BOTH, expand=True)

frame_victorino= tk.Frame(frame_entrada_tokens)
frame_victorino.pack(side="left", fill=tk.BOTH, expand=True)

frame_codigo_python= tk.Frame(frame_entrada_tokens)
frame_codigo_python.pack(side="right", fill=tk.BOTH, expand=True)

frame_codigo_intermedio= tk.Frame(frame_entrada_tokens)
frame_codigo_intermedio.pack(side="right", fill=tk.BOTH, expand=True)




frame_token= tk.Frame(frame_entrada_tokens)
frame_token.pack(side="right", fill=tk.BOTH, expand=True)

etiqueta_entrada = tk.Label(frame_victorino, text="Ingrese código Victorino:")
etiqueta_entrada.pack(side="top")

entrada_texto = tk.Text(frame_victorino, height=20, width=40)
entrada_texto.pack(side="bottom", expand=True)


etiqueta_token = tk.Label(frame_token, text="TOKENS:")
etiqueta_token.pack(side="top")
# Crear la tabla de tokens
tabla_tokens = ttk.Treeview(frame_token, columns=("Type", "Token"), show="headings")
tabla_tokens.heading("Type", text="Type")
tabla_tokens.heading("Token", text="Token")
tabla_tokens.pack(side="right", fill=tk.BOTH)



etiqueta_token = tk.Label(frame_codigo_intermedio, text="Codigo Intermedio:")
etiqueta_token.pack(side="top")
codigo_intermedio = tk.Text(frame_codigo_intermedio, height=20, width=40)
codigo_intermedio.pack(side="bottom", expand=True)


etiqueta_token = tk.Label(frame_codigo_python, text="Codigo Python:")
etiqueta_token.pack(side="top")
codigo_python = tk.Text(frame_codigo_python, height=20, width=40)
codigo_python.pack(side="bottom", expand=True)




boton_analizar = tk.Button(ventana, text="Analizar", command=analizar)
boton_analizar.pack()
boton_compilar = tk.Button(ventana, text="Compilar", command=compilar)
boton_compilar.pack()

frame_bottom= tk.Frame(ventana)
frame_bottom.pack(side="bottom", fill=tk.BOTH, expand=True)

frame_terminal= tk.Frame(frame_bottom)
frame_terminal.pack(side="right", fill=tk.BOTH, expand=True)

terminal = tk.Label(frame_terminal, text="Terminal")
terminal.pack(side="top")

resultados_terminal = tk.Text(frame_terminal, height=10, width=30, background="black", foreground="white")
resultados_terminal.pack(side="bottom", fill="both")

frame_buttons=tk.Frame(ventana)
frame_bottom.pack(side="left", fill=tk.BOTH, expand=True)




def limpiar_tabla_tokens():
    # Limpiar la tabla de tokens
    for row in tabla_tokens.get_children():
        tabla_tokens.delete(row)

def obtener_tokens(lexer):
    tokens = []
    while True:
        token = lexer.nextToken()
        if token.type == Token.EOF:
            break
        tokens.append(token)
    return tokens
def mostrar_tokens_en_tabla(tokens,lexer):
    for token in tokens:
        tipo = lexer.symbolicNames[token.type]
        valor = token.text
        tabla_tokens.insert("", "end", values=(tipo, token.type, valor))


ventana.mainloop()