from supabase import create_client, Client
import systemHelper.osHelper as sysHelper
from supabaseHelper.supbase_storage_item_listing import SupabaseFolderListing
import FileAndDirectory.file as fs

# Initialize Supabase client
SUPABASE_URL = sysHelper.getEnvValue("supabaseUrl")
SUPABASE_SERVICE_KEY = sysHelper.getEnvValue("supabase_service_key")
SUPABASE_KEY = sysHelper.getEnvValue('supabaseKey')

supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

def upload_folder(bucketName: str, folderName: str):
    try:
        res = supabase.storage.from_(bucketName).upload(folderName, b'', {'content-type': 'text/plain'})
    except Exception as e:
        print('Exception creating folder ', e)

def upload_file_to_bucket(bucket_name: str, file_path: str, storage_path: str):
    with fs.OpenFileRead(file_path, 'rb') as f:
        data = f.read()

    try:
        response = supabase.storage.from_(bucket_name).upload(storage_path, data, {
            "content-type": "application/octet-stream",
            "cache-control": "3600"
        })
    except Exception as e:
        print(f"Upload failed: {response}")
    
    return response

def create_storage_bucket(bucket_name: str, public: bool = False):
    response = supabase.storage.create_bucket(bucket_name, {"public": public})
    
    if response.get("error"):
        raise Exception(f"Bucket creation failed: {response['error']['message']}")
    
    print(f"Bucket '{bucket_name}' created successfully.")
    return response

def bucket_exists(bucket_name: str) -> bool:
    try:
        buckets = supabase.storage.list_buckets()
        return any(bucket.name == bucket_name for bucket in buckets)
    except Exception as e:
        raise Exception(f"Failed to list buckets: {e}")
    
def list_buckets():
    try:
        buckets = supabase.storage.list_buckets() 
        print('bucket count: ', len(buckets))
        for bucket in buckets:
            print('Bucket Name: ', bucket.name)
    except Exception as e:
        raise Exception('failed to list buckets {e}')
    
def list_folders_in_bucket(bucketName: str, folder: str = ''):
    try:
        buckets = supabase.storage.from_(bucketName).list(folder)
        return buckets
    except Exception as e:
        raise Exception('failed to get folders in bucket')
    
def list_files_in_bucket(bucketName: str, folder: str = ''):
    try:
        filesInBucket = supabase.storage.from_(bucketName).list(folder)
        return SupabaseFolderListing(bucketName + '/' + folder, filesInBucket)
    except Exception as e:
        raise Exception(f'failed to get folders in bucket {bucketName}/{folder}')
    
def insert_into_table(table_name: str, data: dict):
    try:
        supabase.table(table_name).insert(data).execute()
        print(f'Successfully inserted data into {table_name}: {data['name']}')
    except Exception as e:
        raise Exception(f'Failed to insert into {table_name} data - {data}, error {e}')
    
def get_records_from_table(table_name: str, filters: dict = None):
    try:
        query = supabase.table(table_name)
        if filters:
            for key, value in filters.items():
                query = query.eq(key, value)
        response = query.select("*").execute()
        return response.data
    except Exception as e:
        raise Exception(f'Failed to get records from {table_name}, error {e}')