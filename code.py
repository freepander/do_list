#encoding=utf-8
import os,sys

#abspath = os.path.dirname(__file__)
#sys.path.append(abspath)
# os.chdir(abspath)
reload(sys)
sys.setdefaultencoding('utf-8')
import web
import time
import simplejson

cur_file_dir = os.path.split(os.path.realpath(__file__))[0]
DATA_PATH = cur_file_dir + '/data/'
TEMPLATE_PATH = cur_file_dir + '/templates/'
urls = (
		'/', 'List',
		)

app = web.application(urls, globals())
application = app.wsgifunc()

render = web.template.render(TEMPLATE_PATH, cache = False, globals={})
class List:
	def GET(self):
		base_href = web.ctx.home+'\\'
		return render.index(base_href)


if __name__ == '__main__':
	app.run()
