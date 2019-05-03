import unittest
import flask
import projectGit.Project.Project_02
import requests
url = "http://127.0.0.1:5001/"
middle1 = "api/Project"

class TEST:
    def build_project_test(self):
        response = requests.get(url+ middle1 +"?ID=136917")
        print(requests)
