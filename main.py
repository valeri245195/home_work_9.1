def input_error(func):

    def wrapper(*args, **kwargs):
        #print('penis')
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return str(e)

    return wrapper


# Словник для зберігання контактів (ім'я: телефон)
contacts = {}


# Декоратор для обробки помилок вводу
@input_error
def handle_hello():
    return "How can I help you?"


@input_error
def handle_add(command):
    # Розбиваємо введену команду на частини
    _, name, phone = command.split()
    # Зберігаємо контакт в словнику
    if name in contacts:

        return 'This contact already has a phone number'
    contacts[name] = phone
    return f"Contact {name} added with phone {phone}"


@input_error
def handle_change(command):
    _, name, phone = command.split()
    # Міняємо номер телефону для існуючого контакту
    contacts[name] = phone
    return f"Phone number for contact {name} changed to {phone}"


@input_error
def handle_phone(command):
    _, name = command.split()
    # Виводимо номер телефону для зазначеного контакту
    return f"The phone number for contact {name} is {contacts[name]}"


@input_error
def handle_show_all():
    if not contacts:
        return "No contacts available."

    # Виводимо всі збережені контакти
    result = "Contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def main():
    while True:
        # Користувач вводить команду
        user_input = input("Enter a command: ").lower()

        # Перевірка на команду для завершення роботи бота
        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break

        # Обробка команд за допомогою відповідних функцій-обработчиків
        if user_input == "hello":
            print(handle_hello())

        elif user_input.startswith("add "):
            print(handle_add(user_input))

        elif user_input.startswith("change "):
            print(handle_change(user_input))

        elif user_input.startswith("phone "):
            print(handle_phone(user_input))

        elif user_input == "show all":
            print(handle_show_all())

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
