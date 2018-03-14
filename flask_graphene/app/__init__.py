from flask import Flask
from flask import send_from_directory
from flask import render_template

from flask_graphql import GraphQLView

from app.database import db_session
from app.schema import schema

app = Flask(__name__, static_url_path='')


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,
        context={'session': db_session},
    ),
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/s/<path:path>')
def send_static(path):
    return send_from_directory('static/dist', path)


@app.route('/', methods=['GET'])
def main_page():
    return render_template('main.html')
