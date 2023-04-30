import redis
import csv
import datetime
from redis import RedisError

r = redis.Redis(password='YOUR_PASSWORD', host='YOUR_ENDPOINT_HOST', port=YOUR_ENDPOINT_PORT, decode_responses=True)

try:
	r.ts().create("quantity", retention_msecs = None)
except RedisError as  e:
	print(e)

with open("OnlineRetail.csv", encoding='utf-8-sig') as csvf:
	csvReader = csv.DictReader(csvf)

	lastTime = 0
	totalQuantity = 0

	for rows in csvReader:
		invoiceTime = datetime.datetime.strptime(rows['InvoiceDate'], '%m/%d/%Y %H:%M')
		invoiceEpoch = int(invoiceTime.timestamp()) * 1000
		quantity = int(rows['Quantity'])
#		print(invoiceEpoch, quantity)
		if (invoiceEpoch > lastTime):
			print("Total orders for " + str(lastTime) + " is " + str(totalQuantity))
			r.ts().add("quantity", lastTime, totalQuantity)
			totalQuantity = 0
			lastTime = invoiceEpoch

		totalQuantity += quantity

