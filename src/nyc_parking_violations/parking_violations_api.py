
from sodapy import Socrata
import os
def get_parking_violations(page_size: int, page_num: int=None) -> list:
	
	client = Socrata("data.cityofnewyork.us", os.environ["APP_KEY"])

	total = client.get("nc67-uf89", select='COUNT(*)')
	total = int(total[0]["COUNT"])

	total_num_pages = total//page_size+1# total number of calls/page size

	output = []
	if page_num==None:
		for i in range(total_num_pages): 
			output+=client.get("nc67-uf89", limit=page_size, offset=i*page_size)
	else:
		for i in range(int(page_num)):
			output+=(client.get("nc67-uf89", limit=page_size, offset=i*page_size))

	return(output)