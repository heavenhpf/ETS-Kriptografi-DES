import socket
import image

def Main():
        # Memasukkan host address
        host = '192.168.1.11'
        # Memasukkan port
        port = 5000
        # Mendapatkan instance
        mySocket = socket.socket()
        # Connect host adress dan port
        mySocket.connect((host,port))
        # Enkripsi image dengan bantuan image.py
        pad = image.pad_export
        message = image.img_enc+pad
        # Mengirim pesan
        for i in range(0,len(message),1024) :
                limit = min(i+1024,len(message))
                chunk = message[i:limit]
                mySocket.send(chunk.encode())
                 
        print("All Data sent to server")
        mySocket.close()
 
if __name__ == '__main__':
    Main()
