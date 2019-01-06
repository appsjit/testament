# make sure ES is up and running
import requests
#connect to our cluster
from elasticsearch import Elasticsearch
#let's iterate over swapi people documents and index them
import json


res = requests.get('http://localhost:9200')
print(res.content)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# r = requests.get('http://localhost:9200')
# i = 1
# while r.status_code == 200:
#     r = requests.get('http://swapi.co/api/people/' + str(i))
#     es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
#     i = i + 1
#
# print(i)

print(es.get(index='sw', doc_type='people', id=5))



r = requests.get('http://localhost:9200')
i = 18
while r.status_code == 200:
   r = requests.get('http://swapi.co/api/people/'+ str(i))
   es.index(index='sw', doc_type='people', id=i,     body=json.loads(r.content))
   i=i+1


print(es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}}))

### 8.2
print(es.search(index="sw", body={"query": {"prefix" : { "name" : "lu" }}}))

## 8.3
es.search(index="sw", body={"query": {"fuzzy_like_this_field" : { "name" : {"like_text": "jaba", "max_query_terms":5}}}})