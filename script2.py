import nmap


#precisa ter nmap instalado e importar a lib python-nmap


def scan_portas():
    host = '127.0.0.1'
    ports = '21-443'
    proto = 'tcp'
    nmScan = nmap.PortScanner()
    nmScan.scan(host, ports)
    nmScan.command_line()
    lport = nmScan[host][proto].keys()
    for port in lport:
        print(f'port: {port} - state: {nmScan[host][proto][port]["state"]}')

scan_portas()
a = input('')
