import zipfile, sys


def main():
    base_zip_file_path = r'/home/hadyftw/htb/challenges/misc/eternal-loop/eternal-loop.zip'

    with zipfile.ZipFile(base_zip_file_path, 'r') as parent_zip_file:
        password = bytes('hackthebox', 'utf-8')
        parent_zip_file.extractall(pwd = password)
        next_zip_file = parent_zip_file.namelist()[0]

        while True:
            if not zipfile.is_zipfile(next_zip_file):
                break
            with zipfile.ZipFile(next_zip_file, 'r') as child_zip_file:
                try:
                        password = bytes(child_zip_file.namelist()[0].split('.')[0], 'utf-8')
                        child_zip_file.extractall(pwd = password)
                        next_zip_file = child_zip_file.namelist()[0]
                except (RuntimeError, zipfile.BadZipFile):
                    print(f"[-] The password for {next_zip_file} file is incorrect!")
                    sys.exit(1)
                

    

if __name__ == '__main__': 
    print(f"[*] Unzipping the nested zip files in progress...")
    main()