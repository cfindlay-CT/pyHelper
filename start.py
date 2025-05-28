import os
import supabaseHelper.supabaseClient as sc
import FileAndDirectory.directory as directory


# Example usage
directory_path = r'C:\Users\clint\Documents\products'  # Change this path
bucketExists = sc.bucket_exists('product-images')
sc.list_buckets()
print('Bucket exists: ', bucketExists)

content = directory.list_files_by_folder(directory_path)
print(content)
