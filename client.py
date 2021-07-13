from cryptography.fernet import Fernet
import socket


PORT = 50003
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', PORT))
    #データを入力
    data = input('Please input > ')
    #共通鍵
    key=b'f3Wt4YosRSGFimDDNOopTZLe0W62kQimamuuYp5dLXI='
    #キーを読み込む
    f = Fernet(key)
    #暗号化する
    token = f.encrypt(data.encode())
    #サーバ側に送る.
    s.send(token)
    print(s.recv(BUFFER_SIZE).decode())