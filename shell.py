import basic

while True:
    text = input('basic > ')
    result, error = basic.run('<stdin>', text)

    if not error:
        print(result)
    else:
        print(error.as_string())