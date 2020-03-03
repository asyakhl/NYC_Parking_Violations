from sys import argv
from src.nyc_parking_violations.parking_violations_api import get_parking_violations

if __name__ =="__main__":
	def to_json_file(file_name: str, content:list):
		with open(file_name, "w") as res_out:
			return res_out.write(str(content))

	
	if len(argv)==2:
		get_parking_violations(int(argv[1]))
	elif argv[2]=="results.json":
		result = get_parking_violations(int(argv[1]))
		to_json_file(argv[2],result)
	elif len(argv)==3 $ int(argv[2])==int:
		get_parking_violations(int(argv[1]), int(argv[2]))
	elif len(argv)==4:
		result = get_parking_violations(int(argv[1]), int(argv[2]))
		to_json_file(argv[3],result)



	
	