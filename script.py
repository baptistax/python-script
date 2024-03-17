###importar bibliotecas
from sys import platform
import os
import subprocess
import nmap


'''
###Checando integridade da imagem

def scan_image(image_path):
    try:
        # Verifique se a imagem do container existe
        if not os.path.exists(image_path):
            print(f"A imagem {image_path} não foi encontrada.")
            return

        # Use o ClamAV para escanear a imagem em busca de malware
        result = subprocess.run(['clamscan', '-r', image_path], capture_output=True, text=True)

        # Verifique o resultado do scan
        if "Infected files: 0" in result.stdout:
            print(f"A imagem {image_path} está livre de malware.")
        else:
            print(f"A imagem {image_path} possui possíveis ameaças:")
            print(result.stdout)

    except Exception as e:
        print(f"Erro durante a verificação da imagem: {e}")

image_path = input("Insira aqui o caminho completo para a sua imagem")
scan_image(image_path)
'''

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


'''
Identificar Vulnerabilidades Conhecidas:

    Utilize bancos de dados de vulnerabilidades conhecidas, como o NIST National Vulnerability Database (NVD) e CVE Details, para obter informações sobre vulnerabilidades.

Escanear Imagens de Containers e Máquinas Virtuais: (ok)

    Desenvolva um módulo para escanear imagens de containers e máquinas virtuais em busca de vulnerabilidades conhecidas.
    Considere verificar configurações inadequadas, permissões excessivas, etc.

Avaliar Configurações de Segurança:

    Verifique as configurações de segurança do ambiente de execução, como políticas de rede, permissões de usuário, etc.
'''