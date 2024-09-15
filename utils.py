"""
utils.py
"""
from settings import (AFFIRMATIVE_VALUES, NEGATIVE_VALUES)


def map_response(response):
    """
    Identificar y convertir respuestas
    """

    # Convertir todo a minúsculas
    response = str(response).lower()
    if response in AFFIRMATIVE_VALUES:
        return 'si'
    elif response in NEGATIVE_VALUES:
        return 'no'
    return 'otro'


def show_label(pct: float, allvals: list):
    """
    Función para personalizar etiquetas en gráfico
    """
    total = sum(allvals)
    absolute = int(pct / 100. * total)
    return f'{absolute}\n({pct:.1f}%)'
