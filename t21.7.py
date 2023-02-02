import re


""" T21.7 У текстовому файлі міститься текст українською мовою. «Стиснути»
цей текст, видаливши у словах усі голосні літери. Якщо у слові тільки
голосні літери або слово має довжину не більше 2 символів, - голосні не
видаляти. Використати регулярні вирази. """


# Усі голосні букви
LETTERS = r"[АОУЕІИЇЯЮЄаоуеиіїяює]+"
# Усі не укр літери (для того аби замінити усе зайве замість літер, наприклад: точки, коми, кавички)
NON_WORDS = r"[^а-щА-ЩЬьЮюЯяЇїІіЄєҐґ]+"
# Для функції valid_word, аби очистити слова від зайвих знаків та голосних
TO_CLEAR = LETTERS + '|' + NON_WORDS


def valid_word(word):
    # Очищуємо слова від зайвих знаків та голосних
    clear_word = re.sub(TO_CLEAR, "", word)
    return len(word) > 2 and len(set(clear_word)) != 0


if __name__ == "__main__":
    with open("text_21.7", "r+", encoding="utf-8") as f:
        f_contents = f.read()
        f_words = re.split(" ", f_contents)
        f_words = [re.sub(LETTERS, '', word) if valid_word(word) else word for word in f_words]
        f.seek(0)
        result_text = ' '.join(f_words)
        f.write(result_text)
        f.truncate()
        print(result_text)


