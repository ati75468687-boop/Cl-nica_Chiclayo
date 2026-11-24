from modelo import RegistroTriaje


# PRUEBA 1: Clasificacion por temperatura
def probar_clasificacion():

    # Caso de hipotermia
    paciente1 = RegistroTriaje("12345678", 35.5, 80)
    assert paciente1.clasificar() == "ALERTA: HIPOTERMIA"

    # Caso de temperatura normal
    paciente2 = RegistroTriaje("12345678", 36.8, 75)
    assert paciente2.clasificar() == "SIGNOS VITALES NORMALES"

    # Caso de fiebre
    paciente3 = RegistroTriaje("12345678", 38.0, 100)
    assert paciente3.clasificar() == "ALERTA: FIEBRE / DERIVAR"

    # Comprobacion de los limites
    paciente4 = RegistroTriaje("12345678", 36.0, 80)
    assert paciente4.clasificar() == "SIGNOS VITALES NORMALES"

    paciente5 = RegistroTriaje("12345678", 37.5, 80)
    assert paciente5.clasificar() == "SIGNOS VITALES NORMALES"


# PRUEBA 2: Validacion de datos
def probar_validaciones():

    casos_invalidos = [
        (None, 36.5, 80),
        ("", 36.5, 80),
        ("12345678", "abc", 80),
        ("12345678", 36.5, 0),
        ("12345678", float("inf"), 80),
        ("12345678", float("nan"), 80)
    ]

    for datos in casos_invalidos:

        try:
            RegistroTriaje(*datos)

        except ValueError:
            pass

        else:
            raise AssertionError(
                f"Se aceptaron datos invalidos: {datos}"
            )


# PRUEBA 3: Verificar los datos registrados
def probar_datos():

    paciente = RegistroTriaje("12345678", 37.0, 80)

    resultado = paciente.obtener_datos()

    assert resultado["paciente_dni"] == "12345678"
    assert resultado["temperatura"] == 37.0
    assert resultado["frecuencia_cardiaca"] == 80.0
    assert resultado["clasificacion"] == "SIGNOS VITALES NORMALES"


# EJECUCION DE TODAS LAS PRUEBAS
if __name__ == "__main__":

    probar_clasificacion()
    print("[OK] Pruebas de clasificacion superadas.")

    probar_validaciones()
    print("[OK] Pruebas de validacion superadas.")

    probar_datos()
    print("[OK] Pruebas de registro de datos superadas.")

    print("\nTODAS LAS PRUEBAS UNITARIAS FUERON SUPERADAS.")