from bs4 import BeautifulSoup
import socket

from urllib.request import urlopen
#Input del host, para que no sea un valor quemado
HOST = input('host definido: ')
PORT= int(input('numero del puerto: '))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#envio de data:
request = 'GET / HTTP/1.1\r\nHost: '+HOST+'\r\nConnection: close\r\n\r\n'

s.send(str.encode(request, 'utf-8'))
print(request)  # Request

# Recibir datos:
buffer = []
while True:
    d = s.recv(1024)  # HTTP RESPONSE
    if d:
        buffer.append(d)
    else:
        break
data = b' '.join(buffer)

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))


# Escriba los datos recibidos en un archivo html:
with open(HOST + '.html', 'wb') as htmlfile:
    htmlfile.write(html)

#Este fue el intento que empece a realizar para hacer el parseo de las direcciones
#Me toco hacerlo con una URL quemada por el momento
#Los otros valores se toman de forma con el input, y tambien se escribe el HTML
#segun el host ingresado.
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())
# Cierre la conexión:
s.close()

# Me apoye en el tutorial de: https://programmerclick.com/article/546769496/
