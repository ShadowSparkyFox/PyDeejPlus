import tkinter as tk
from tkinter import ttk


def prompt_user(values, message):
    root = tk.Tk()  # use Toplevel() instead of Tk()

    root.title("PyDeejPlus - Glassfox BV")
    root.geometry("300x50")
    root.resizable(False, False)
    # @TODO: figure out ico packaging and such
    root.iconbitmap('C:/Users/josip/PyDeejPlus/src/resources/glassfox.ico')
    ttk.Label(root, text=message).pack()
    box_value = tk.StringVar()
    combo = ttk.Combobox(root, textvariable=box_value, values=values)
    combo.pack()
    combo.bind('<<ComboboxSelected>>', lambda _: root.destroy())
    root.grab_set()
    root.wait_window(root)  # wait for itself destroyed, so like a modal dialog
    return box_value.get()
