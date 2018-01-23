from flask import Flask, render_template
import sequence_library as seq
app = Flask(__name__)


@app.route('/')
def hello_world():
   num = "7"
   resp = seq.get_fibonacci(num)
   if resp.status_code != 200:
      raise ApiError('Cannot get number: {}'.format(resp.status_code))
   fib_num = resp.json()["fibonacci_number"]

   return render_template('index.html', num=num, fib_num=fib_num)

if __name__ == '__main__':
   app.run(port='1112')
