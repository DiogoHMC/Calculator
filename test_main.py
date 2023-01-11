from main.incremento import Opera, Error

import pytest

@pytest.mark.parametrize("op1, op2, resp", [(3,2,5)])
def test_somador(op1, op2, resp):
    somador=Opera()
    somador= somador.soma(op1, op2)
    assert somador == resp

@pytest.mark.parametrize("op1, op2, resp", [(5,2,3)])
def test_sub(op1, op2, resp):
    subtracao=Opera()
    subtracao=subtracao.sub(op1, op2)
    assert subtracao == resp

@pytest.mark.parametrize("op1, op2, resp", [(3,2,6)])
def test_mult(op1, op2, resp):
    multplicacao=Opera()
    multplicacao=multplicacao.mult(op1, op2)
    assert multplicacao == resp

@pytest.mark.parametrize("op1, op2, resp", [(8,4,2)])
def test_div(op1, op2, resp):
    divisao=Opera()
    divisao=divisao.div(op1, op2)
    assert divisao == resp

def test_somaString():
    somador=Opera()
    with pytest.raises(Error):
        somador.soma(-2, -4)
