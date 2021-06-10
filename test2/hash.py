import hashlib
import os


def hash_file(algorithm, filename, check):
    h = hashlib.md5()
    if algorithm != 'md5':
        if algorithm == 'sha1':
            h = hashlib.sha1()
        else:
            h = hashlib.sha256()
    with open(filename, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
        summ = h.hexdigest()
        if check == summ:
            print(filename, "OK")
        else:
            print(filename, "FAIL")

def analyze(searchfile):
    with open(searchfile, "r") as file:
        while True:
            line = file.readline()
            if not line:
                print("Всё")
                break
            list1 = line.split(' ')
            filename = list1[0]
            check_file = os.path.exists(filename)
            if check_file:
                alg = list1[1]
                check_sum = list1[2].strip('\n')
                hash_file(alg, filename, check_sum)
            else:
                print(filename, "Not found")

analyze("hash.txt")