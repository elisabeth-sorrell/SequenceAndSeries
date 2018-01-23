import sequence_library as seq

resp = seq.get_fibonacci("7")
if resp.status_code != 200:
  raise ApiError('Cannot get number: {}'.format(resp.status_code))
print('Number is: {}'.format(resp.json()["fibonacci_number"]))


