import dpkt
import argparse

class PCAPProcessor
"""This will process the PCAP provided by the user"""
	def __init__(self, file):
	self.PCAP = args.PCAP
	file = open(self.PCAP)
	return file
	
	def IPProcess(self, file):
		PCAP = dpkt.pcap.Reader(file)
		return ProcessedPCAP

if __name__ == '__main__':
	parser == argparse.ArgumentParser(description='This program will do the most amazing analysis of a PCAP file you have ever seen.')
	parser.add_argument('-p', '--PCAP', dest='PCAP', help='Please provide a path to the PCAP file')
	parser.add_argument('-t', '--type', dest='type', choices=['IP', 'Port', 'Traffic'], help='Provide either IP, Port or UDP/TCP to base the traffic on. Choose IP, Port or Traffic')
	args = parser.parse_args()
	if args.type == IP:
		inst = PCAPProcessor() #Instantiate the class first!
		inst.IPProcess()
	