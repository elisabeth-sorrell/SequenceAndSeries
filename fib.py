from flask import Flask, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)


class Sequence(Resource):
   def get(self, num):
      req = int(num)
      if req == 0:
         fib_num = 0
      elif req == 1: 
         fib_num = 1
      else:
         fib_num = (req - 1) + (req - 2)
      result = {'fibonacci_number' : fib_num }
      
      return jsonify(result)

api.add_resource(Sequence, '/sequence/<num>')
if __name__ == '__main__':
   app.run(port='1111')
