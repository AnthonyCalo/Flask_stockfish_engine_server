import sys
import json
from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS, cross_origin
from flask_restx import Api, Resource, fields, reqparse
import os
from argparse import ArgumentParser
from stockfish import Stockfish


app = Flask(__name__)
CORS(app)

api = Api(app, title="Calo Chess Stockfish API", description="Calo Chess stockfish api")
ns = api.namespace("/", description="Calo Chess Stockfish")

recordModel = api.model("recordModel",
                        {
    "content": fields.String(readonly=True, description="record Content")
                        })

def cmdArgParser():
    parser= ArgumentParser(description="API Server chess Calo")
    flask_group = parser.add_argument_group("Rest Server Options")
    flask_group.add_argument("--port", "-p", type=int, help="Port to run server", required=True)
    flask_group.add_argument("--debug", "-d", help="debug mode")
    return parser

@ns.route("/")
class getMove(Resource):
    def post(self):
        data = request.json
        #path to stockfish executable file
        stockfish = Stockfish()
        stockfish.set_position(data["moves"])
        bestmove = (stockfish.get_best_move())
        return jsonify(bestmove)




if __name__ == "__main__":
    app.run(debug=True)