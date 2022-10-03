import pandas as pd
from modeltools.preprocessing import get_numerical_features

def test_get_numerical_features_simple():
    """En este vamos a probar que logra distiguir
    entre cadenas de texto y numeros enteros"""

    df = pd.DataFrame({
        "numerica": [5],
        "categorica":["rojo"]
    })
    
    assert get_numerical_features(df) == ["numerica"]


def test_get_numerical_features_empty():
    """En este vamos a probar que logra distiguir
    entre cadenas de texto y numeros enteros"""

    df = pd.DataFrame({
        "categorica":["rojo"]
    })
    
    assert get_numerical_features(df) == []


def test_get_numerical_features_zero_columns():
    """se devuelve una lista vacia si el df"""

    df = pd.DataFrame()
    
    assert get_numerical_features(df) == []



def test_get_numerical_features_zero_rows():
    """se devuelve una lista vacia si el df"""

    df = pd.DataFrame({
        "numerica": pd.Series(dtype=int)
    })
    
    assert get_numerical_features(df) == ["numerica"]


def test_get_numerical_features_int_and_float():
    """funciona correctamente con columna integer y una float"""

    df = pd.DataFrame({
        "numerica": [5],
        "numerica2": [5.02],
    })
    
    assert get_numerical_features(df) == ["numerica","numerica2"]


def test_get_numerical_features_columns_withoutname():
    """funciona correctamente con columnasnumericas sin nombre
    (columnas con numeros/posiciones"""


    df = pd.DataFrame([
        [1, "a"]
    ])

    assert get_numerical_features(df) == [0]

def test_get_numerical_features_complex():
    """funciona correctamente con numeros complejos"""

    df = pd.DataFrame({
        "compleja": [complex(3,5)]
    })

    assert get_numerical_features(df) == ['compleja']