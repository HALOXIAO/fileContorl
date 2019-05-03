from flask import Flask, request, jsonify, send_from_directory, Response, abort
import os
import random
import filelock

project = Flask(__name__)
file_path = r"E:\imagin\test"


class Func:
    @staticmethod
    def back(path, stag, wtag, name=None):
        filepath = path + '/' + name
        if os.path.isfile(filepath):
            return jsonify({"msg": stag, "ID": name})
        else:
            return jsonify({'errmsg': wtag})

    @staticmethod
    def send(path, wtag, name=None):
        path = path + '/' + name
        if os.path.isfile(path):
            try:
                return send_from_directory(file_path, name, as_attachment=True)  # as_attachment为True是下载
            except(Exception):
                return jsonify("upload faile")
        else:
            return jsonify({"errormessage": wtag})

    @staticmethod
    def save(path, wtag, stag, obj, name=None):
        filepath = path + '\\' + name
        if os.path.isfile(filepath):
            try:
                obj.save(os.path.join(path, name))
                return jsonify({'mes': stag})
            except(Exception):
                return jsonify("saving fail")
        else:
            return jsonify({"err": wtag})


@project.route('/api/Project', methods=['POST'], strict_slashes=False)
def build_project():
    func = Func()
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    number = random.randint(100, 9999999)
    name = str(hash(number))
    try:
        f = request.files['file']
        f.save(os.path.join(file_path, name))
    except(Exception):
        return jsonify("file has sth wrong")
    path = file_path
    return func.back(path, '上传成功', 'upload wrong', name)


@project.route('/api/Project', methods=['DELETE'], strict_slashes=False)  # OK
def delete_project():
    name = str(request.args.get('ID'))  # 获得文件ID
    filepath = file_path + '/' + name
    if os.path.isfile(filepath):
        try:
            os.remove(filepath)
            return jsonify({'msg': '成功删除'})
        except(Exception):
            return jsonify("A failure occurred while deleting the file")
    else:
        return jsonify({'fileError': "Destination file does not exist"})



@project.route('/api/Project', methods=['GET'], strict_slashes=False) #OK
def get_project():
    name = str(request.args.get('ID'))
    filepath = file_path + '/' + name
    if os.path.isfile(filepath):
        f = open(os.path.join(file_path, name), encoding='cp852')
        w = open(os.path.join(file_path, 'TEMP'), 'a')
        for line in f:
            w.write(line)
        f.close()
        w.close()
        try:
            return send_from_directory(file_path, 'TEMP', as_attachment=True)  # as_attachment为True是下载
        finally:
                os.remove(os.path.join(file_path, name))
    else:
        return jsonify({"errormessage": 'without this file'})


@project.route('/api/Project', methods=['PUT'], strict_slashes=False)
def edit_project():
    func = Func()
    name = str(request.args.get('ID'))
    try:
        f = request.files['file']
        return func.save(file_path, 'file path wrong', '成功编辑', f, name=name)
    except(Exception):
        return jsonify("edit Wrong")


@project.route('/api/ForkProject', methods=['PUT'], strict_slashes=False)
def fork_project():
    name = str(request.args.get('ID'))
    func = Func()
    return func.send(file_path, 'file does not exit', name=name)


if __name__ == '__main__':
    project.run(host='127.0.0.1',
                port=5001, threaded=True,
                debug=True)
