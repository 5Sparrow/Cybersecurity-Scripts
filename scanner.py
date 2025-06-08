import socket

target = input("Enter IP or domain to scan: ")
port = int(input("Enter port to scan (e.g., 80): "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)

result = sock.connect_ex((target, port))

if result == 0:
    print(f"[+] Port {port} is OPEN on {target}")
else:
    print(f"[-] Port {port} is CLOSED or FILTERED on {target}")

sock.close()
