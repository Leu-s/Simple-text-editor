import tkinter as tk
from tkinter .filedialog import askopenfilename
from tkinter .filedialog import asksaveasfilename


def open_file():
    """Открывает файл для редактирования"""
    filepath = askopenfilename(
        filetypes=[('Text files', '*.txt'), ('All Files', '*.*')]
    )
    if not filepath:
        return
    txt_edit.delete('1.0', tk.END)
    with open(filepath, 'r') as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f'Simple text editor - {filepath}')


def save_file():
    """Сохраняем текущий файл как новый файл."""
    filepath = asksaveasfilename(
        defaultextension='txt',
        filetypes=[('Text files', '*.txt'),
                   ('All files', "*.*")]
    )
    if not filepath:
        return
    with open(filepath, 'w') as output_file:
        text = txt_edit.get('1.0', tk.END)
        output_file.write(text)
    window.title(f'Simple text editor - {filepath}')


window = tk.Tk()
window.title('Simple text editor')

window.rowconfigure(0, minsize=400, weight=1)  # (<Высота первой строки, пикс>, <minsize>, <weight>)
window.columnconfigure(1, minsize=400, weight=1)
window.minsize(width=580, height=65)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(master=window, bg='#2D2A2E')
btn_open = tk.Button(fr_buttons, text='Open', bg='#EDD864', command=open_file)
btn_save = tk.Button(fr_buttons, text='Save as...', bg='#EDD864', command=save_file)

btn_open.grid(row=1, column=0, sticky='ew', padx=5, pady=0)
btn_save.grid(row=0, column=0, sticky='ew', padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky='ns')
txt_edit.grid(row=0, column=1, sticky='nsew')

window.mainloop()

