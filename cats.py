import requests
import json
import wget
from nanoid import generate

domain = "https://cataas.com/cat?json=true"

i=0
while i<100:
    x= requests.get(domain)
    data =json.loads(x.text)
    type = data["mimetype"]
    out = type.split("/")
    address= "https://cataas.com"+data["url"]
    print(address)
    filename =generate('1234567890abcdef', 10)+"."+out[1]
    name = wget.download(address,filename)
    
    i+=1
