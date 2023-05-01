import redis
import datetime
import time

r = redis.Redis(password='O3lnmWPfc8dG4SmToXPYnV0q3BsbD8eG', host='redis-19787.c16.us-east-1-3.ec2.cloud.redislabs.com', port=19787, decode_responses=True)

while True:
	received = r.xread({"orders": '$'}, None, 0)

	print(received)

	for result in received:
		data = result[1]
		for tuple in data:
			orderDict = tuple[1];
			print(orderDict)

	time.sleep(1)

