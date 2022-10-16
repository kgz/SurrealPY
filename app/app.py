import asyncio
import random
import string
from typing import Optional

from flask import Flask, jsonify, request
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)
from modules.database import database
from user.user import AnonymousUser, User

login_manager = LoginManager()
app = Flask(__name__)
login_manager.init_app(app)
login_manager.anonymous_user = AnonymousUser
# set session key
app.secret_key = random.choice([string.ascii_letters, string.digits]) * 32

@login_manager.user_loader
async def load_user(user_id):
    return await User.get(user_id)

@app.route('/')
async def hello_world():
    return 'Hello, World!'


@app.route('/api')
async def api():
    return 'Hello, World!'

# set unauthorized handler
@login_manager.unauthorized_handler
def unauthorized():
    return jsonify({"error": "Unauthorized"}), 401

@app.route('/api/me')
@login_required
async def me():
    user: User = current_user
    # if not user.is_authenticated:
    #     return jsonify({"error": "Unauthorized"}), 401
    print(user.is_authenticated)
    return jsonify(user.__dict__)

@app.route('/api/user/signup', methods=['GET'])
async def signup():
    username = request.args.get('username')
    email = request.args.get('email')
    password = request.args.get('password')
    user = await User.signup(username, email, password)
    if user:
        login_user(user)
        return jsonify(user.id)
    return jsonify(False)


@app.route('/api/user/login', methods=['POST'])
async def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User(username)
    check = await user.check_password(username, password)
    if (check):
        login_user(user)
        print(current_user)
        return jsonify({"success": True})
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@app.route('/api/user/logout', methods=['GET'])
@login_required
async def logout():
    logout_user()
    return 'success'    

@login_manager.user_loader
def load_user(id) -> Optional[User]:
    # u = self.app.database.getUser(id)
    # if u:
    return User(id)
    # else:
    #     return None

async def main():

    import hupper
    from waitress import serve
    h = hupper.start_reloader("app.wrapper")
    h.watch_files(["/server", "/modules", "/cronjobs"])
    serve(app, host="0.0.0.0", port=80, threads=4) 

def wrapper():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

if __name__ == "__main__":
    wrapper()