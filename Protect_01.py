from flask import Flask, request, jsonify, send_from_directory, Response, abort
import os
import random
project = Flask(__name__)
file_path = "E:\imagin\\test"


@project.route('/api/Project', methods=['POST'], strict_slashes=False)
def build_project():
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    number = random.randint(100, 999999)
    f = request.files['file']
    name = str(hash(number))
    f.save(os.path.join(file_path, name))
    path = file_path + '/' + name
    if os.path.exists(path):
        return jsonify({ "msg": "上传成功", "ID": name})
    else:
        return jsonify({'errmsg': 'wrong'})
    abort(Response("upload failed"))


@project.route('/api/Project', methods=['DELETE'], strict_slashes=False)
def delete_project():
    name = str(request.args.get('ID'))
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
        return send_from_directory(file_path, name, as_attachment=True)#as_attachment为True是下载
    else:
        return jsonify({"errormessage": "file does not exit"})
    abort(Response("Download failed"))


@project.route('/api/Project', methods=['PUT'])
def edit_project():
    pass


if __name__ == '__main__':
    project.run(host='127.0.0.1', port = 5000)