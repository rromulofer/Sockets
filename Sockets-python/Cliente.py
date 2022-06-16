#!/usr/bin/env python3
# RÔMULO SOUZA FERNANDES
# REDES DE COMPUTADORES - UENF
# TRABALHO SOBRE SOCKETS

import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 50000        # Porta do servidor

# Familia do protocolo e como socket irá tratar a entrega de dados
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPV4 e TCP
s.connect((HOST, PORT))  # Faz a conexão
s.sendall(str.encode('Olá mundo!\n'))  # Envia os dados
data = s.recv(1024)  # Recebe os dados

print('\n- Mensagem: ', data.decode())
