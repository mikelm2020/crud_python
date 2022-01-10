PASSWORD = '12345'


def password_required(func):
    def wrapper():
        password = input('Which is your password? ')

        if password == PASSWORD:
            return func()
        else:
            print('the password is not correct')

    return wrapper


@password_required
def needs_password():
    print('The password is correct')


def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()
    return wrapper


@upper
def say_my_name(name):
    return 'Hola, {}'.format(name)


if __name__ == '__main__':
    #needs_password()
    print(say_my_name('David'))
