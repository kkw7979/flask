from flask import Flask, render_template, request
import random
from datetime import datetime, time

app = Flask(__name__)

# 가상의 주식 목록
stocks = ['AAPL', 'GOOG', 'MSFT', 'AMZN', 'TSLA']

def is_valid_time():
    # 현재 시간을 가져옴
    now = datetime.now().time()
    # 지정한 범위 내에 있는지 확인
    return time(19, 0) <= now <= time(8, 0)

# 댓글을 저장할 파일
comment_file = 'comments.txt'

@app.route('/')
def index():
    if is_valid_time():
        # 추천 주식을 반환
        recommended_stock = random.choice(stocks)
    else:
        recommended_stock = "지금은 추천 주식을 받을 수 없는 시간입니다."

    # 이전 댓글 불러오기
    with open(comment_file, 'r', encoding='utf-8') as file:
        comments = file.readlines()

    return render_template('index.html', stock=recommended_stock, comments=comments)

@app.route('/comment', methods=['POST'])
def add_comment():
    # 사용자가 입력한 댓글
    new_comment = request.form['comment']

    # 새로운 댓글을 파일에 추가
    with open(comment_file, 'a', encoding='utf-8') as file:
        file.write(new_comment + '\n')

    return index()

if __name__ == '__main__':
    app.run(debug=True)
