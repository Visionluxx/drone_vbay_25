import socket
import sys
import termios
import tty

UDP_IP = "192.168.4.1"
UDP_PORT = 14550

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Hàm đọc 1 ký tự không cần Enter
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

print("Điều khiển drone bằng bàn phím trong Termux:")
print(" w: FRONT | s: BACK | a: YAW_LEFT | d: YAW_RIGHT")
print(" r: UP    | f: DOWN | z: LEFT     | x: RIGHT")
print(" q: Quit")

while True:
    key = getch()

    if key == "r":
        sock.sendto(b"UP", (UDP_IP, UDP_PORT))
        print("UP")
    elif key == "f":
        sock.sendto(b"DOWN", (UDP_IP, UDP_PORT))
        print("DOWN")
    elif key == "a":
        sock.sendto(b"YAW_LEFT", (UDP_IP, UDP_PORT))
        print("YAW_LEFT")
    elif key == "d":
        sock.sendto(b"YAW_RIGHT", (UDP_IP, UDP_PORT))
        print("YAW_RIGHT")
    elif key == "w":
        sock.sendto(b"FRONT", (UDP_IP, UDP_PORT))
        print("FRONT")
    elif key == "s":
        sock.sendto(b"BACK", (UDP_IP, UDP_PORT))
        print("BACK")
    elif key == "x":
        sock.sendto(b"RIGHT", (UDP_IP, UDP_PORT))
        print("RIGHT")
    elif key == "z":
        sock.sendto(b"LEFT", (UDP_IP, UDP_PORT))
        print("LEFT")
