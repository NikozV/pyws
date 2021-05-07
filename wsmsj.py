'''

Script que envia automaticamente msj a WhatsApp, 
con un horario especifico, es necesario estar con WhatsApp web y logeado
es necesrio instalar:
- python3-tk
- python3 -m pip install pywhatkit

autor: Vassallo Nicolas

'''

#Importo libreria pywhatkit
import pywhatkit 

#Ingreso de numero de celular
num = input("ingrese numero de celular: ")
numCel = "+54"+num #agrego +54 para que mandar msj a un cel argentino
print(numCel) #Control

#Ingreso de mensaje
mensaje = input("Mensaje: ")

#Ingreso de hora en la que quiere ser enviado el msj
print("##### Ingrese la hora y minuto de envio del mensaje #####")
h = int(input("Hora: "))
m = int(input("Minutos: "))

# Usamos Un try-except para controlar si es correcto el numero
try: 
 
    pywhatkit.sendwhatmsg(numCel,  #Numero destinatario
                            mensaje, #Mensaje
                            h,m) #Hora,minutos al que se quiere mandar el mensaje
    
    print("Mensaje Enviado") #mensaje en consola que avisa que viajo bien el msj
  
except:  
     
    print("Ocurrio Un Error") #Mesaje de error en consola, algo salio mal