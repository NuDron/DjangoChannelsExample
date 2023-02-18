import secrets
import os

path_init_file = 'DjangoCore/himitsu.txt'


def open_file_and_rtn_val(fielpath):
    temp = open(fielpath, 'r+').read()
    return temp


def himitsu_ni_suru():
    try:
        file_exists = os.path.exists(path_init_file)
    except FileNotFoundError as e:
        print(f"[Exception] {e}")
    if file_exists:
        print(f'[{file_exists} ]File with secret already exists ... (path: {path_init_file})')
    else:
        file = open(path_init_file, 'w')
        file.write(secrets.token_urlsafe())
        file.close()
        print(f'New secret created in {path_init_file}. File exists: {file_exists}')
    return open_file_and_rtn_val(fielpath=path_init_file)


# if __name__ == '__main__':
#     print(himitsu_ni_suru())