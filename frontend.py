from flask import Flask, render_template, request, redirect
import sequence_library as seq
app = Flask(__name__)


@app.route('/calculate', methods = ['POST'])
def calculate():
   num = request.form['num']
   resp = seq.get_fibonacci(num)
   if resp.status_code != 200:
      raise ApiError('Cannot get number: {}'.format(resp.status_code))
   fib_num = resp.json()["fibonacci_number"]
   answer = "The fibonacci number of " + str(num) + " is " + str(fib_num)
   return render_template('index.html', answer=answer)

@app.route('/')
def home():
   return render_template('index.html', answer='')


if __name__ == '__main__':
   app.run(port='1112')
