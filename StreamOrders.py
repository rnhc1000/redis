import csv
import redis

r = redis.Redis(password='O3lnmWPfc8dG4SmToXPYnV0q3BsbD8eG', host='redis-19787.c16.us-east-1-3.ec2.cloud.redislabs.com', port=19787)


with open("OnlineRetail.csv", encoding='utf-8-sig') as csvf:
	csvReader = csv.DictReader(csvf)

	for row in csvReader:
		r.xadd("orders", row)
