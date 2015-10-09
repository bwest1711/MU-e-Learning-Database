from flask import Flask, Blueprint, send_file
from cache import cache

client_app = Blueprint('client_app', __name__,
                    static_url_path='/client',
                    static_folder='dist',
                    template_folder='dist')

@client_app.route('/')
def home():
    return send_file('client/dist/index.html')
