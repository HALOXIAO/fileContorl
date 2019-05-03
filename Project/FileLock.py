import threading
import pymysql
""""verson:v1.0"""
""""此FileLock的思想是通过维护一个由文件名确定表格来进行Lock，故文件名切勿相同"""

FileStore = {}


class FileLock:
    def add_file(self, name):
        FileLock[name] = 0

    def check_filelock(self, name):
        if FileLock[name] is 1:
            return False
        else:
            return True

    def delete_filelock(self, name):
        del FileStore[name]



