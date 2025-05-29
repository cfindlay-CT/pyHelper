from supabase import create_client, Client
import systemHelper as sysHelper

import FileAndDirectory.file as fs

# Initialize Supabase client
SUPABASE_URL = sysHelper.geGetEnvValue("supabaseUrl")
SUPABASE_SERVICE_KEY = sysHelper.GetEnvValue("supabase_service_key")
SUPABASE_KEY = sysHelper.GetEnvValue('supabaseKey')

supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)


def upload_file_to_bucket(bucket_name: str, file_path: str, storage_path: str):
    with fs.OpenFile(file_path, "rb") as f:
        data = f.read()

    response = supabase.storage.from_(bucket_name).upload(storage_path, data, {
        "content-type": "application/octet-stream",
        "cache-control": "3600"
    })

    if response.get("error"):
        raise Exception(f"Upload failed: {response['error']['message']}")
    
    print("File uploaded successfully.")
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
    
def list_folders_in_bucket(bucketName: str):
    try:
        buckets = supabase.storage.from_(bucketName).list('folders')
        print(buckets)
    except Exception as e:
        raise Exception('failed to get folders in bucket')