def filter():
    # read 1 - 4 node file
    for n in range(1,5):
        icmp = []
        with open('Captures/' + "Node"+str(n)+".txt", "r") as f:
            line = f.readline()
            packet = line
            while line:
                line = f.readline()
                if "No." in line:
                    if "ICMP" in packet and "unreachable" not in packet:
                        icmp.append(packet)
                    packet = ''
                packet += line
        with open('Captures/' + "Node"+str(n)+"_filtered.txt","w") as fw:
           for packet in icmp:
                fw.write(packet)
                print(packet)

































