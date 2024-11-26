import requests
import subprocess
from termcolor import colored  # Yazılara renk katmak için
import time

# Büyük logo ve başlık
def show_logo():
    print(colored("""
    ████████╗███████╗███╗   ███╗
    ╚══██╔══╝██╔════╝████╗ ████║
       ██║   █████╗  ██╔████╔██║
       ██║   ██╔══╝  ██║╚██╔╝██║
       ██║   ███████╗██║ ╚═╝ ██║
       ╚═╝   ╚══════╝╚═╝     ╚═╝
       """, "red", attrs=['bold']))
    print(colored("ZFM Tool'a Hoşgeldiniz!", "cyan", attrs=['bold']))

# Kullanıcı Bilgilerini Toplama
def get_ip_info():
    response = requests.get('https://ipinfo.io/json')
    if response.status_code == 200:
        data = response.json()
        ip_info = {
            "IP": data['ip'],
            "Şehir": data['city'],
            "Bölge": data['region'],
            "Ülke": data['country'],
            "İSS": data['org']
        }
        return ip_info
    else:
        print("IP bilgileri alınamadı.")
        return {}

# Port Taraması
def scan_ports(ip):
    result = subprocess.run(['nmap', '-sV', ip], stdout=subprocess.PIPE, text=True)
    return result.stdout

# SSH Brute Force Denemesi
def ssh_brute_force(ip, username, password_list):
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for password in password_list:
        try:
            ssh.connect(ip, username=username, password=password)
            ssh.close()
            return f"Başarılı: {password}"
        except:
            continue
    return "Başarılı bir parola bulunamadı."

# Arayüzleri Nikto ve DirBuster'dan Çekme
def nikto_scan():
    print("Nikto ile web zafiyet taraması başlıyor...")
    subprocess.run(["nikto", "-h", "http://example.com"])  # Örnek URL'yi değiştir

def dirbuster_scan():
    print("DirBuster ile dizin taraması başlıyor...")
    subprocess.run(["dirbuster"])  # DirBuster GUI'yi çağırır

# Ağ Zafiyet Araçları
def network_vulnerabilities():
    while True:
        print(colored("""
        1. Monitor Mode Başlat
        2. Airgeddon Başlat
        3. Wireshark Başlat
        4. MSFConsole Başlat
        5. Wifite Başlat
        6. Çıkış
        """, "yellow", attrs=['bold']))

        choice = input(colored("Bir seçenek seçin: ", "yellow"))
        
        if choice == "1":
            print(colored("Monitor Mode başlatılıyor...", "green"))
            subprocess.run(["airmon-ng", "start", "wlan0"])  # Monitor mode başlatma komutu
        
        elif choice == "2":
            print(colored("Airgeddon başlatılıyor...", "green"))
            subprocess.run(["airgeddon"])  # Airgeddon arayüzünü başlat

        elif choice == "3":
            print(colored("Wireshark başlatılıyor...", "green"))
            subprocess.run(["wireshark"])  # Wireshark'ı başlat

        elif choice == "4":
            print(colored("MSFConsole başlatılıyor...", "green"))
            subprocess.run(["msfconsole"])  # MSFConsole başlat

        elif choice == "5":
            print(colored("Wifite başlatılıyor...", "green"))
            subprocess.run(["wifite"])  # Wifite başlat

        elif choice == "6":
            print(colored("Ağ Zafiyet Araçları sekmesinden çıkılıyor...", "red"))
            break
        
        else:
            print(colored("Geçersiz seçim. Lütfen tekrar deneyin.", "red"))

# Ana Menü
def main():
    show_logo()
    while True:
        print(colored("""
        1. Kullanıcı Bilgilerini Topla
        2. Açık Port Taraması Yap
        3. SSH Brute Force Denemesi
        4. SQL Zafiyet Taraması
        5. IP Adresini Değiştir
        6. Nikto Aracı ile Tarama
        7. DirBuster ile Tarama
        8. Ağ Zafiyet Araçları
        9. Çıkış
        """, "red", attrs=['bold']))

        choice = input(colored("Bir seçenek seçin: ", "yellow"))
        
        if choice == "1":
            print(colored("ZFM Tool'a Hoşgeldiniz!", "green", attrs=['bold']))
            ip_info = get_ip_info()
            print(colored("Kullanıcı Bilgileri:", "blue"))
            for key, value in ip_info.items():
                print(f"{key}: {value}")
        
        elif choice == "2":
            print(colored("ZFM Tool'a Hoşgeldiniz!", "green", attrs=['bold']))
            hedef_ip = input("Taramak istediğiniz IP: ")
            port_results = scan_ports(hedef_ip)
            print(colored("Port Tarama Sonuçları:", "blue"))
            print(port_results)
        
        elif choice == "3":
            print(colored("BRUTE FORCE KULLANMAK BİR SUÇTUR!", "red", attrs=['bold', 'underline']))
            hedef_ip = input("SSH Brute Force için hedef IP: ")
            kullanıcı_adı = input("Kullanıcı adı: ")
            parola_listesi = ["123456", "admin", "password", "root"]  # Örnek parola listesi
            brute_result = ssh_brute_force(hedef_ip, kullanıcı_adı, parola_listesi)
            print(colored(brute_result, "blue"))
        
        elif choice == "4":
            print(colored("ZFM Tool'a Hoşgeldiniz!", "green", attrs=['bold']))
            hedef_url = input("Hedef URL: ")
            result = subprocess.run(['sqlmap', '-u', hedef_url, '--batch'], stdout=subprocess.PIPE, text=True)
            print(result.stdout)
        
        elif choice == "5":
            print(colored("IP adresinizi değiştirme işlemi başlatılıyor...", "yellow"))
            subprocess.run(["ifconfig", "eth0", "192.168.1.100"])  # Örnek IP değişimi
        
        elif choice == "6":
            print(colored("Nikto ile tarama başlatılıyor...", "blue"))
            nikto_scan()
        
        elif choice == "7":
            print(colored("DirBuster ile tarama başlatılıyor...", "blue"))
            dirbuster_scan()
        
        elif choice == "8":
            network_vulnerabilities()  # Ağ zafiyetleri için sekmeye yönlendir

        elif choice == "9":
            print(colored("ZFM Tool'dan çıkış yapılıyor...", "red"))
            break
        
        else:
            print(colored("Geçersiz seçim. Lütfen tekrar deneyin.", "red"))

if __name__ == "__main__":
    main()
