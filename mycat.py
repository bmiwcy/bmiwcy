import socket
import threading
import getopt
import sys
import signal

def handler_client(client,server):
    while True:
        try:
            request = client.recv(1024)
            if len(request):
                print request
            else:
                pass
        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            sys.exit()

def server_loop(host,port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    while True:
        client, addr = server.accept()
        client_handler = threading.Thread(target=handler_client,args=(client,server))
        client_handler.setDaemon(True)
        client_handler.start()


        
options, args = getopt.getopt(sys.argv[1:],"l:p:",["listen=","port="])

if not len(sys.argv[1:]):
    print "Noting inputed!"
    
for opt, value in options:
   if opt in ("-l","--listen"):
        host = str(value)
        port = int(args[0])
        server_loop(host,port)

if len(args):

    client_host, client_port = sys.argv[1:]
    
    client_host = str(client_host)
    client_port = int(client_port)
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print "[*] Client Socket Error!"

    try:    
        client.connect((client_host,client_port))
    except:
        print "[*] Client Connect Error!"
        client.close()
        sys.exit()
        
    print "[*] Client Mode:"    
    while True:
        try:
            c_buff = raw_input()
            client.send(c_buff)
        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            sys.exit()

