import pytest
from eficiencia_motor import calcular_eficiencia, classificar_eficiencia, analise_motor

# -----------------------------
# Testes do cálculo de eficiência
# -----------------------------
def test_calcular_eficiencia_valor_correto():
    assert calcular_eficiencia(900, 1000) == 90.0

def test_calcular_eficiencia_arredondamento():
    assert calcular_eficiencia(855, 1000) == 85.5

def test_calcular_eficiencia_entrada_zero():
    with pytest.raises(ValueError):
        calcular_eficiencia(800, 0)

# -----------------------------
# Testes da classificação de eficiência
# -----------------------------
def test_classificacao_ie1():
    assert classificar_eficiencia(75.0) == "IE1 - Baixa eficiência"

def test_classificacao_ie2():
    assert classificar_eficiencia(85.0) == "IE2 - Eficiência média"

def test_classificacao_ie3():
    assert classificar_eficiencia(92.0) == "IE3 - Alta eficiência"

# -----------------------------
# Teste de integração
# -----------------------------
def test_analise_motor_integracao():
    eficiencia, classificacao = analise_motor(880, 1000)
    assert eficiencia == 88.0
    assert classificacao == "IE2 - Eficiência média"
