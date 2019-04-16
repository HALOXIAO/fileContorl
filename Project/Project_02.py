
from flask import Flask, request, jsonify, send_from_directory, Response, abort
import os
import random
project = Flask(__name__)
file_path = "E:\imagin\\test"


class Func:
    def back(self, path, stag, wtag, name=None):
        if os.path.exists(path):
            return jsonify({ "msg": "%s", "ID": name}) % wtag
        else:
            return jsonify({'errmsg': '%s'}) % stag
        abort(Response("faile"))

    def send(self, path, wtag, name=None):
        if os.path.exists(path):
            return send_from_directory(file_path, name, as_attachment=True)  # as_attachment为True是下载
        else:
            return jsonify({"errormessage": "%s"}) % wtag
        abort( Response("faile"))

    def save(self, path, wtag, stag, object, name=None):
        if not os.path.exists(path):
            return jsonify({"err": "%s"}) % wtag
        else:
            object.save(os.path.join(path, name))
            return jsonify({'mes': "%s"}) % stag
        abort(Response("faile"))


@project.route('/api/Project', methods=['POST'], strict_slashes=False)
def build_project():
    func = Func()
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    number = random.randint(100, 999999)
    f = request.files['file']
    name = str(hash(number))
    f.save(os.path.join(file_path, name))
    path = file_path + '/' + name
    func.back(path, '上传成功', 'wrong', name)

@project.route('/api/Project', methods=['DELETE'], strict_slashes=False)
def delete_project():
    name = str(request.args.get('ID')) #获得文件ID
    file = file_path +'\\'+ name
    if os.path.exists(file):
        os.remove(file)
        return jsonify({'msg': '成功删除'})
    else:
        return jsonify({'fileError': "Destination file does not exist"})
    return jsonify({'err': 'test'})


@project.route('/api/Project', methods=['GET'], strict_slashes=False)
def get_project():
    name = str(request.args.get('ID'))
    if os.path.exists(file_path):
        f = open(os.path.join(file_path, name), encoding = 'cp852')
        w = open(os.path.join(file_path, 'TEMP'), 'a')
        for line in f:
            w.write(line)
        f.close()
        w.close()
        try:
            return send_from_directory(file_path, 'TEMP', as_attachment=True)#as_attachment为True是下载
        finally:
            os.remove(os.path.join(file_path, name))
    else:
        return jsonify({"errormessage": "file does not exit"})
    abort(Response("Download failed"))


@project.route('/api/Project', methods=['PUT'], strict_slashes=False)
def edit_project():
    func = Func()
    name = str(request.args.get('ID'))
    f = request.files['file']
    func.save(file_path, 'file path wrong','成功编辑', f, name)


@project.route('/api/ForkProject', methods=['PUT'], strict_slashes=False)
def fork_project():
    name = str(request.args.get('ID'))
    func = Func()
    func.send(file_path, 'file does not exit', name)


if __name__ == '__main__':
    project.run(host='127.0.0.1', port=5000)

