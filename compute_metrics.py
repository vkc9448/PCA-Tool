import math
from packet_parser import*
# I want to define each variable here
# number_request_sent = the number of echo request that the node sent
# number_reply_sent = the number of echo reply that the node sent
# number_request_received = the number of echo request that the node received
# number_reply_received = the number of echo reply that the node received
# total_request_sent = how many frame length of echo request that the node sent
# total_request_received = how many frame length of echo request that the node received
# total_request_data_sent = how many payload of echo request that the node sent
# total_request_data_sent = how many payload of echo request that the node received
# total_RTT = the sum of RTT
# total_delay = the sum of delay
# total_hop = the sum of hop
def compute():
	f = open('Mini Project 2 Output.csv', 'w')
	print ("Length:",len(node_info))
	nodes_ip = {"Node1": "192.168.100.1", "Node2": "192.168.100.2", "Node3": "192.168.200.1","Node4": "192.168.200.2"}
	for n in range(1,5):
		start = 0
		end  = 0
		for index, value in enumerate(node_info):
			if value == "Node" + str(n):
				start = index + 1
			if value == "Node"+str(n+1):
				end = index
		# here are all variables
		number_request_sent, number_reply_sent, number_request_received, number_reply_received = 0,0,0,0
		total_request_sent,total_request_received = 0,0
		total_request_data_sent, total_request_data_received = 0,0
		total_RTT, total_delay, total_hop = 0,0,0

		for i in range(start,end):
			r = node_info[i]
			info = r.split(" ")
			if nodes_ip["Node"+str(n)] == info[2]:
				if "request" in r:
					number_request_sent += 1
					total_request_sent += int(info[4])
					#IP header 20 bytes, ICMP header 8 bytes, the rest is ICMP payload, ethernet header 14 bytes, total 42 bytes
					total_request_data_sent += int(info[4]) - 42
				else:
					number_reply_sent += 1
			else:
				if "request" in r:
					number_request_received += 1
					total_request_received += int(info[4])
					# IP header 20 byte, ICMP header 8 bit, the rest is ICMP payload, ethernet header 14 bytes, total 42 bytes
					total_request_data_received += int(info[4]) - 42
				else:
					number_reply_received += 1

			# calculate the sum of RTT
			if "request" in r and info[2] == nodes_ip["Node"+str(n)]:
				for k in range(start,end):
					c = node_info[k]
					compare = c.split(" ")
					if int(compare[7]) == int(info[0]) and "reply" in c:
						total_RTT += (float(compare[1]) - float(info[1])) # RTT
						total_hop += (int(info[6]) - int(compare[6])) + 1 # hop
						break

			# calculate the sum of delay
			if "request" in r and info[3] == nodes_ip["Node"+str(n)]:
				for k in range(start,end):
					c = node_info[k]
					compare = c.split(" ")
					if int(compare[7]) == int(info[0]) and "reply" in c:
						total_delay += (float(compare[1]) - float(info[1])) # delay
						break


		# Write to file
		f.writelines("Node "+str(n)+"\n")
		f.writelines("\n")
		f.writelines("Echo Requests Sent, Echo Requests Received, Echo Replies Sent, Echo Replies Received\n")
		information = str(number_request_sent)+","+str(number_request_received)+","+str(number_reply_sent)+","+str(number_reply_received)
		f.writelines(information+"\n")
		f.writelines("Echo Request Bytes Sent (bytes), Echo Request Data Sent (bytes)\n")
		f.writelines(str(total_request_sent)+","+str(total_request_data_sent)+"\n")
		f.writelines("Echo Request Bytes Received (bytes), Echo Request Data Received (bytes)\n")
		f.writelines(str(total_request_received)+","+str(total_request_data_received)+"\n")
		f.writelines("\n")
		f.writelines("Average RTT (milliseconds),"+format("%.2f" %(total_RTT * 1000/number_request_sent))+"\n")
		f.writelines("Echo Request Throughput (kB/sec),"+format("%.1f" %(total_request_sent / (total_RTT) / 1000))+"\n")
		f.writelines("Echo Request Goodput (kB/sec),"+format("%.1f" %(total_request_data_sent / (total_RTT) / 1000))+"\n")
		f.writelines("Average Reply Delay (microseconds,"+format("%.2f" %(total_delay * 1000000 / number_request_received))+"\n")
		f.writelines("Average Echo Request Hop Count,"+format("%.2f" %(float(total_hop) / number_request_sent))+"\n")
		f.writelines("\n")

		# Testing
		#print("Node " + str(n), "Echo request sent:", number_request_sent, "Echo request received:", number_request_received, "Echo reply sent:", number_reply_sent, "Echo reply received:", number_reply_received)
		#print("Node " + str(n) + " Total Echo request sent size:", total_request_sent)
		#print("Node " + str(n) + " Total Echo request received size:", total_request_received)
		#print("Node " + str(n) + " Total Echo request sent data:", total_request_data_sent)
		#print("Node " + str(n) + " Total Echo request received data:", total_request_data_received)
		#print("Sum of RTT", total_RTT)
		#print("Node " + str(n) + " Average RTT:", (total_RTT * 1000 / number_request_sent), "ms")
		#print("Node " + str(n) + " Echo request Throughput:", (total_request_sent / (total_RTT) / 1000), "kb/s")
		#print("Node " + str(n) + " Echo request Goodput:", (total_request_data_sent / (total_RTT) / 1000), "kb/s")
		#print("Node " + str(n) + " Average Reply Delay:", (total_delay * 1000000 / number_request_received), "us")
		#print("Total hop", total_hop)
		#print("Node " + str(n) + " Hop count: " + format("%.2f" % (float(total_hop) / number_request_sent)), "\n")
	f.close()