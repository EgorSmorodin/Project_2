import tkinter as tk
from tkinter import messagebox
import module_generator

class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор паролей")

        self.generator = None

        # Заголовок
        self.title_label = tk.Label(root, text="Генератор паролей", font=("Arial", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Метка для выбора длины пароля
        self.length_label = tk.Label(root, text="Длина пароля:")
        self.length_label.grid(row=1, column=0, padx=10, pady=5)

        # Поле ввода для длины пароля
        self.password_length = tk.Entry(root, width=10)
        self.password_length.grid(row=1, column=1, padx=10, pady=5)

        # Метка для выбора использования Unicode символов
        self.emoji_label = tk.Label(root, text="Использовать Unicode символы?")
        self.emoji_label.grid(row=2, column=0, padx=10, pady=5)

        # Поле для выбора Unicode (1 - да, 0 - нет)
        self.emoji_var = tk.IntVar()
        self.emoji_checkbox = tk.Checkbutton(root, text="Да", variable=self.emoji_var)
        self.emoji_checkbox.grid(row=2, column=1, padx=10, pady=5)

        # Кнопка для генерации пароля
        self.generate_button = tk.Button(root, text="Генерировать", command=self.generate_password)
        self.generate_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Поле для вывода сгенерированного пароля
        self.password_entry = tk.Entry(root, width=30)
        self.password_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        # Кнопка для сохранения пароля
        self.save_button = tk.Button(root, text="Сохранить пароль", command=self.save_password)
        self.save_button.grid(row=5, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            length = int(self.password_length.get())
            if length < 6:
                messagebox.showwarning("Ошибка", "Длина пароля должна быть хотя бы 6 символов!")
                return

            emoji = self.emoji_var.get()

            # Создаем объект генератора паролей
            self.generator = module_generator.PasswordGenerator(length, emoji)
            password = self.generator.generate()

            # Отображаем сгенерированный пароль
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)

        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректную длину пароля!")

    def save_password(self):
        if self.generator is None:
            messagebox.showwarning("Ошибка", "Сначала сгенерируйте пароль!")
            return

        website = self.ask_for_input("Введите название сайта:")
        if website is None:
            return

        login = self.ask_for_input("Введите логин аккаунта:")
        if login is None:
            return

        # Сохраняем пароль
        self.generator.save(website, login)
        messagebox.showinfo("Успех", "Пароль успешно сохранен!")

    def ask_for_input(self, prompt):
        input_window = tk.Toplevel(self.root)
        input_window.title(prompt)

        label = tk.Label(input_window, text=prompt)
        label.pack(padx=10, pady=10)

        entry = tk.Entry(input_window, width=30)
        entry.pack(padx=10, pady=10)

        def on_submit():
            user_input = entry.get()
            if user_input.strip():
                input_window.destroy()
                return user_input
            else:
                messagebox.showwarning("Ошибка", "Поле не может быть пустым!")
                return None

        submit_button = tk.Button(input_window, text="Подтвердить", command=on_submit)
        submit_button.pack(padx=10, pady=10)

        input_window.wait_window(input_window)  # Ожидаем, пока окно не закроется

        return None