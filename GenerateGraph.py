import csv

# Dictionaries to de-dupliate items and customers, and map them to unique internal IDs
itemNodeIDs = {}
customerNodeIDs = {}
orderNodeIDs = {}

itemNodes = []
customerNodes = []
orderNodes = []
transactEdges = []
containsEdges = []

nextID = 0

with open("OnlineRetail.csv", encoding='utf-8-sig') as csvf:
	csvReader = csv.DictReader(csvf)

	for rows in csvReader:

		# Skip anonymous purchases
		if 'CustomerID' not in rows:
			continue

		StockCode = rows['StockCode']
		Description = rows['Description']
		UnitPrice = rows['UnitPrice']
		InvoiceNo = rows['InvoiceNo']
		Quantity = rows['Quantity']
		CustomerID = rows['CustomerID']
		Country = rows['Country']
		InvoiceDate = rows['InvoiceDate']

		# Build up dictionaries of unique items and customers
		if StockCode not in itemNodeIDs:
			itemNodes.append([nextID, StockCode, Description, UnitPrice])
			itemNodeIDs[StockCode] = nextID
			nextID += 1

		if CustomerID not in customerNodeIDs:
			customerNodes.append([nextID, CustomerID, Country])
			customerNodeIDs[CustomerID] = nextID
			nextID += 1

		# If we are seeing this invoice number for the first time,
		# create an order node and associate the customer with the order
		if InvoiceNo not in orderNodeIDs:
			orderNodes.append([nextID, InvoiceNo, InvoiceDate])
			transactEdges.append([customerNodeIDs[CustomerID], nextID])
			orderNodeIDs[InvoiceNo] = nextID
			nextID += 1

		# Associate the item with the order
		containsEdges.append([orderNodeIDs[InvoiceNo], itemNodeIDs[StockCode]])

#Dump out the nodes
itemFields = ['_internalItemID', 'StockCode', 'Description', 'UnitPrice']
customerFields = ['_internalCustomerID', 'CustomerID', 'Country']
orderFields = ['_internalOrderID', 'InvoiceNo', 'InvoiceDate']

with open("item.csv", 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(itemFields)
	writer.writerows(itemNodes)

with open("customer.csv", 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(customerFields)
	writer.writerows(customerNodes)

with open("order.csv", 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(orderFields)
	writer.writerows(orderNodes)

#Dump out the edges
transactionFields = ['CustomerID', 'OrderID']
containsFields = ['InvoiceID', 'ItemID']

with open("transaction.csv", 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(transactionFields)
	csvwriter.writerows(transactEdges)

with open("contains.csv", 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(containsFields)
	csvwriter.writerows(containsEdges)

