import datetime

from redis_om import (
	JsonModel,
	EmbeddedJsonModel,
	Field
)

class Product(EmbeddedJsonModel):
	StockCode: str
	Description: str
	UnitPrice: float

class Order(JsonModel):
	InvoiceNo: str
	Quantity: int = Field(index=True)
	InvoiceDate: datetime.date
	CustomerID: int
	Item: Product
	Country: str

