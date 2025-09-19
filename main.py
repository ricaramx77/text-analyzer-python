import tkinter as tk
from tkinter import scrolledtext, messagebox
from text_utils import count_words, term_frequency, find_palindromes

class TextAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Analyzer")
        self.root.geometry("500x500")

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
        self.text_area.pack(pady=10)

        self.analyze_btn = tk.Button(root, text="Analyze", command=self.analyze_text)
        self.analyze_btn.pack(pady=5)

        self.result_label = tk.Label(root, text="Results:", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=5)
        self.result_box = tk.Text(root, height=10, width=60, state=tk.DISABLED)
        self.result_box.pack(pady=5)

    def analyze_text(self):
        text = self.text_area.get("1.0", tk.END)
        word_count = count_words(text)
        freq = term_frequency(text)
        palindromes = find_palindromes(text)

        result = f"Word count: {word_count}\n\n"
        result += "Term frequency:\n"
        for word, count in freq.most_common():
            result += f"  {word}: {count}\n"
        result += "\nPalindromes:\n"
        result += ", ".join(palindromes) if palindromes else "None"

        self.result_box.config(state=tk.NORMAL)
        self.result_box.delete("1.0", tk.END)
        self.result_box.insert(tk.END, result)
        self.result_box.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextAnalyzerApp(root)
    root.mainloop()
def saludar(nombre: str) -> str:

    return f"Hola, {nombre}!"



if __name__ == "__main__":

    print(saludar("Ricardo"))
