import os
import shutil


class OS:
    def listdir1(self, dir):
        return os.listdir(dir)

    def mkdir(self, dir_path):
        return os.mkdir(dir_path)

    def remove(self, path):
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)

    def copy(self, path1, path2):
        return shutil.copy2(path1, path2)

    def move(self, path1, path2):
        return shutil.move(path1, path2)

    def search(self, path, name):
        result = []
        for root, dirs, files in os.walk(path):
            if name in files:
                result.append(os.path.join(root, name))
        return result

    def change_permission(self, path, mode):
        return os.chmod(path, mode)


atr1 = OS()

print(atr1.listdir1(r'C:\Users\enot4\PycharmProjects\Taks'))
