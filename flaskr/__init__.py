import os

from flask import Flask
from . import db

def create_app(test_config=None):
    # configuration file are relative to the instance folder
    app = Flask(__name__, instance_relative_config=True)
    
    # 设置默认配置 SECRET_KEY 设置为dev 部署时用随机值重写
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/hello')
    def hello():
        return 'Hello World!'
     
    db.init_app(app)

    
    return app

