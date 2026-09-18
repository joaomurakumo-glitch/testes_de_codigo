from senha import validar_senha
import pytest

@pytest.mark.parametrize("senha, esperado", [
    ("123", False),
    ("1234567", False),
    ("12345678", True),
    ("123456789", True)
]
)
def test_validar_senhas(senha, esperado):

    resultado = validar_senha(senha)
    assert resultado == esperado

