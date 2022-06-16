#!/usr/bin/env python3
# RÔMULO SOUZA FERNANDES
# REDES DE COMPUTADORES - UENF
# TRABALHO SOBRE SOCKETS

import socket

HOST = 'localhost'  # Endereço IP do servidor
PORT = 50000        # Porta do servidor

# Familia do protocolo e como socket irá tratar a entrega de dados
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPV4 e TCP
s.bind((HOST, PORT))  # Associa a estrutura socket e o endereço/porta do servidor
s.listen()  # Modo escuta
print('\n --- Esperando um cliente se conectar ---\n')
conn, ender = s.accept()
# Aceita conexões de clientes, retorna uma tupla da conexão realizada

print('Conectado em: ', ender)
while True:
    data = conn.recv(1024)  # Recebe os dados
    if not data:
        print('\n --- Encerrando a coneção --- \n')
        conn.close()  # Encerra a conexão
        break
    conn.sendall(data)  # Envia os dados
