
node_info = []

def parse():
	global node_info
	for n in range(1,5):
		info_list = []
		node_info.append("Node"+str(n))
		with open('Captures/' + "Node"+str(n)+"_filtered.txt","r") as f:
			line = "nothing"
			enter = False
			while line:
				line = f.readline()
				if enter:
					info_list.append(line)
					enter = False

				if "No." in line:
					enter = True

		for i in info_list:
			writeIn = []
			temp = i.split(" ")
			for value in temp:
				if len(value.strip()) != 0:
					writeIn.append(value)
			# In this sequence
			# No.  Time  Source  Destination  Length  requestOrReply  ttl  ReplyOrRequestNo
			icmp_info = writeIn[0] + " " + writeIn[1] + " " + writeIn[2] + " " + writeIn[3] + " " + writeIn[5] + " " + writeIn[8] + " " + writeIn[11].replace("ttl=", "") + " " + writeIn[14].replace(")\n","")
			node_info.append(icmp_info)
			#print(icmp_info)
	node_info.append("Node5")
#	print(node_info.append)


