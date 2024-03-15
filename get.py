from random import *


def get_input(user_input):
    global start_number
    start_number = int(user_input[:user_input.find('.')])
    to_up = 65
    for i in range(97, 105):
        user_input = user_input.replace(chr(i) + ")", chr(to_up) + ")")
        to_up += 1
    max_number = start_number
    while user_input.find(str(max_number) + ".") != -1:
        max_number += 1
    max_number -= 1
    tests = []
    options = {}
    number = start_number
    while len(user_input) != 0:
        start_ind = user_input.find(str(number) + ".")
        end_ind = user_input.find("A)")
        if user_input[start_ind:end_ind] == "":
            break
        tests.append(user_input[user_input.find(" ", start_ind) : end_ind])
        opt = []
        alpha_number = ord("B")
        alpha = chr(alpha_number)
        while user_input.find(alpha + ")") != -1:
            if number < max_number and user_input.find(alpha + ")") > user_input.find(
                str(number + 1) + "."
            ):
                break
            opt.append(user_input[end_ind : user_input.find(alpha + ")")])
            end_ind = user_input.find(alpha + ")")
            alpha_number += 1
            alpha = chr(alpha_number)
        l = user_input.find(str(number + 1) + ".")
        if l == -1:
            l = len(user_input) + 1
        opt.append(user_input[end_ind : l])
        user_input = user_input[user_input.find(str(number + 1) + ".") :]
        end_ind = user_input.find(chr(alpha_number - 1) + ")")
        if len(tests) == max_number - start_number + 1:
            user_input = user_input[1:]
        options[number] = opt
        number += 1
    return [options, tests, len(tests)]


def get_answers(
    user_input, user_answer: str, number_of_tests: int, number_of_need_tests: int
):
    number_of_tests = int(number_of_tests)
    number_of_need_tests = int(number_of_need_tests)
    for i in range(ord("0"), number_of_tests + 1):
        user_answer = user_answer.replace(str(i), "")
    user_answer = user_answer.replace(".", "")
    user_answer = user_answer.replace(".", "")
    user_answer = user_answer.replace(" ", "")
    test_numbers = [i for i in range(number_of_tests)]
    get = get_input(user_input + " ")
    if get[2] != len(user_answer):
        return [-1, -1]
    new_ans = ""
    for i in range(start_number, start_number + get[2]):
        get[1][i - start_number] = str(i) + "." + get[1][i - start_number]
    number_of_need_tests = min(number_of_need_tests, number_of_tests)
    new_tests = sample(get[1], number_of_need_tests)
    options = []
    for i in new_tests:
        options.append(get[0][int(i[:i.find(".")])])
    for i in range(start_number, start_number + len(new_tests)):
        new_ans += user_answer[int(new_tests[i - start_number][:new_tests[i - start_number].find(".")]) - start_number]
        new_tests[i -start_number] = str(i) + new_tests[i - start_number][new_tests[i - start_number].find('.') :]

    for i in range(len(options)):
        options[i] = sample(options[i], len(options[i]))
    answer = []
    for i in range(len(options)):
        al_n = ord("A")
        alph = chr(al_n)
        for j in range(len(options[i])):
            if options[i][j][0] == new_ans[i]:
                answer.append(alph)
            options[i][j] = alph + options[i][j][1:]
            al_n += 1
            alph = chr(al_n)
    for i in range(len(answer)):
        answer[i] = str(i + 1) + ". " + answer[i]
    ans = ""
    for i in range(len(new_tests)):
        ans += new_tests[i] + "\n"
        for j in range(len(options[i])):
            ans += options[i][j] + " "
        ans += "\n"
    ans += "\n"
    ans += "\n"
    ans += "JAVOBLAR: " + " ".join(answer)
    return [ans, get[2]]
