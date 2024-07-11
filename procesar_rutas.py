import xml.etree.ElementTree as ET

def redondear_vehs_per_hour(valor):
    """Redondear el valor de vehsPerHour al entero más cercano."""
    return str(round(float(valor)))

def ajustar_duration(valor_actual, valor_objetivo):
    """Ajustar el valor de duration al valor objetivo."""
    return f"{valor_objetivo:.2f}"

def procesar_xml(ruta_archivo, ruta_archivo_salida, valor_duration):
    """Leer y procesar el archivo XML, redondeando los valores de vehsPerHour y ajustando los valores de duration."""
    tree = ET.parse(ruta_archivo)
    root = tree.getroot()
    
    for elem in root.iter():
        for attr in list(elem.attrib.keys()):  # Convert keys to list to allow modification during iteration
            if attr == 'vehsPerHour':
                valor_original = elem.attrib[attr]
                valor_redondeado = redondear_vehs_per_hour(valor_original)
                elem.attrib[attr] = valor_redondeado
            elif attr == 'duration':
                valor_original = elem.attrib[attr]
                valor_ajustado = ajustar_duration(valor_original, valor_duration)
                elem.attrib[attr] = valor_ajustado
    
    tree.write(ruta_archivo_salida)
# Ejemplo de uso
ruta_archivo = 'ruta1_completo.rou.xml'
ruta_archivo_salida = 'ruta1_completo_procesar.rou.xml'
valor_duration = 30.00
procesar_xml(ruta_archivo, ruta_archivo_salida, valor_duration)