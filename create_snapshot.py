import FileAndDirectory.directory as dir

def run_3dstore():
    dir.create_snapshot(
        root="C:\\projects\\3dstore",
        include_extensions=[".ts", ".html", ".sass"],
        skip_dirs=["node_modules", ".git"],
        output_dir="C:\\projects\\3dstore\\snapshots"
    )

def run_node_api():
    dir.create_snapshot(
        root="C:\\projects\\nodeAPI",
        include_extensions=[".js"],
        skip_dirs=["node_modules", ".git"],
        output_dir="C:\\projects\\NodeAPI\\snapshots"
    )

if __name__ == "__main__":

    print('Project List')
    print('1. 3D_Store')
    print('2. Node API')
    print('--------------------')
    choice = input('Options: ')

    match choice:
        case '1':
            run_3dstore()
        case '2':
            run_node_api()

