import string, random, os

class PasswordGenerator:
    def __init__(self, length, emoji):
        self.length = length
        self.emoji = emoji
        self.password = ''
        # Стандартный набор символов
        self.Lists = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    # Функция для генерации пароля с двумя режимами
    def generate(self):
        character_pool = self.Lists
        if self.emoji == 1:
            unicode_characters = ''.join(chr(i) for i in range(10000, 11000))
            character_pool += unicode_characters
        password = ''.join(random.choices(character_pool, k=self.length))
        self.password = password
        return password

    # Функция сохранения пароля в папку программы
    def save(self, website, login):
        os.makedirs(website, exist_ok=True)
        file_path = os.path.join(website, f"{login}.txt")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"Логин:\n{login}\n")
            file.write(f"Пароль:\n{self.password}\n")
