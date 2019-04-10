from flask import Flask, request, jsonify, send_from_directory, Response, abort
import os
import random
import hashlib
project = Flask(__name__)
file_path = r"E:\imagin\test"


@project.route('/api/Project', methods=['POST'], strict_slashes=False)
def build_project():
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    number = random.randint()
    f = request.files['file']
    name = hash(str(number))
    f.save(os.path.join(file_path, name))
    path = file_path + '/' + name
    if os.path.exists(path):
        return jsonify({ "msg": "上传成功", "ID": name})
    else:
        return jsonify({'errmsg': 'wrong'})
    abort(Response("upload failed"))


@project.route('/api/Project/<ID>', methods=['DELETE'])
def delete_project(ID):
    name = ID
    if os.path.exists(file_path):
        file = file_path + name
        os.remove(file)
    else:
        return jsonify({"Destination file does not exist"})
    return jsonify({'test'})


@project.route('/api/Project/<ID>', methods=['GET'], strict_slashes=False)
def get_project(ID):
    name = ID
    if os.path.exists(file_path):
        dirpath = os.path.join(project.root_path, 'upload')
        return send_from_directory(file_path, name, as_attachment=True)#as_attachment为True是下载
    else:
        return jsonify({"errormessage": "file does not exit"})
    abort(Response("Download failed"))


@project.route('/api/Project', methods=['PUT'])
def edit_project():
    pass


if __name__ == '__main__':
    project.run(host='127.0.0.1', port = 5000)