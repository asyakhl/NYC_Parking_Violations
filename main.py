from sys import argv
from src.nyc_parking_violations.parking_violations_api import get_parking_violations
import argparse
if __name__ == "__main__":

	ap = argparse.ArgumentParser()
	ap.add_argument("--page_size", required=True)
	ap.add_argument("--page_num", required=False)
	ap.add_argument("--output", required=False)
	args = vars(ap.parse_args())

	args_list = [None]*len(argv[1:])
	for i in range(len(list(argv[1:]))):
		indx = list(argv[1:])[i].index("=")
		args_list[i] = ("".join(list(argv[1:])[i][:indx]))
		
	
	def to_json_file(file_name: str, content:list):
		with open(file_name, "w") as res_out:
			for i in range(len(content)):
				res_out.write(f"{content[i]}\n")
			return res_out
	
		if len(argv)==2:
		 		print(get_parking_violations(int(args["page_size"])))
		elif len(argv)==3:

			if "--output" in args_list:
				result = get_parking_violations(int(args["page_size"]))
				to_json_file(args["output"],result)
			else:
				print(get_parking_violations(int(args["page_size"]), int(args["page_num"])))

		elif len(argv)==4:
			result = get_parking_violations(int(args["page_size"]), int(args["page_num"]))
			to_json_file(args["output"],result)
		
	
	



	
	