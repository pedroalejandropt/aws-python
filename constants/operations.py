from resources.s3 import *
from resources.dynamo import *
from resources.opensearch import *

OPERATIONS =  {
    # dynamodb
    'db_create': dy_db_create,
    'db_read': dy_db_read,
    'db_update': dy_db_update,
    'db_delete': dy_db_delete,
    'db_echo': dy_db_echo,
    # s3 bucket
    's3_create': s3_create_bucket,
    's3_upload': s3_upload_file,
    's3_download': s3_download_file,
    's3_list_buckets': s3_list_buckets,
    # open search
    'os_create_index': os_create_index,
    'os_delete_index': os_delete_index,
    'os_search_document': os_search_document,
    'os_index_document': os_index_document,
    'os_delete_document': os_delete_document,
}