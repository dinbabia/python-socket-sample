from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.bind(('localhost', 9000))
        serversocket.listen(5) # queue/hold other 4 requests temporarily. don't tell them you're busy
        while(1):
            # .accept() will wait forever until someone requests
            # it wil not proceed to the next line
            # wait until a call is established
            (clientsocket, address) = serversocket.accept()
            
            # When a call is established, then proceed to the next lines
            # Client may speak first due to http
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split('\n')
            if ( len(pieces) > 0):
                print(pieces[0])
            
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hellloooo woorld</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    serversocket.close()
print("Access http://localhost:9000")
createServer()
