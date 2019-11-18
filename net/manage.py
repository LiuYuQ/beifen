
from flask_script import Manager,Server
from app import app

manager = Manager(app) # 注册一个manager实例，自带了runserver命令
manager.add_command("runserver",Server(host='0.0.0.0'))

@manager.command
def hello():
    """这只是一个测试命令"""
    print("OK")
    return "Hello World!"


# 下面是IDE上运行入口,可不管

if __name__ == '__main__':
    manager.run()
