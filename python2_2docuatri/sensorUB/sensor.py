import statistics
from typing import List


class SensorTermico:
    """
    Representa un sensor térmico instalado en un servidor.
    
    Atributos:
        id_sensor (str): Identificador único del sensor.
        ubicacion (str): Ubicación física del sensor (ej. 'Rack A-4').
        __temperaturas (List[float]): Listado privado de lecturas térmicas.
    """

    def __init__(self, id_sensor: str, ubicacion: str, temperaturas: List[float] | None = None):
        """
        Inicializa un nuevo sensor térmico.

        Args:
            id_sensor (str): Identificador único del sensor.
            ubicacion (str): Ubicación física del sensor.
            temperaturas (List[float] | None): Lecturas iniciales opcionales.
        """
        self.id_sensor = id_sensor
        self.ubicacion = ubicacion
        self.__temperaturas = temperaturas if temperaturas is not None else []

    @property
    def temperaturas(self) -> List[float]:
        """
        Retorna una copia del listado de temperaturas para evitar mutaciones externas.

        Returns:
            List[float]: Copia del listado de lecturas térmicas.
        """
        return self.__temperaturas[:]

    def agregar_lectura(self, temp: float) -> bool:
        """
        Agrega una lectura térmica validando su rango lógico (0°C a 85°C).

        Args:
            temp (float): Temperatura a registrar.

        Returns:
            bool: True si la lectura es válida y se agrega; False si se descarta.
        """
        if 0 <= temp <= 85:
            self.__temperaturas.append(temp)
            return True
        return False

    def obtener_promedio(self) -> float:
        """
        Calcula el promedio histórico de temperaturas del sensor.

        Returns:
            float: Promedio de lecturas térmicas.

        Raises:
            ValueError: Si no existen lecturas registradas.
        """
        if not self.__temperaturas:
            raise ValueError("No hay lecturas registradas para calcular el promedio.")
        return statistics.mean(self.__temperaturas)

    def obtener_maxima(self) -> float:
        """
        Retorna la temperatura máxima registrada.

        Returns:
            float: Valor máximo registrado.

        Raises:
            ValueError: Si la lista de temperaturas está vacía.
        """
        if not self.__temperaturas:
            raise ValueError("No hay lecturas registradas para obtener la máxima.")
        return max(self.__temperaturas)

    def alerta_sobrecalentamiento(self, umbral: float) -> bool:
        """
        Evalúa si la última lectura supera un umbral de seguridad.

        Args:
            umbral (float): Temperatura límite de seguridad.

        Returns:
            bool: True si la última lectura supera el umbral; False en caso contrario.

        Raises:
            ValueError: Si no existen lecturas registradas.
        """
        if not self.__temperaturas:
            raise ValueError("No hay lecturas registradas para evaluar sobrecalentamiento.")
        return self.__temperaturas[-1] > umbral
