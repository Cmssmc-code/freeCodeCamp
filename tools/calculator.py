import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculatrice")
        self.geometry("300x400")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        self.display_var = tk.StringVar()
        display = tk.Entry(self, textvariable=self.display_var, font=("Arial", 24), justify='right', bd=10, relief=tk.RIDGE)
        display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            action = lambda x=text: self.on_button_click(x)
            tk.Button(self, text=text, width=5, height=2, font=("Arial", 18),
                      command=action).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        for i in range(6):
            self.rowconfigure(i, weight=1)
            if i < 4:
                self.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.display_var.set('')
        elif char == '=':
            try:
                result = str(eval(self.display_var.get()))
                self.display_var.set(result)
            except Exception:
                self.display_var.set('Error')
        else:
            current = self.display_var.get()
            self.display_var.set(current + char)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
