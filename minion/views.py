from flask import Blueprint, jsonify, request

from os import popen


view = Blueprint("view", __name__)


@view.route("/api/run/", methods=['POST'])
def minion_run():
    """
    Minion api

    post:
      { 'command': 'ls -l' }

    return:
      { 'result': 'ls -l output'}
    """
    content = request.get_json(force=True)

    if 'command' not in content:
        return jsonify(dict(message='In correct instructions, Master')), 400

    result = popen(content['command']).read()
    return jsonify(dict(result=result))
