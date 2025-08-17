import socket
import keyboard  # pip install keyboard

UDP_IP = "192.168.4.1"
UDP_PORT = 14550

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
    if keyboard.is_pressed("r"):
        sock.sendto(b"UP", (UDP_IP, UDP_PORT))
        print("UP")
    elif keyboard.is_pressed("f"):
        sock.sendto(b"DOWN", (UDP_IP, UDP_PORT))
        print("DOWN")
    elif keyboard.is_pressed("a"):
        sock.sendto(b"YAW_LEFT", (UDP_IP, UDP_PORT))
        print("YAW_LEFT")
    elif keyboard.is_pressed("d"):
        sock.sendto(b"YAW_RIGHT", (UDP_IP, UDP_PORT))
        print("YAW_RIGHT")
    elif keyboard.is_pressed("w"):
        sock.sendto(b"YAW_FRONT", (UDP_IP, UDP_PORT))
        print("YAW_FRONT")
    elif keyboard.is_pressed("s"):
        sock.sendto(b"YAW_BACK", (UDP_IP, UDP_PORT))
        print("YAW_BACK")
    elif keyboard.is_pressed("x"):
        sock.sendto(b"RIGHT", (UDP_IP, UDP_PORT))
        print("RIGHT")
    elif keyboard.is_pressed("z"):
        sock.sendto(b"LEFT", (UDP_IP, UDP_PORT))
        print("LEFT")
