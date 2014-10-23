import os, sys

from models import *
from peewee import *

db = MySQLDatabase(host = '127.0.0.1', user = 'root', passwd = 'root', database = 'do_list')

db.connect()
db.create_tables([Task])
