
import datetime
import csv
import json
from redis_om import (JsonModel, EmbeddedJsonModel)
from pydantic import ValidationError
from Schema import *

with open("OnlineRetail.csv", encoding='utf-8-sig') as csvf:
	csvReader = csv.DictReader(csvf)

	for rows in csvReader:
		try:
			item = Product(
				StockCode=rows['StockCode'],
				Description=rows['Description'],
				UnitPrice=rows['UnitPrice']
			)

			order = Order(
				InvoiceNo=rows['InvoiceNo'],
				Item = item,
				Quantity=rows['Quantity'],
				InvoiceDate=datetime.datetime.strptime(rows['InvoiceDate'], '%m/%d/%Y %H:%M'),
				CustomerID=rows['CustomerID'],
				Country=rows['Country']
			)

		except ValidationError as e:
			print(e)
			continue

		print(order.key())
		order.save()

