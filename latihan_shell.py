import subprocess
import sys

# Fungsi untuk mencetak pesan, baik gagal, berhasil atau ada kesalahan lain
def print_message(args = True, host = 'none', invalidIp = False):
    if not args :
        print('Gagal: IP address belum diberikan\ncontoh : latihan_shel.py 192.168.0.3')
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


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else :
        print_message(args=False)
