import time
import concurrent.futures
import subprocess

T1 = time.perf_counter()

# Fungsi untuk mencetak pesan, baik gagal, berhasil atau ada kesalahan lain
def print_message(args = True, host = 'none', invalidIp = False):
    if not args :
        print('Gagal: IP address belum diberikan\ncontoh : latihan_shel.py 192.168.100.1')
    elif args == 'Up' or args == 'Down':
        print('Host ' + host + ' is ' + args)
    elif invalidIp:
        print('Alamat ip salah')

def main(arg):
    p1 = subprocess.Popen(['ping','-c3',arg],stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['grep','packet'],stdin=p1.stdout,stdout=subprocess.PIPE)
    p1.stdout.close()
    output = p2.communicate()[0].decode('utf-8').split(",")
    if len(output) == 5:
        print_message(args='Down',host=arg)
    else :
        if int(output[2][1]) >= 1:
            print_message(args='Down',host=arg)
        else:
            print_message(args='Up',host=arg)

with concurrent.futures.ProcessPoolExecutor() as executor:
    ips = ["192.168.100.1", "192.168.11.6", "192.168.100.3", "8.8.8.8", "8.8.4.4"]
    results = [executor.submit(main,ip) for ip in ips]
    for f in concurrent.futures.as_completed(results):
        f.result()

T2 = time.perf_counter()

print(f"selesai dalam : {round(T2 - T1, 2)} detik")
