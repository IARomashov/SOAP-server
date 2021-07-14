# Example SOAP server.
soap_server.py
Uses the spyne library.  
Calculate sum and difference of numbers.  
An example of requests to the server is request_soap.py.

### Start server:
```shell
python soap_server.py
```

### View wsdl:
```shell
curl -X GET "http: // localhost: 8000 /? wsdl"
```

## request_soap.py.
The request is sent using the zeep library.  
Sends two numbers to calculate the sum of the numbers.  
And also two numbers for calculating the difference of numbers.





