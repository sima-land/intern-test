from flask import Flask, request, render_template
from data.get_recommendations import find_recommendations, check_id
import test_app

app = Flask(__name__, template_folder="data/templates")
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('recommendations.html')

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

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
