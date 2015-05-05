import random
import sys
import os

from flask import Flask

app = Flask(__name__)

# make the WSGI interface available at the top level so wfastcgi can get it.
# wsgi_app = app.wsgi_app

# import all of our routes from path.py
from path import *

app.debug = True
# launching server
if __name__ == '__main__':
    app.run()
