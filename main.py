from sys import argv
from datetime import datetime
from src.nyc_parking_violations.parking_violations_api import get_parking_violations
from src.elastic_search.elastic_search import create_and_update_index
import argparse
if __name__ == "__main__":

	es=create_and_update_index("parking_violation_records", "records")

	def to_json_file(file_name: str, content:list):
		with open(file_name, "w") as res_out:
			for i in range(len(content)):
				res_out.write(f"{content[i]}\n")
			return res_out
	def get_and_output_parking_violations(argv):
		ap = argparse.ArgumentParser()
		ap.add_argument("--page_size", required=True)
		ap.add_argument("--page_num", required=False)
		ap.add_argument("--output", required=False)
		args = vars(ap.parse_args())

		args_list = [None]*len(argv[1:])
		for i in range(len(list(argv[1:]))):
			indx = list(argv[1:])[i].index("=")
			args_list[i] = ("".join(list(argv[1:])[i][:indx]))
			
		
		if len(argv)==2:
		 		reults=get_parking_violations(int(args["page_size"]))
		 		print(results)
		 		return None, results
		elif len(argv)==3:

			if "--output" in args_list:
				results = get_parking_violations(int(args["page_size"]))
				return to_json_file(args["output"],results), results
			else:
				results=get_parking_violations(int(args["page_size"]), int(args["page_num"]))
				print(results)
				return None, results
		elif len(argv)==4:
			results = get_parking_violations(int(args["page_size"]), int(args["page_num"]))
			return to_json_file(args["output"],results), results

	file, list_park_viol=get_and_output_parking_violations(argv)

	for viol in list_park_viol:
		viol["timestamp"]= datetime.now()
		viol["issue_date"]=datetime.strptime(viol["issue_date"], "%m/%d/%Y")
		if "penalty_amount" in viol:
			viol["fine_amount"]=float(viol["fine_amount"])
		if "interest_amount" in viol:
			viol["interest_amount"]=float(viol["interest_amount"])
		if "reduction_amount" in viol:
			viol["reduction_amount"]=float(viol["reduction_amount"])
		if "payment_amount" in viol:
			viol["payment_amount"]=float(viol["payment_amount"])
		if "amount_due" in viol:
			viol["amount_due"]=float(viol["amount_due"])
		res = es.index(index="parking_violation_records", doc_type="records", body = viol)
		print(res["result"])



	
	