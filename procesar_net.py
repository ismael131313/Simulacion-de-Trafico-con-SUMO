import xml.etree.ElementTree as ET

def actualizar_speed(valor):
    """Actualizar el valor de speed a un número específico."""
    return f"{valor:.2f}"

def procesar_xml_speed(ruta_archivo, ruta_archivo_salida, nuevo_valor):
    """Leer y procesar el archivo XML, actualizando los valores de speed y guardando en un nuevo archivo."""
    tree = ET.parse(ruta_archivo)
    root = tree.getroot()
    
    for elem in root.iter():
        for attr in elem.attrib:
            if attr == 'speed':
                elem.attrib[attr] = actualizar_speed(nuevo_valor)
    
    tree.write(ruta_archivo_salida)

# Ejemplo de uso
ruta_archivo = 'mapa1.net.xml'
ruta_archivo_salida = 'mapa1_procesar.net.xml'
nuevo_valor_speed = 13.89
procesar_xml_speed(ruta_archivo, ruta_archivo_salida, nuevo_valor_speed)