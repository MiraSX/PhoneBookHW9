

# Тут декоратор, который проверяет ошибки ввода.
def input_error(func):
    def inner(*args, contacts):
        try:
            return func(*args, contacts)
        except (KeyError, ValueError, IndexError) as e:
            return e
    return inner

# Ниже сделал функции для записи данных + добавил немного вывода текста в консоль для понятия происходящего
def hello(*args, **kwargs):
    return 'How can I help you?'

@input_error
def add(name, number, contacts):
    contacts[name] = number
    return (f'User {name} with {number} was added')

@input_error
def change(name, number, contacts):
    if not name in contacts:
        return (f'There is no {name}')
    else:
        contacts[name] = number
        return (f'{name} was changed!')

@input_error
def phone (name, contacts):
    if name in contacts:
        return(f'{name}\'s number is {contacts[name]}')
    else:
        return (f'There is no {name}')
    
def show_all (*args, contacts):
    return ('\n'.join([f'{name} {number}' for name,number in contacts.items()]))


# Основная работа с вводом
def main():
    contacts = {}
    
    while True:
        # переводим ввод в нижний регистр и разбиваем в лист для отделения команды от данных.
        inp_command = input('Enter command: ').lower().split()
        if not inp_command:
            continue
        # команды для выхода 
        if inp_command[0] == "good bye" or inp_command[0] == "close" or inp_command[0] == "exit":
            break
        # список основных команд 
        COMMANDS = {'hello': hello,
                    'add': add,
                    'change': change,
                    'phone': phone,
                    'show': show_all}
        # сама инициализация команды 
        if inp_command[0] in COMMANDS:
            handler = COMMANDS[inp_command[0]]
            print(handler(*inp_command[1:], contacts=contacts))
        else:
            print('Unknown command')
            continue

        
            

if __name__ == '__main__':
    main()