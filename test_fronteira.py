from fronteira import classificar_idade
import pytest

#def test_menor_de_idade():
#    assert classificar_idade(17) == "Menor de idade"

#def test_maior_de_idade():
#    assert classificar_idade(18) == "Maior de idade"

#def test_idade_10():
#    assert classificar_idade(10) == "Menor de idade"


@pytest.mark.parametrize(
    "idade, resultado_esperado",
    [
        (10, "Menor de idade"),
        (17, "Menor de idade"),
        (18, "Maior de idade"),
        (21, "Maior de idade"),
        (30, "Maior de idade"),

    ]
)
def test_classificar_idade(idade, resultado_esperado):
    resultado = classificar_idade(idade)
    assert resultado == resultado_esperado