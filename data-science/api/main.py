from flask import Flask, render_template, request, flash
from inference import build_model

app = Flask(__name__)
app.secret_key = 'some_secret'
model = build_model()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/search", methods=['POST'])
def search():
    count_uniq_users = 44958

    if request.method == 'POST':

        if request.form['user_id'].isdigit() and 0 <= int(request.form['user_id']) <= count_uniq_users:
            user_id = int(request.form['user_id'])
            df_rec = model.inference(user_id)
            return render_template('search.html', tables=[df_rec.to_html(classes='data')], titles=df_rec.columns.values)
        else:
            error = 'user id должен быть числовым в диапазоне от 0 до 44958'
            flash('user id')
            return render_template('index.html', error=error)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
