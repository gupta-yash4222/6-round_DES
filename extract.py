file = open("6-round_DES\out_server.txt", 'r')
fo = open("6-round_DES\ctext.txt", 'w')

for line in file:
    for word in line.split():
        if(len(word)==16):
            fo.write(word + "\n")
