# https://stackskills.com/courses/102831/lectures/1499426

import web

urls = (
    '/(.*)/(.*)', 'index'
)

render = web.template.render("resources/")
app = web.application(urls, globals())

class index:
    def GET(self, name, age):
        return render.main(name, age)

if __name__ == "__main__":
    app.run()