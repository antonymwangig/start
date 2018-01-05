import re
class keywords:
	def __init__(self):
		self.productKeywords=["name","product","goods","goods-name","product-name","brand"]
		self.priceKeywords=["price","sale","sale-price","price-new","new-price","old-price","price-old"]
	def ProductIndentifiers(self):
		return self.productKeywords
	def ProductPricesIndentifiers(self):
		return self.priceKeywords
	def isProductKeyword(self,dict):
		for key in self.productKeywords:
			if re.search(key,str(dict)):
				return True

		return False
	def isPriceKeyword(self,dict):
		for key in self.priceKeywords:
			if re.search(key,str(dict)):
				
				return True

		return False
