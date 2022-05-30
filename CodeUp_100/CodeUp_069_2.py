grade = input()
data = {'A':'best!!!', 'B':'good!!', 'C':'run!', 'D':'slowly~'}
print(data[grade]) if grade in data.keys() else print('what?')
