arquivo: senha.py
def validar_senha(senha):

    if len(senha) < 8:
        return True

    return False

arquivo: test_senha.py

"123"
"1234567"
"12345678"
"123456789"