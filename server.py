from Flask_app import app
from Flask_app.controllers import users
from Flask_app.controllers import pies

if __name__ == '__main__':
    app.run(debug=True)