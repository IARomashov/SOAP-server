from zeep import Client


client = Client('http://localhost:8000/?wsdl')
result = client.service.summa(100, 50)
print(result)

result = client.service.difference(20, 5)
print(result)
