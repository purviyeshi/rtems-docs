import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '4.11.99'
release = '4.11.99'

project = "RTEMS Classic API Guide"

latex_documents = [
	('index', 'c-user.tex', u'RTEMS Classic API Guide', u'RTEMS Documentation Project', 'manual'),
]
