class Frame_class:
    def __init__(self):
        self.url = str()
        self.data = str()
        self.project = str()
        self.headers = str()
        self.classquery = str()

    def getProjJira(self):
        if self.classquery == '' or self.classquery['jql'] == 'CHANGEME':
            return 'jiraCl.classquery is not proper syntax, please set value or update jql: ' + str(self.classquery)
        return requests.get(
            url=self.url,
            data=self.data,
            headers=self.headers,
            params=self.classquery  # this is class query var
        )

    def __repr__(self):
        return "url: {} ; data: {} ; project: {} ; query: {}".format(self.url, self.data, self.project, self.classquery)


# calculate the 50 percent of original dimensions
width = int(frame.shape[1] * 50 / 100)
height = int(frame.shape[0] * 50 / 100)
dsize = (width, height)

# resize image for display only - save the full resolution for the write to file
display = cv2.resize(frame, dsize)
imgbytes = cv2.imencode(".png", display)[1].tobytes()
window["-IMAGE-"].update(data=imgbytes)