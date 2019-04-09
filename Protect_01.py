from flask import Flask, request, jsonify
import os
project = Flask(__name__)
file_path = "E:\imagin\test"

@project.route('/api/Project', methods=['POST'], strict_slashes=False)
def build_project():
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    f = request.files
    f.save(os.path.abspath.join(file_path, f.filename))
    return jsonify({"errno": 'wrong', "errmsg": "上传成功"})

@project.route('api/Project', methods=['DELETE'])
def delete_project():
    if os.path.exists(file_path):
        pass
    else:
        return jsonify({"Destination file does not exist"})


@project.route('api/Project', methods=['GET'])
def get_project():



@project.route('api/Project', methods=['PUT'])
def edit_project():
    pass