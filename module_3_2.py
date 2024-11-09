def send_email(message, recipient, *, sender="university.help@gmail.com"):
    valid = ('.com', '.ru', '.net')

    def is_valid_email(email):
        return '@' in email and email.endswith(valid)

    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return

    # Здесь может быть код для отправки письма
    print(f"Письмо отправлено с адреса {sender} на адрес {recipient} с сообщением: {message}")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')