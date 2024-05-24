import nmap
import xlsxwriter

#precisa ter nmap instalado e importar a lib python-nmap
#precisa ter XlsxWriter


def scan_portas():

    host = '127.0.0.1'
    ports = '0-1023'
    proto = 'tcp'

    nmScan = nmap.PortScanner()
    nmScan.scan(host, ports)
    nmScan.command_line()
    lport = nmScan[host][proto].keys()
    data = {}

    for port in lport:
        data[port] = nmScan[host][proto][port]["state"]
    return data


def cria_planilha(data):

    workbook = xlsxwriter.Workbook('script.xlsx')
    plan = workbook.add_worksheet("Script")

    i = 1
    for item in data:
        plan.write(f'A{i}', item)
        i += 1

    i = 1
    for item in data:
        plan.write(f'B{i}', data[item])
        i += 1

    workbook.close()


dados = scan_portas()
cria_planilha(dados)
