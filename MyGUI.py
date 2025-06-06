import tkinter as tk
from tkinter import ttk, messagebox

class Analyze_DNA:
    def __init__(self):
        self.size = None
        self.gc_content = None
        self.start_codons = None
        self.stop_codons = None

    def size_of(self, sequence):
        sequence = sequence.upper()
        self.size = len(sequence)
        return self.size

    def gc_content_of(self, sequence):
        sequence = sequence.upper()
        self.gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
        return round(self.gc_content, 2)

    def find_start_codons(self, sequence):
        sequence = sequence.upper()
        self.start_codons = []
        start_codons = ['ATG', 'GTG', 'TTG']
        for i in range(len(sequence) - 2):
            if sequence[i:i+3] in start_codons:
                self.start_codons.append(i)
        return self.start_codons

    def find_stop_codons(self, sequence):
        sequence = sequence.upper()
        self.stop_codons = []
        stop_codons = ['TAA', 'TAG', 'TGA']
        for i in range(len(sequence) - 2):
            if sequence[i:i+3] in stop_codons:
                self.stop_codons.append(i)
        return self.stop_codons

    def analyze_all(self, sequence):
        self.size_of(sequence)
        self.gc_content_of(sequence)
        self.find_start_codons(sequence)
        self.find_stop_codons(sequence)
        return {
            "Size": self.size,
            "GC_Content": self.gc_content,
            "Start_Codons": self.start_codons,
            "Stop_Codons": self.stop_codons
        }

class MyGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CMB2_gui")
        self.root.geometry("600x900")
        self.root.configure(bg="snow")

        self.headlineframe = tk.Frame(self.root, bg='pale turquoise', height=50, width=600)
        self.headlineframe.pack()
        self.headline = tk.Label(self.headlineframe, text="DNA Analyzer", font=("Arial", 16, 'bold'), fg="midnight blue")
        self.headline.pack()

        self.seq_box = tk.Text(self.root, font=('Arial', 12), height=5, width=40)
        self.seq_box.place(x=100, y=120)

        self.cal_button = tk.Button(self.root, text="CALCULATE", font=('Arial', 14), bg="steel blue", fg="midnight blue", command=self.show_results)
        self.cal_button.place(x=230, y=220)

        self.output_label = tk.Label(self.root, text="", bg="snow", font=('Arial', 12), justify="left")
        self.output_label.place(x=100, y=280)

        self.root.mainloop()

    def show_results(self):
        sequence = self.seq_box.get("1.0", tk.END).strip().upper()

        if not sequence:
            messagebox.showwarning("Input Error", "Please enter a DNA sequence.")
            return

        if any(base not in "ATGC" for base in sequence):
            messagebox.showerror("Invalid Sequence", "The sequence must contain only A, T, G, and C.")
            return

        analyzer = Analyze_DNA()
        try:
            result = analyzer.analyze_all(sequence)
            result_text = (
                f"Size: {result['Size']} bp\n"
                f"GC Content: {result['GC_Content']}%\n"
                f"Start Codons at: {result['Start_Codons']}\n"
                f"Stop Codons at: {result['Stop_Codons']}"
            )
            self.output_label.config(text=result_text)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
MyGUI()