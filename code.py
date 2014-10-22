#encoding=utf-8
import os,sys

#abspath = os.path.dirname(__file__)
#sys.path.append(abspath)
# os.chdir(abspath)
reload(sys)
sys.setdefaultencoding('utf-8')
import web
import datetime
import simplejson

from peewee import *

cur_file_dir = os.path.split(os.path.realpath(__file__))[0]

db = MySQLDatabase(host = '127.0.0.1', user = 'root', passwd = 'root', database = 'do_list')

TEMPLATE_PATH = cur_file_dir + '/templates/'

urls = (
		'/', 'List',
		'/task/create', 'Task_create',
		'/create_table', 'Util_createTable',
		)

app = web.application(urls, globals())
application = app.wsgifunc()

render = web.template.render(TEMPLATE_PATH, cache = False, globals={})
class List:
	def GET(self):
		base_href = web.ctx.home+'\\'
		task_list = Task.select()
		return render.index(base_href, task_list)

class Task_create:
	def POST(self):
		data = web.input()
		task = Task()
		task.content = data.get('content')
		task.datetime = datetime.datetime.now()
		task.save()
		web.seeother('/')


class Util_createTable:
	def GET(self):
		db.connect()
		db.create_tables([Task])

class BaseModel(Model):
	class Meta:
		database = db

class Task(BaseModel):
	content = CharField()
	datetime = DateTimeField()


if __name__ == '__main__':
	app.run()
