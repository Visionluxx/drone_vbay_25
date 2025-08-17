import socket, sys, tty, termios

UDP_IP = "192.168.4.1"
UDP_PORT = 14550
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def getch():
    """Đọc 1 ký tự ngay khi nhấn (Linux/Termux)"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

print("Nhấn phím để điều khiển: r/f/a/d/w/s/x/z, nhấn q để thoát")

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
        sock.sendto(b"YAW_FRONT", (UDP_IP, UDP_PORT))
        print("YAW_FRONT")
    elif key == "s":
        sock.sendto(b"YAW_BACK", (UDP_IP, UDP_PORT))
        print("YAW_BACK")
    elif key == "x":
        sock.sendto(b"RIGHT", (UDP_IP, UDP_PORT))
        print("RIGHT")
    elif key == "z":
        sock.sendto(b"LEFT", (UDP_IP, UDP_PORT))
        print("LEFT")


