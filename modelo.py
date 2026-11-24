from math import isfinite


class RegistroTriaje:

    def __init__(self, paciente_dni, temperatura, frecuencia_cardiaca):

        # Validar DNI del paciente
        if not isinstance(paciente_dni, str) or not paciente_dni.strip():
            raise ValueError("El DNI del paciente es obligatorio.")

        self.paciente_dni = paciente_dni.strip()

        # Validar datos numéricos
        try:
            self.temperatura = float(temperatura)
            self.frecuencia_cardiaca = float(frecuencia_cardiaca)
        except (TypeError, ValueError):
            raise ValueError("La temperatura y la frecuencia cardiaca deben ser numericas.")

        # Validar valores finitos
        if not isfinite(self.temperatura) or not isfinite(self.frecuencia_cardiaca):
            raise ValueError("Los valores deben ser numeros validos.")

        # Validar frecuencia cardiaca
        if self.frecuencia_cardiaca <= 0:
            raise ValueError("La frecuencia cardiaca debe ser mayor a cero.")

    # Metodo para clasificar al paciente
    def clasificar(self):

        if self.temperatura < 36.0:
            return "ALERTA: HIPOTERMIA"

        elif 36.0 <= self.temperatura <= 37.5:
            return "SIGNOS VITALES NORMALES"

        else:
            return "ALERTA: FIEBRE / DERIVAR"

    # Metodo para obtener los datos del paciente
    def obtener_datos(self):

        return {
            "paciente_dni": self.paciente_dni,
            "temperatura": self.temperatura,
            "frecuencia_cardiaca": self.frecuencia_cardiaca,
            "clasificacion": self.clasificar()
        }