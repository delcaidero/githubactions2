"""
este módulo contiene helpers par ael prerpocesamiento de datos
"""

import numpy as np
def prueba(a,b,c,d):
    """[summary]

    Args:
        a ([type]): [description]
        b ([type]): [description]
        c ([type]): [description]
        d ([type]): [description]
    """



def get_numerical_features(df):
    """
    devuelve una lista con el nombre de las coumnas que d

    param:
    type:

    Parámetros
    ----------



    Ejemplos
    --------

    >>> from modeltools.preprocessing import get_numerical_features
    >>> import pandas as pd
    >>> df = pd.DataFrame({'a':[1]})
    >>> get_numerical_features(df)
    ['a']



    """
    return list(df.select_dtypes(include=[np.number]).columns)