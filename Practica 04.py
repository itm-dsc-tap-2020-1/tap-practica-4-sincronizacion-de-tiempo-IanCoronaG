#
#	
#   Ian Corona
#	Solicita hora de servidor ntp, imprime hora de salida y llegada de solicitud,
#	ajusta hora de reloj a tiempo_servidor + (salida-llegada)/2
#
import datetime
from time import ctime
import ntplib
import os
x = datetime.datetime.now()

print ("Hora de salida de la petición:  = %s" % x)


servidor_de_tiempo = "time-e-g.nist.gov"

cliente_ntp = ntplib.NTPClient()
respuesta = cliente_ntp.request(servidor_de_tiempo)
hora_actual = datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")
y = datetime.datetime.now()
print ("Hora de llegada de la petición:  = %s" % y)
print("Respuesta de " + servidor_de_tiempo +  ": " + str(hora_actual) + "\n")
print("Ajuste: "+str(((y-x)/2)))

nueva_hora = hora_actual+ ((y-x)/2)
print("\nHora a fijar: "+str(nueva_hora))

frmt= 'date -u "'+str(nueva_hora.strftime("%m%d%H%M%Y.%S"))+'"'
os.system(frmt)