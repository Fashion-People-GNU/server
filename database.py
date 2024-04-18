import pyrebase
import json

class database:
    def __init__(self):
        try:
            with open('flask-server/authentication/firebase_auth.json') as f:
                config = json.load(f)

            firebase = pyrebase.initialize_app(config)
            self.db = firebase.database()
        except:
            print("json file open error")
        
    # 데이터 삽입
    def insert(data):
        pass

    # 데이터 가져오기
    def get():
        pass