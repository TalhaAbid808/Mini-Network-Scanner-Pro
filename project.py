import socket
target = input("Enter Ip Address: ")
start_port =int(input("Enter Start port: "))
end_port =int(input("Enter End port: "))
open_ports =0
for port in range(start_port,end_port +1):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result==0:
        try:
            service=socket.getservbyport(port)
        except:
            service="Unknown"
        print(f"port{port} is open {service}")
        open_ports +=1
        with open("scan_result.txt","a") as file:
            file.write(f"port{port} is open {service} \n")
    s.close()
print("Total open ports",open_ports)