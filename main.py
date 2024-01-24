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
def handle_hello(command):
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
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for contact {name} changed to {phone}"
    return 'That name is not in the contact book'


@input_error
def handle_phone(command):
    _, name = command.split()
    # Виводимо номер телефону для зазначеного контакту
    if name in contacts:
        return f"The phone number for contact {name} is {contacts[name]}"
    return f"Name {name} is not in the contact book"


@input_error
def handle_show_all(command):
    if not contacts:
        return "No contacts available."

    # Виводимо всі збережені контакти
    result = "Contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


@input_error
def handle_end(command):
    return 'Good bye!'


ACTIONS = {
    'hello ': handle_hello,
    'add ': handle_add,
    'change ': handle_change,
    'phone ': handle_phone,
    "show all ": handle_show_all,
    'good night ': handle_end,
    'exit ': handle_end,
    'close ': handle_end
}


@input_error
def bad_commands(command):
    return 'Bad command'


@input_error
def get_hendler(user_input):
    for action in ACTIONS:
        if user_input.startswith(action):
            return ACTIONS[action]
    return bad_commands


def main():
    while True:
        # Користувач вводить команду
        user_input = f"{input('Enter a command: ').lower()} "
        handler = get_hendler(user_input)
        result = handler(user_input)
        print(result)
        if result == 'Good bye!':

            break


if __name__ == "__main__":
    main()
