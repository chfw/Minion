import os
import sys
from minion.app import create_app


def main():
    if len(sys.argv) == 2:
        static_folder = os.path.join(os.getcwd(), sys.argv[1])
    else:
        static_folder = '/srv/minion/public'
    flask_app = create_app(static_folder=static_folder)
    flask_app.run(host='0.0.0.0', port=3000)
