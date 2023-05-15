import json
import boto3
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth

host = 'my-test-domain.us-east-1.es.amazonaws.com'
port = 443
region = 'eu-west-1'

credentials = boto3.Session().get_credentials()
auth = AWSV4SignerAuth(credentials, region)

client = OpenSearch(
    hosts = [{'host': host, 'port': port}],
    http_auth = auth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

index_name = 'python-test-index'
index_body = {
  'settings': {
    'index': {
      'number_of_shards': 4
    }
  }
}

document = {
  'title': 'Moneyball',
  'director': 'Bennett Miller',
  'year': '2011'
}

def os_create_index(index_name, index_body):
    response = client.indices.create(
        index_name, 
        body=index_body
    )
    json_result = json.dumps(response, sort_keys=True, indent=4)
    return json_result

def os_delete_index(index_name):
    response = client.indices.delete(
        index = index_name
    )
    json_result = json.dumps(response, sort_keys=True, indent=4)
    return json_result
    
def os_index_document(index_id, index_name, document):
    response = client.index(
        id = index_id,
        index = index_name,
        body = document,
        refresh = True
    )
    json_result = json.dumps(response, sort_keys=True, indent=4)
    return json_result
    
def os_search_document(index_name, query):
    response = client.search(
        body = query,
        index = index_name
    )
    json_result = json.dumps(response, sort_keys=True, indent=4)
    return json_result
    
def os_delete_document(index_id, index_name):
    response = client.delete(
        id = index_id,
        index = index_name
    )
    json_result = json.dumps(response, sort_keys=True, indent=4)
    return json_result

