import supabaseHelper.supabaseClient as sc
import FileAndDirectory.directory as directory
import FileAndDirectory.file as fh
import systemHelper.osHelper as sh

bucketName = sh.getEnvValue('defaultBucket')

# Example usage
def create_folder_in_bucket(folderName: str, bucketName: str):
    res = sc.upload_folder(bucketName, folderName + '/.keep')
    print('created folder')
    print(res)

def upload_files(files: list[str], path: str):
    path = path + '/'
    for file in files:
        baseName = fh.getBaseName(file)
        fullPath = path + baseName
        res = sc.upload_file_to_bucket(bucketName, file, fullPath)
        print(res)

def check_if_files_found(fileName: str):
    foldersInBucket = sc.list_folders_in_bucket(bucketName)
    foldersInBucket = [f['name'] for f in foldersInBucket]

    if fileName in foldersInBucket:
        return True
    
    return False

def main():
    directory_path = sh.getEnvValue('productFileLocation') # Change this path
    bucketName = sh.getEnvValue('defaultBucket')
    bucketExists = sc.bucket_exists(bucketName)
    print('Bucket exists: ', bucketExists)

    content = directory.list_files_by_folder(directory_path)
    print('content')
    print(content)
    for dir in content:
        files = content[dir]['files']
        directoryName = dir
        print('files', files)

        directoryExist = check_if_files_found(directoryName)
        
        if not directoryExist:
            create_folder_in_bucket(directoryName, bucketName)
            upload_files(files, directoryName)




if __name__ == "__main__":
    main()


