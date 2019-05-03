import requests
url = "http://127.0.0.1:5001/"
middle1 = "api/Project"
middle2 = "api/ForkProject"

def choise_file():
    file = open(r"E:\imagin\test/%s" %(input()))
    data = {
        'file': file
    }
    return data


class TEST:
    def get_project_test(self, id):
        response = requests.get(url+ middle1 +"?ID="+str(id))
        print(response.content)

    def delete_project_test(self, id):
        response = requests.delete(url + middle1 +"?ID="+str(id))

    def build_project_test(self):
        response = requests.post(url=url+middle1, data=choise_file())

    def edit_project_test(self, id):
        response = requests.put(url=url+middle1+"?ID="+str(id))
        print(response.content)
    def fork_project_test(self, id):
        response = requests.put(url=url + middle2 + "?ID=" + str(id))

if __name__ == '__main__':
    a = TEST()
    a.get_project_test(12332112)