# diagnósticos.py - Módulo de diagnósticos de enfermedades comunes

diagnosticos = [
    {
        "enfermedad": "Mildiu (Oídio)",
        "síntomas": "Polvo blanco o gris en hojas, flores y tallos",
        "causa": "Hongo que prospera en ambientes húmedos y cálidos",
        "tratamiento": "Aplicar fungicida, mejorar ventilación, reducir humedad"
    },
    {
        "enfermedad": "Roya",
        "síntomas": "Manchas anaranjadas o marrones en el envés de las hojas",
        "causa": "Infección fúngica",
        "tratamiento": "Remover hojas infectadas, fungicida, mejorar ventilación"
    },
    {
        "enfermedad": "Mancha Negra",
        "síntomas": "Manchas negras circulares con halo amarillo",
        "causa": "Hongo que afecta principalmente a rosas",
        "tratamiento": "Fungicida, remover hojas infectadas, evitar riego por aspersión"
    },
    {
        "enfermedad": "Pudrición de Raíces",
        "síntomas": "Planta marchita, raíces oscuras y blandas",
        "causa": "Exceso de agua y suelo mal drenado",
        "tratamiento": "Replanta en suelo seco, reduce el riego, mejora drenaje"
    },
    {
        "enfermedad": "Plagas - Ácaros",
        "síntomas": "Hojas pálidas con puntitos blancos y telarañas finas",
        "causa": "Parásitos microscópicos",
        "tratamiento": "Acaricida, aumentar humedad, mantener limpias las hojas"
    }
]

def obtener_diagnosticos():
    return diagnosticos
