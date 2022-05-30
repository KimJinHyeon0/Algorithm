grade = input()

def comment(x):
    print({'A':'best!!!', 'B':'good!!', 'C':'run!', 'D':'slowly~'}.get(x, 'what?'))

comment(grade)
