from collections import defaultdict
logs = ["morgan string_compare", "felix string_compare", "morgan reverse", "rohan sort", "andy reverse", "morgan sqrt"]
def solution(logs):
    answer = []
    problem_l = defaultdict(set)
    user_l = set()
    for log in logs:
        user, problem = map(str, log.split())
        user_l.add(user)
        problem_l[problem].add(user)
    for item in problem_l.items():
        if len(item[1]) >= len(user_l)/2:
            answer.append(item[0])
    answer.sort()
    return answer
print(solution(logs))
10-32