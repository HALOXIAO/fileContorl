from flask import Flask
project = Flask(__name__)


@project.route('/api/Project', methods=['POST'])
def build_project():
    pass


@project.route('api/Project', methods=['DELETE'])
def delete_project():
    pass


@project.route('api/Project', methods=['GET'])
def get_project():
    pass


@project.route('api/Project', methods=['PUT'])
def edit_project():
    pass