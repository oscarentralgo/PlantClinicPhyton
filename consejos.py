# consejos.py - Módulo de consejos para el cuidado de plantas

consejos = [
    {
        "consejo": "Riego Adecuado",
        "descripción": "Riega cuando el suelo esté seco al tacto. No todas las plantas necesitan la misma cantidad de agua.",
        "frecuencia": "2-3 veces por semana (varía según la planta)"
    },
    {
        "consejo": "Luz Solar",
        "descripción": "La mayoría de plantas necesitan 6-8 horas de luz indirecta. Evita luz solar directa en plantas delicadas.",
        "frecuencia": "Diario"
    },
    {
        "consejo": "Temperatura",
        "descripción": "Mantén temperaturas entre 15-25°C. Evita cambios bruscos de temperatura.",
        "frecuencia": "Constante"
    },
    {
        "consejo": "Humedad",
        "descripción": "Aumenta la humedad nebulizando las hojas o colocando la maceta sobre agua.",
        "frecuencia": "Según el tipo de planta"
    },
    {
        "consejo": "Abono",
        "descripción": "Aplica fertilizante durante la época de crecimiento (primavera-verano).",
        "frecuencia": "Cada 2-4 semanas en primavera y verano"
    },
    {
        "consejo": "Poda",
        "descripción": "Elimina hojas y ramas muertas para favorecer el crecimiento de nuevas ramas.",
        "frecuencia": "Según sea necesario"
    }
]

def obtener_consejos():
    return consejos
