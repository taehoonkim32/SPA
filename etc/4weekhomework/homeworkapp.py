from flask import Flask, render_template, jsonify, request

homeworkapp = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@homeworkapp.route('/')
def home():
    return render_template('4th_homework.html')


## API 역할을 하는 부분
@homeworkapp.route('/homeworks', methods=['POST'])
def write_homework():
    name_receive = request.form['name_give']
    number_receive = request.form['number_give']
    address_receive =  request.form['address_give']
    HP_receive = request.form['HP_give']

    homework = {
       'name': name_receive,
       'number': number_receive,
       'address': address_receive,
        'HP': HP_receive
    }

    db.homeworks.insert_one(homework)
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})


@homeworkapp.route('/homeworks', methods=['GET'])
def read_homeworks():
    homeworks = list(db.homeworks.find({},{'_id':0}))
    return jsonify({'result': 'success', 'homeworks': homeworks})


if __name__ == '__main__':
    homeworkapp.run('0.0.0.0', port=5000, debug=True)