import os, sys
reload(sys)
sys.setdefaultencoding('utf-8')

from peewee import *

db = MySQLDatabase(host = '127.0.0.1', user = 'root', passwd = 'root', database = 'do_list')

class BaseModel(Model):
	class Meta:
		database = db

class Task(BaseModel):
	content = CharField()
	datetime = DateTimeField()

