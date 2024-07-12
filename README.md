# Simulacion-de-Trafico-con-SUMO
<p>El siguiente trabajo se enfoca en modelar el tráfico realista de la Av. 12 de Abril Campus Central de la Universidad de Cuenca. La información que se ingresó en la simulación como el flujo vehicular y ciclo semafórico se actualizo tomando como punto de referencia los datos de Movilidad del año 2022, que fueron proporcionado por el Municipio de Cuenca.</p>

<p>En este repositorio contamos con todos los archivos necesarios para la correcta simulación. Contamos con programas de Python para actualizar la información de manera automatizada:</p>

<ul>
  <li>Para actualizar la velocidad de los vehículos modificar el parámetro "nuevo_valor_speed" del programa de Python "procesar_net.py".</li>
  <li>Para actualizar la duración de espera de los buses en cada una de las modificar el parámetro "valor_duration" del programa de Python "procesar_rutas.py".</li>
</ul>

<p>Una vez que tengamos los parámetros de simulación de acorde a nuestras necesidades ejecutamos el archivo contenedor de la simulación de SUMO que lleva de nombre "corregido.sumocfg". Este ejecutara los demás archivos necesarios como:</p>

<ul>
  <li>El mapa o escenario de simulación deberemos contar con el archivo "mapa1.net.xml"</li>
  <li>Para la generación de los vehículos y rutas, debemos contar con el archivo "ruta1_completo_procesar.rou.xml"</li>
  <li>Adicional agregamos un archivo para las paradas de buses "Paradas_bus.add.xml"</li>
</ul>
<ul>
  <li>Los datos proporcionados por la municipalidad se encuentran en "Semaforos_avLoja_Abril-Completo"</li>
</ul>
