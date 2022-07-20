#!/usr/bin/env python3

import socket

def banner_grabber_ssh(ip_host,port_host):

	connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Create a TCP connection
	connection.connect((ip_host,int(port_host)))
	print(connection.recv(1024))
	connection.close()

def banner_grabber_web(ip_host,port_host):

	connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	connection.connect((ip_host,int(port_host)))
	http_request="GET HTTP/2.0 \r\n"
	connection.send(http_request.encode())   #functia send permite doar bytes. asa ca trebuie folosit encode() din str
	http_response=connection.recv(1024)
	print(http_response.decode())
	connection.close()


ip=input("Enter IP to scan: ")
port=(input("Enter Port to scan: "))


if (port == "22"):
	banner_grabber_ssh(ip,port)	

if (port=="8080" or port=="80" or port=="9999"):
	banner_grabber_web(ip,port)
