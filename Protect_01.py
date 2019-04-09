from flask import Flask, request, jsonify, send_from_directory, Response, abort
import os
project = Flask(__name__)
file_path = r"E:\imagin\test"


@project.route('/api/Project', methods=['POST'], strict_slashes=False)
def build_project():
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    f = request.files['file']
    f.save(os.path.join(file_path, f.filename))
    name = str(f.filename)
    path = file_path + '/' + name
    if os.path.exists(path):
        return jsonify({ "msg": "上传成功"})
    else:
        return jsonify({'errmsg': 'wrong'})


@project.route('/api/Project', methods=['DELETE'])
def delete_project():
    f = request.files['file']
    # if os.path.exists(file_path):
    #     pass
    # else:
    #     return jsonify({"Destination file does not exist"})
    return jsonify({'test'})


@project.route('/api/Project', methods=['GET'], strict_slashes=False)
def get_project(filename):
    if os.path.exists(file_path):
        dirpath = os.path.join(project.root_path, 'upload')
        return send_from_directory(dirpath, filename, as_attachment=True)#as_attachment为True是下载
    else:
        return jsonify({"errormessage": "file does not exit"})
    abort(Response("Download failed"))

@project.route('/api/Project', methods=['PUT'])
def edit_project():
    pass

if __name__ == '__main__':
    project.run(
                host='127.0.0.1',
                port = 5000)