import requests


class FrameClass:
    def __init__(self):
        self.url = str()
        self.data = str()
        self.project = str()
        self.headers = str()
        self.classquery = str()

    def get_project_json(self):
        if self.classquery == '' or self.classquery['json'] == 'CHANGEME':
            return 'Not proper syntax, please set value: ' + str(self.classquery)
        return requests.get(
            url=self.url,
            data=self.data,
            headers=self.headers,
            params=self.classquery
        )

    def __repr__(self):
        return "url: {} ; data: {} ; project: {} ; query: {}".format(self.url, self.data, self.project, self.classquery)
