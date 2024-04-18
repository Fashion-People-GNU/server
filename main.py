from flask import Flask

app = Flask(__name__)

# 루트
@app.route('/', method=['POST','GET'])
def hello_world():
    
    return 'Hello World!'

# 옷 추천
@app.route('/clothes_propose')
def propose_cloth():
    return 'clothes_propose'

# 옷 추가
@app.route('/add_clothes')
def add_clothes():
    pass

if __name__=='__main__':
    app.run()