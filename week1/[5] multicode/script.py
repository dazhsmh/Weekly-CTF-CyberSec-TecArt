import base64
import urllib.parse
import codecs

msg = "NmU3MDZlNzE3MjdhNmMyNTM3NDI2MTcyNjY2NzcyNzE1ZjcyNjE3MDMwNzE3NjYxNzQ1ZjM2NzIzNDM5NmUzODM3MzkyNTM3NDQ="

decodebase64 = base64.b64decode(msg)
decodehex = bytes.fromhex(decodebase64.decode('utf-8'))
decodeurl = urllib.parse.unquote(decodehex.decode('utf-8'))
decoderot13 = codecs.decode(decodeurl, 'rot_13')
hasil = decoderot13

print(hasil)
