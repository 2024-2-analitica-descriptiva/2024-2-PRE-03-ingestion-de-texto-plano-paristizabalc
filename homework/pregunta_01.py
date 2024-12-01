"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import re

import pandas as pd

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    def extract_records(data):
        """Extraer registos empleando regex"""
        pattern = re.compile(
            r"([0-9]+)(?:\s+)([0-9]+)(?:\s+)([0-9|\,]+)(?:[\s|\%]+)([a-z|\s|\,|\-|\/|\n|(|)]+)(?:\.*\n*)"
        )

        return pattern.findall(data)

    def process_key_words(data):
        """Procesar palabras clave"""

        def concat_key_words(key_words):
            """Concatenar palabras clave"""
            key_words = key_words.replace("\n", " ").split(",")
            return ", ".join([" ".join(word.strip().split()) for word in key_words])

        data = [
            (
                int(record[0]),
                float(record[1]),
                float(record[2].replace(",", ".")),
                concat_key_words(record[3]),
            )
            for record in data
        ]

        return data

    def create_dataframe(data):
        """Crear dataframe"""
        columns = [
            "cluster",
            "cantidad_de_palabras_clave",
            "porcentaje_de_palabras_clave",
            "principales_palabras_clave",
        ]
        df = pd.DataFrame(data, columns=columns)

        return df

    def read_text_file(file_path):
        """Leer archivo de texto"""
        with open(file_path, "r") as file:  # type: ignore
            data = file.read()

        return data

    def run_job():
        data = read_text_file("files/input/clusters_report.txt")
        data = extract_records(data)
        data = process_key_words(data)
        data = create_dataframe(data)

        return data

    return run_job()


if __name__ == "__main__":
    print(pregunta_01())