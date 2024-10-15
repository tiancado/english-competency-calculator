# The first prototype

# haven't programmed in forevuh but here we go :^)
import sys
import time

# Given data
# creating_weight = 0.35
# responding_weight = 0.35
# exam_weights_total = 0.30
# exam1_weight = 0.10
exam2_weight = 0.20
desired_final_grade = 0.50

# Results for assessments
# creating_results = []
# responding_results = []
# exam1_result = 0

# Calculate the weighted average for creating and responding assessments
# def average():
#     creating_average = sum(creating_results) / len(creating_results)
#     responding_average = sum(responding_results) / len(responding_results)
#     return creating_average, responding_average
#
# # Calculate the current score contribution from creating, responding and first exam
# def score(ca, ra, e1):
#     return ((ca * creating_weight) +
#             (ra * responding_weight) +
#             (e1 * exam1_weight))
#
# # Calculate the required score in the final exam to reach the desired grade
# def result(cs):
#     return (desired_final_grade - cs) / exam2_weight
#
# def calculate():
#     print(f"Creating average: {average()[0]}\n"
#           f"Responding average: {average()[1]}")
#     print(f"\nCurrent progressive mark: {score(average()[0], average()[1], exam1_result)}")
#     print(f"\nNeeded result: {result(score(average()[0], average()[1], exam1_result))}")

def calculate(c):
    i = 1
    while i < 4:
        dots = '.'*i
        print("\r{}".format(dots), flush=True, end='')
        time.sleep(1)
        i += 1
    return (desired_final_grade - (1 - exam2_weight) * c) / exam2_weight

# Communicators
def talker(script):
    i = 0
    while i < (len(script)):
        print(script[i])
        time.sleep(1)
        i += 1
    return "radicals"

def confirm():
    truth = input("\nDid you mess up and put in the wrong mark?\n"
                  ": ")
    if truth in ["yes", "y", "affirmative", "yip", "yippie doodah", "yaur", "yeah", "yuh", "yah", "yep", "yis"]:
        print("\nthank you for telling the truth")
        return True
    else:
        print("\nok it's locked in now\nno turning back around")
        return False

#Thank god for stackoverflow
# def intconvert(v):
#     digits = ''.join(c for c in v if c.isdigit())
#     if digits:
#         print(f"Converted integer {digits}\n")
#         return int(digits)
#     else:
#         return
def floatconvert(v):
    decimal_found = False
    valid_chars = []
    for c in v:
        if c.isdigit():
            valid_chars.append(c)
        elif c =='.' and not decimal_found:
            valid_chars.append(c)
            decimal_found = True
    valid_string = ''.join(valid_chars)
    if valid_string and valid_string != '.':
        f = float(valid_string)/100
        print(f"Converted float: {f}\n")
        return f
    else:
        print("No valid float could be extracted\n")
        return

# key to my survival part
def interface():
    talker(["\nNows the following may be painful but please don't worry\n",
            "It doesn't matter in the end"])
    while True:
        result_input = input("What is your current progressive mark?\n: ")
        floatinput = floatconvert(result_input)
        if floatinput:
            talker(["thank you for cooperating\n", "unless\n"])
            if confirm():
                continue
            else:
                break

    talker(["\nNOW!",
            "\nThe exam mark you need is\n",
            "calculating :^)\n"])
    required = calculate(floatinput)
    print(f"\n\n{round(required*100, 2)}%!")
    if required < 0.5:
        talker(["\nCongrats!",
                "\nIf you failed, you don't need to worry",
                "\nY'all good"])
        i = 1
        while i < 6:
            dots = '!' * i
            print("\r{}".format(dots), flush=True, end='')
            time.sleep(1)
            i += 1
    else:
        talker(["\nUh oh!",
                f"\nYou need pass the exam by {round((required-0.5)*100, 2)}%",
                "\nbut don't worry, I believe in you"])
        i = 1
        while i < 6:
            dots = '!' * i
            print("\r{}".format(dots), flush=True, end='')
            time.sleep(1)
            i += 1

    talker(["\n\noks, goodbye!",
           "\nAnd the best of luck into the future"])
    i = 1
    while i < 11:
        dots = '!' * i
        print("\r{}".format(dots), flush=True, end='')
        time.sleep(0.25)
        i += 1
    print("\n\nProgram ends in\n\n")
    for b in range(10, 0, -1):
        sys.stdout.write(f"\r{b} seconds")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\n\nProgram ended, GOODBYE :^)")

# Key to my survival
# def interface():
#     tasks = ["Task 1a Take-home Composing Imaginative",
#              "Task 2 MMFR Essay",
#              "Task 3 Comprehension",
#              "Task 1b In-class Composing Imaginative",
#              "Task 4 Semester One Exam",
#              "Task 5 Interpretative/Persuasive Composing",
#              "Task 6 SH-5 In-class Essay",
#              "Task 7 Oral Presentation"]
#     cw = [0, 3, 5]
#     rw = [1, 2, 6, 7]
#     talker(["\nNows the following may be painful but please don't worry\n",
#             "It doesn't matter in the end"])
#     p = 0
#     while True:
#         if p < 8:
#             result_input = input(f"\nWhat did you get for \"{tasks[p]}\"\n: ")
#             intinput = floatconvert(result_input)
#             if intinput:
#                 talker(["thank you for cooperating\n", "unless\n"])
#                 if confirm():
#                     continue
#                 else:
#                     if p in cw:
#                         creating_results.append(intinput/100)
#                         print(creating_results)
#                     elif p in rw:
#                         responding_results.append(intinput/100)
#                         print(responding_results)
#                     else:
#                         exam1_result = intinput/100
#                         print(exam1_result)
#                     p += 1
#                     continue
#             else:
#                 talker(["\nNo digits in the input!\n",
#                         "Let's try that again\n",
#                         "But this time put in a number :)"])
#                 continue
#         else:
#             print("Done asking :)")
#             break
#
#     calculate()
#
#     # while True:
#     #     task1_result_input = input("\nWhat did you get for \"Task 1a Composing Imaginative\"\n: ")
#     #     if intconvert(task1_result_input):
#     #         talker(["ignore that fancy bit of code but thank you for cooperating\n",
#     #                 "unless\n..."])
#     #         if confirm():
#     #             continue
#     #         else:
#     #             creating_results.append(int(task1_result_input))
#     #             break
#     #     else:
#     #         talker(["\nNo digits in the input!\n",
#     #                 "Let's try that again\n",
#     #                 "But this time don't be stupid :)"])
#     #         continue

# Intro
talker(["Hey there buddy\n",
        "I hear you wanna knowin' "
        "the score you needed to score"
        "to achieve English competency\n",
        "Wells, I gots you buddo\n",
        "Please be cooperative and answer the questions truthfully\n",
        ";)"])

interface()
