# https://stackskills.com/courses/102831/lectures/1499425

import web

urls = (
    '/(.*)', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self, name):
        return "<h1>Hello " + name +  "</h1>\nHow are you today?"

if __name__ == "__main__":
    app.run()