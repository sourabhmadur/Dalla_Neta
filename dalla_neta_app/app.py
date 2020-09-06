from flask import Flask
app = Flask(__name__)


@app.route('/')
def entry():
    return "Enter your location"


@app.route('/<my_neta_url>')
def redirect_url(my_neta_url):
    return 'More info at <a href="https://myneta.info/maharashtra2019/index.php?action=show_candidates&constituency_id={}">Redirect</a>'.format(my_neta_url)

if __name__ == '__main__':
    app.run()