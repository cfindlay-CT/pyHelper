import supabaseHelper.supabaseClient as sc
import FileAndDirectory.directory as directory


# Example usage
directory_path = r''  # Change this path
bucketName = ''
bucketExists = sc.bucket_exists(bucketName)
sc.list_buckets()
print('Bucket exists: ', bucketExists)

content = directory.list_files_by_folder(directory_path)

for dir in content:
    print(dir)
    sc.list_folders_in_bucket(bucketName)
print(content)
