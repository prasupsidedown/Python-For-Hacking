import socket

Target_host = "127.0.0.1"
target_port = 9997

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"Halo, Cuaca sedang tidak bisa diprediksi",(Target_host, target_port))

data, addr = client.recvfrom(4096)
print("Pesan dari server: \"{}\"".format(data.decode()))

client.close()
