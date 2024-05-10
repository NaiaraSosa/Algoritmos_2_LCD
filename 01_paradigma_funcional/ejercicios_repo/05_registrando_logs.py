"""
Ejercicio: Registrando logs
A lo largo de nuestro programa es posible que necesitemos almacenar información de interés en el log de ejecución. 
A efectos prácticos, nuestro destino de log será la consola, por lo que podemos utilizar simplemente un print() 
para registrar un mensaje de log.

Implementar una función log currificada que permita registrar un mensaje de log y el tipo, que puede ser error, alerta o información.
"""

from functools import partial

def log(tipo, mensaje):
    print(f"[{tipo.upper()}] {mensaje}")

log_error = partial(log, "error")
log_alerta = partial(log, "alerta")
log_informacion = partial(log, "información")

# Ejemplos de uso
log_error("Ocurrió un error")
log_alerta("Se generó una alerta")
log_informacion("Este es un mensaje informativo")

