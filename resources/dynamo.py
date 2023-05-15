import boto3

tableName = ""
dynamo = boto3.resource('dynamodb', region_name='us-west-1').Table(tableName)

def dy_db_create(x):
    dynamo.put_item(**x)

def dy_db_read(x):
    dynamo.get_item(**x)

def dy_db_update(x):
    dynamo.update_item(**x)
    
def dy_db_delete(x):
    dynamo.delete_item(**x)

def dy_db_echo(x):
    return x