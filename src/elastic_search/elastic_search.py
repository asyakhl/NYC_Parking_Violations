from datetime import datetime
from elasticsearch import Elasticsearch
from requests import get
from time import sleep

def create_and_update_index(index_name, doc_table):
	es=Elasticsearch()
	try:
		es.indices.create(index=index_name)
	except Exception:
		pass

	return es

