import requests

def get_fibonacci(num):
  return requests.get(_url('/sequence/fibonacci/{}'.format(num)))
def get_square(num):
  return requests.get(_url('sequence/square/{}'.format(num)))  

def _url(path):
  return 'http://localhost:1111' + path

