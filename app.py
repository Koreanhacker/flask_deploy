from flask import Flask, request, jsonify
import subprocess
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# 머신러닝 모델 학습 (간단한 선형 회귀 모델)
X_train = [[1], [2], [3], [4], [5]]
y_train = [2, 4, 5, 4, 5]
model = LinearRegression()
model.fit(X_train, y_train)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Streamlit에서 전달한 입력값을 JSON 형식으로 받음
    X_test = [[data['input_value']]]  # 입력값을 리스트 형태로 변환하여 예측에 사용
    prediction = model.predict(X_test)[0]  # 머신러닝 모델로 예측 수행
    return jsonify({'prediction': prediction})  # 예측 결과를 JSON 형식으로 반환

if __name__ == '__main__':
    app.run()
