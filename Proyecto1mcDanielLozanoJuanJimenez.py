import re
import tkinter as tk
from tkinter import messagebox
import struct

def float_to_binary(num):
    """Convierte un número de punto flotante a IEEE 754 (32 bits)."""
    return format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')

def int_to_binary(num):
    """Convierte un número entero a complemento a 2 (32 bits)."""
    if num < 0:
        num = (1 << 32) + num  # Complemento a 2
    return format(num, '032b')

def binary_to_float(binary_str):
    """Convierte una cadena binaria IEEE 754 a punto flotante."""
    return struct.unpack('!f', struct.pack('!I', int(binary_str, 2)))[0]

def binary_to_int(binary_str):
    """Convierte una cadena binaria en complemento a 2 a entero."""
    val = int(binary_str, 2)
    if val >= (1 << 31):
        val -= (1 << 32)
    return val

def tokenize(expr):
    """
    Separa la expresión en tokens (números y operadores) distinguiendo
    el signo negativo unario de la resta binaria.
    """
    # Separamos manteniendo los operadores
    parts = re.split(r'([+\-*/])', expr)
    # Quitamos espacios y cadenas vacías
    parts = [p.strip() for p in parts if p.strip() != '']
    tokens = []
    i = 0
    while i < len(parts):
        token = parts[i]
        # Si es un operador...
        if token in '+-*/':
            # Verificar si es un signo negativo unario:
            # Si es '-' y (es el primer token o el token previo es un operador)
            if token == '-' and (len(tokens) == 0 or tokens[-1] in '+-*/'):
                # Combinar con el siguiente token para formar el número negativo
                if i + 1 < len(parts):
                    tokens.append(token + parts[i+1])
                    i += 2
                    continue
            # En otro caso es un operador binario normal
            tokens.append(token)
            i += 1
        else:
            # Es un número normal
            tokens.append(token)
            i += 1
    return tokens

def do_operation(a, b, op):
    """
    Realiza la operación entre 'a' y 'b'. Si ambos son int se opera de forma entera,
    si al menos uno es float, se opera en punto flotante.
    """
    both_int = isinstance(a, int) and isinstance(b, int)

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b if both_int else float(a) * float(b)
    elif op == '/':
        # División: si ambos son enteros, se realiza división entera (//)
        return a // b if both_int else float(a) / float(b)

def evaluate_expression(expression):
    """
    Evalúa la expresión respetando la precedencia de operadores.
    Primero se resuelven las multiplicaciones y divisiones,
    luego las sumas y restas.

    Se respeta que si ambos operandos son enteros se usa la operación entera.
    """
    try:
        tokens = tokenize(expression)
        # Se espera que los tokens estén en forma: número, operador, número, ...
        # Separa números y operadores:
        numbers = []
        operators = []
        for i, token in enumerate(tokens):
            if i % 2 == 0:
                # Número: lo convertimos a float si tiene punto, sino a int
                num = float(token) if '.' in token else int(token)
                numbers.append(num)
            else:
                operators.append(token)

        # Paso 1: Resolver * y / (respeta la precedencia)
        temp_nums = [numbers[0]]
        temp_ops = []
        for i in range(len(operators)):
            op = operators[i]
            next_num = numbers[i+1]
            if op in ('*', '/'):
                prev_num = temp_nums.pop()
                res = do_operation(prev_num, next_num, op)
                temp_nums.append(res)
            else:
                temp_nums.append(next_num)
                temp_ops.append(op)

        # Paso 2: Resolver + y -
        result = temp_nums[0]
        idx = 0
        for op in temp_ops:
            idx += 1
            result = do_operation(result, temp_nums[idx], op)

        # Si el resultado es float pero equivalente a entero, lo convertimos a int
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        # Convertir el resultado a binario según corresponda
        if isinstance(result, float):
            bin_result = float_to_binary(result)
        else:
            bin_result = int_to_binary(result)

        return result, bin_result
    except Exception as e:
        return f"Error: {str(e)}", None

# Variable global para el historial
historial = []

def calculate():
    expression = entrada_expr.get()
    if not expression:
        messagebox.showwarning("Advertencia", "Ingrese una expresión")
        return

    result, binary_res = evaluate_expression(expression)

    if binary_res:
        resultado_var.set(f"{result}")
        resultado_bin_var.set(f"{binary_res}")
        # Agregar la operación al historial
        historial.append(f"{expression} = {result} ({binary_res})")
        actualizar_historial()
    else:
        resultado_var.set(f"Error: {result}")
        resultado_bin_var.set("")

def actualizar_historial():
    historial_texto.config(state=tk.NORMAL)
    historial_texto.delete("1.0", tk.END)
    for operacion in historial:
        historial_texto.insert(tk.END, operacion + "\n")
    historial_texto.config(state=tk.DISABLED)

# Interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Calculadora Aritmética")
root.geometry("550x520")
root.resizable(False, False)

# Paleta de colores
COLOR_BG = "#f5f7fa"
COLOR_ACCENT = "#3498db"
COLOR_TEXT = "#34495e"
COLOR_BTN = "#4da6ff"
COLOR_BTN_TEXT = "white"
COLOR_TITLE = "#b06000"
COLOR_FRAME = "#e1e8ed"
COLOR_BINARY = "#2c3e50"

# Configurar estilo general
root.configure(bg=COLOR_BG)

# Frame principal
main_frame = tk.Frame(root, bg=COLOR_BG, padx=20, pady=10)
main_frame.pack(fill=tk.BOTH, expand=True)

# Título de la aplicación
titulo_app = tk.Label(
    main_frame,
    text="Calculadora Aritmética y Binaria",
    font=("Arial", 16, "bold"),
    fg=COLOR_TITLE,
    bg=COLOR_BG
)
titulo_app.pack(pady=(10, 20))

# Sección de expresión
expr_frame = tk.Frame(main_frame, bg=COLOR_BG)
expr_frame.pack(fill=tk.X, pady=5)

expr_label = tk.Label(
    expr_frame,
    text="Expresión:",
    font=("Arial", 12, "bold"),
    fg=COLOR_TEXT,
    bg=COLOR_BG,
    anchor="w"
)
expr_label.pack(fill=tk.X)

entrada_expr = tk.Entry(
    expr_frame,
    font=("Arial", 12),
    bg="white",
    fg=COLOR_TEXT,
    relief=tk.FLAT,
    highlightthickness=1,
    highlightbackground="#dcdde1",
    highlightcolor=COLOR_ACCENT,
    insertbackground=COLOR_TEXT
)
entrada_expr.pack(fill=tk.X, ipady=8, pady=(5, 0))

# Frame para el botón (centrado)
btn_frame = tk.Frame(main_frame, bg=COLOR_BG)
btn_frame.pack(pady=15)

# Botón calcular
boton_calcular = tk.Button(
    btn_frame,
    text="Calcular",
    command=calculate,
    font=("Arial", 12),
    bg=COLOR_BTN,
    fg=COLOR_BTN_TEXT,
    activebackground="#2980b9",
    activeforeground="white",
    relief=tk.FLAT,
    padx=20,
    pady=5,
    cursor="hand2"
)
boton_calcular.pack()

# Sección de resultado decimal
result_frame = tk.Frame(main_frame, bg=COLOR_BG)
result_frame.pack(fill=tk.X, pady=5)

result_label = tk.Label(
    result_frame,
    text="Resultado Decimal:",
    font=("Arial", 12, "bold"),
    fg=COLOR_TEXT,
    bg=COLOR_BG,
    anchor="w"
)
result_label.pack(fill=tk.X)

resultado_var = tk.StringVar()
resultado_var.set("")
resultado_entry = tk.Entry(
    result_frame,
    textvariable=resultado_var,
    font=("Arial", 12),
    bg="white",
    fg=COLOR_TEXT,
    relief=tk.FLAT,
    highlightthickness=1,
    highlightbackground="#dcdde1",
    highlightcolor=COLOR_ACCENT,
    readonlybackground="#f8f9fa",
    state="readonly"
)
resultado_entry.pack(fill=tk.X, ipady=8, pady=(5, 0))

# Sección de resultado binario
result_bin_frame = tk.Frame(main_frame, bg=COLOR_BG)
result_bin_frame.pack(fill=tk.X, pady=5)

result_bin_label = tk.Label(
    result_bin_frame,
    text="Representación Binaria:",
    font=("Arial", 12, "bold"),
    fg=COLOR_TEXT,
    bg=COLOR_BG,
    anchor="w"
)
result_bin_label.pack(fill=tk.X)

resultado_bin_var = tk.StringVar()
resultado_bin_var.set("")
resultado_bin_entry = tk.Entry(
    result_bin_frame,
    textvariable=resultado_bin_var,
    font=("Courier New", 11), # Fuente monoespaciada para mejor visualización binaria
    bg="white",
    fg=COLOR_BINARY,
    relief=tk.FLAT,
    highlightthickness=1,
    highlightbackground="#dcdde1",
    highlightcolor=COLOR_ACCENT,
    readonlybackground="#f8f9fa",
    state="readonly"
)
resultado_bin_entry.pack(fill=tk.X, ipady=8, pady=(5, 0))

# Sección de historial
hist_label = tk.Label(
    main_frame,
    text="Historial de operaciones:",
    font=("Arial", 12, "bold"),
    fg=COLOR_TEXT,
    bg=COLOR_BG,
    anchor="w"
)
hist_label.pack(fill=tk.X, pady=(15, 5))

# Frame para el historial
frame_historial = tk.Frame(
    main_frame,
    bg=COLOR_FRAME,
    highlightthickness=1,
    highlightbackground="#dcdde1",
    highlightcolor=COLOR_ACCENT
)
frame_historial.pack(fill=tk.BOTH, expand=True)

# Scrollbar para el historial
scrollbar = tk.Scrollbar(frame_historial)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Área de texto para el historial
historial_texto = tk.Text(
    frame_historial,
    height=10,
    font=("Arial", 11),
    bg=COLOR_FRAME,
    fg=COLOR_TEXT,
    relief=tk.FLAT,
    bd=0,
    padx=10,
    pady=10,
    yscrollcommand=scrollbar.set
)
historial_texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=historial_texto.yview)
historial_texto.config(state=tk.DISABLED)

# Descripción del funcionamiento
info_frame = tk.Frame(main_frame, bg=COLOR_BG)
info_frame.pack(fill=tk.X, pady=(10, 0))

info_label = tk.Label(
    info_frame,
    text="• Enteros: representación en complemento a 2 (32 bits)\n• Flotantes: representación IEEE 754 (32 bits)",
    font=("Arial", 9),
    fg="#7f8c8d",
    bg=COLOR_BG,
    justify=tk.LEFT
)
info_label.pack(anchor="w")

# Añadir teclas de acceso rápido
def pulsar_enter(event):
    calculate()

root.bind('<Return>', pulsar_enter)

# Centrar la ventana en la pantalla
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Poner foco en la entrada al iniciar
entrada_expr.focus_set()

root.mainloop()
