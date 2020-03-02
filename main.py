from sys import argv
from sodapy import Socrata
import os

if __name__ =="__main__":

# def get_parking_violations(page_size: int, page_num: int=None, json_file: str="stdout") -> list:
	
	client = Socrata("data.cityofnewyork.us", os.environ["APP_KEY"])

	total = client.get("nc67-uf89", select='COUNT(*)')
	total = int(total[0]["COUNT"])

	num_pages = total/int(argv[2]) # total number of calls/number of pages

	output = []
	if argv[2]==None:
		for i in range(num_pages): 
			output.append(client.get("nc67-uf89", limit=int(argv[1]), offset=i*10))
	else:
		for i in range(int(argv[2])):
			output.append(client.get("nc67-uf89", limit=int(argv[1]), offset=i*10))
	print(output)

	# with open(str(argv[3]), "w") as res_out:
	# 	res_out.write(str(output))


	