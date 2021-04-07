import subprocess

p1 = subprocess.Popen(['ping','-c3','192.168.136.1'],stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep','packet'],stdin=p1.stdout,stdout=subprocess.PIPE)

p1.stdout.close()

output = p2.communicate()[0].decode('utf-8').split(",")




print(output[2][1:3])
