import unittest
from flask import Flask, render_template, request
from data.get_recommendations import find_recommendations, check_id

app = Flask(__name__, template_folder="data/templates")
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('login.html')

@app.route('/get_request', methods=['GET', 'POST'])
def get_request():
    return request

@app.route('/get_user_id')
def get_user_id(form):
    return form.get('user_id')

@app.route('/recommendations', methods=['GET', 'POST']) 
def get_recommendations(): 
    request = get_request()
    user_id = get_user_id(request.form)
    user_id = check_id(user_id)

    if user_id is not None:
        recs = find_recommendations(user_id)
        return (recs.to_html(max_rows=10, index=False))
    else:
        return "Uncorrect user id"

class FlaskTestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        assert response.status_code == 200

    def test_recommendations(self):
        tester = app.test_client(self)
        response = tester.post('/recommendations', data={'user_id': 123}, follow_redirects=True)
        assert response.status_code == 200

    def test_correct_user_id(self):
        user_id = check_id('1231')
        assert user_id != None

    def test_uncorrect_user_id(self):
        user_id_1 = check_id('1231e')
        assert user_id_1 == None
        user_id_2 = check_id(999999999999999)
        assert user_id_2 ==None


if __name__ == "__main__":
        unittest.main()
