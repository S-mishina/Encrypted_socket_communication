import socket
from cryptography.fernet import Fernet

PORT = 50003
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', PORT))
    s.listen()
    while True:
        (connection, client) = s.accept()
        try:
            print('Client connected', client)
            #データを受け取る.
            data = connection.recv(BUFFER_SIZE)
            #共通鍵
            key=b'f3Wt4YosRSGFimDDNOopTZLe0W62kQimamuuYp5dLXI='
            #復号
            f = Fernet(key)
            #出力
            print('復号前'+str(data))
            print('復号後'+str(f.decrypt(data)))
            #コネクションを返す
            connection.send(data.upper())
        finally:
            connection.close()