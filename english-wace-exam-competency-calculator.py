# Imports
import itertools
import numpy as np
import sys
import time


# Key functions
def talker(script):
    """Function to 'talk' to user"""
    i = 0
    while i < (len(script)):
        print(script[i])
        time.sleep(1.25)
        i += 1
    return "radicals"


def confirm(g, t):
    """Confirms user inputs"""
    if t == 0:
        truth = input(f"Your raw school mark is {g}%? (y/n)\n"
                      ": ")
        if truth in ["yes", "y", "affirmative", "yip", "yippie doodah", "yaur", "yeah", "yuh", "yah", "yep", "yis"]:
            print("Confirmed\n")
            return True
        else:
            print("Re-inputting\n")
            return False
    elif t == 1:
        truth = input(f"Your cohort's average is {g[0]} and your cohort's standard deviation is {g[1]}%? (y/n)\n"
                      ": ")
        if truth in ["yes", "y", "affirmative", "yip", "yippie doodah", "yaur", "yeah", "yuh", "yah", "yep", "yis"]:
            print("Confirmed\n")
            return True
        else:
            print("Re-inputting\n")
            return False
    else:
        print("Confirm function received invalid input, issue with program.")
        return ValueError


def float_convert(v):
    """Outputs string as float"""
    decimal_found = False
    valid_chars = []
    for c in v:
        if c.isdigit():
            valid_chars.append(c)
        elif c == '.' and not decimal_found:
            valid_chars.append(c)
            decimal_found = True
    valid_string = ''.join(valid_chars)
    if valid_string and valid_string != '.':
        f = float(valid_string)
        print(f"Converted float: {f}\n")
        return f
    else:
        print("No valid float could be extracted\n")
        return None


# Constant for the state's performance over the years of 2016 to 2023
# 'e' is ATAR English and 'l' is ATAR Literature
years_data = {
    'eMSA_mean': [59.07, 58.54, 58.55, 57.79, 57.85, 58.84, 59.84, 59.84],  # 2023, '22, '21 ... '17, '16
    'eMSA_std': [9.49, 9.77, 9.73, 9.88, 9.72, 9.97, 10.00, 10.43],  # MSA = moderated school assessments
    'eREM_mean': [58.38, 57.75, 57.85, 57.05, 57.04, 58.15, 59.30, 59.10],  # REM = raw examination marks
    'eREM_std': [11.19, 11.57, 11.11, 11.36, 11.11, 11.44, 11.26, 12.07],
    'eCS_mean': [58.75, 58.16, 58.22, 57.42, 57.46, 58.53, 59.60, 59.50],  # CS = combined scores
    'eCS_std': [9.53, 9.89, 9.66, 9.80, 9.64, 9.95, 9.89, 10.42],
    'lMSA_mean': [66.79, 65.89, 64.48, 65.92, 67.76, 71.78, 67.81, 67.38],
    'lMSA_std': [8.87, 8.92, 9.41, 9.5, 9.19, 9.73, 9.34, 8.82],
    'lREM_mean': [66.11, 65.22, 63.88, 65.35, 67.15, 71.24, 67.27, 66.80],
    'lREM_std': [10.09, 10.27, 10.25, 10.56, 10.65, 10.10, 10.72, 9.73],
    'lCS_mean': [66.47, 65.56, 64.22, 65.65, 67.52, 71.58, 67.59, 67.18],
    'lCS_std': [8.69, 8.94, 9.18, 9.27, 9.18, 8.71, 9.30, 8.54]
}


# Step 1: Extrapolate the student's raw exam mark from their cohort's data
# Assume the student performed similarly to the cohort
# Step 2: Moderating the school mark (assuming moderation is on same scale as the exam mark)
# Step 3: Calculating the combined mark (average of raw exam mark and moderated school mark)
# Step 4: Standardising the combined mrk using the AMS parameters
# AMS first standardisation: mean = 60, std dev = 14


def calculate(raw_school_mark, REM_mean, REM_std, MSA_mean, MSA_std, CS_mean, CS_std, cohort_mean, cohort_std_dev):
    """Function that does the calculating"""
    raw_exam_mark = REM_mean + (raw_school_mark - cohort_mean) * (REM_std / cohort_std_dev)
    moderated_school_mark = MSA_mean + (raw_school_mark - cohort_mean) * (MSA_std / cohort_std_dev)
    combined_mark = (raw_exam_mark + moderated_school_mark) / 2
    scaled_combined_mark = 60 + (combined_mark - CS_mean) * (14 / CS_std)

    talker(["Calculating :^)\n"])
    spinner = itertools.cycle('-/|\\')
    for _ in range(50):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
    return raw_exam_mark, moderated_school_mark, combined_mark, scaled_combined_mark


def get_cohort_data():
    while True:
        while True:
            user_input = input("Enter your class's average/mean for the course (in %)\n: ")
            cohort_mean = float_convert(user_input)
            if cohort_mean:
                talker([f"Received cohort mean of {cohort_mean}%"])
                break
            else:
                talker(["You didn't put in a number????\n", "u fricking crazy or sum'n >:&\n",
                        "put in a real number dis time\n"])
                continue

        while True:
            user_input = input("Enter your class's standard deviation for the course\n: ")
            cohort_std_dev = float_convert(user_input)
            if cohort_std_dev:
                talker([f"Received cohort standard deviation of {cohort_std_dev}"])
                break
            else:
                talker(["You didn't put in a number????\n", "u fricking crazy or sum'n >:&\n",
                        "put in a real number dis time\n"])
                continue

        if confirm([cohort_mean, cohort_std_dev], 1):
            break
        else:
            continue

    return cohort_mean, cohort_std_dev


# noinspection PyGlobalUndefined
def main():
    global CS_std, CS_mean, REM_std, REM_mean, MSA_std, MSA_mean

    talker([
        "Hello",
        "This program is to calculate an extrapolated raw examination mark, a moderated school mark,",
        "a raw combined mark and a scaled combined mark from the user's raw school mark and their cohort's",
        "mean and standard deviation.",
        "From the scaled combined mark can the program predict whether the user attains English competency.\n"
    ])

    while True:
        user_input = input("Enter your studied English course (ATEng / ATLit)\n: ")
        if user_input.lower() == "ateng":
            # Calculating the average means and standard deviation across the years
            MSA_mean = np.mean(years_data['eMSA_mean'])
            MSA_std = np.mean(years_data['eMSA_std'])
            REM_mean = np.mean(years_data['eREM_mean'])
            REM_std = np.mean(years_data['eREM_std'])
            CS_mean = np.mean(years_data['eCS_mean'])
            CS_std = np.mean(years_data['eCS_std'])
            break
        elif user_input.lower() == "atlit":
            MSA_mean = np.mean(years_data['lMSA_mean'])
            MSA_std = np.mean(years_data['lMSA_std'])
            REM_mean = np.mean(years_data['lREM_mean'])
            REM_std = np.mean(years_data['lREM_std'])
            CS_mean = np.mean(years_data['lCS_mean'])
            CS_std = np.mean(years_data['lCS_std'])
            break
        else:
            print("Invalid input received!")
            talker([
                "Whatchu u doing?? ':~/",
                "Actually answer the question next time???"
            ])
            continue

    cohort_mean, cohort_std_dev = get_cohort_data()

    while True:
        user_input = input("Enter your raw school mark (in %) [this is your progressive mark :^)]\n: ")
        raw_school_mark = float_convert(user_input)
        if raw_school_mark:
            talker(["Thank you for cooperating."])
            if confirm(raw_school_mark, 0):
                break
            else:
                continue
        else:
            talker(["You didn't put in a number????\n", "u fricking crazy or sum'n >:&\n",
                    "put in a real number dis time\n"])
            continue

    raw_exam_mark, moderated_school_mark, combined_mark, scaled_combined_mark = calculate(raw_school_mark, MSA_mean,
                                                                                          MSA_std, REM_mean, REM_std,
                                                                                          CS_mean, CS_std, cohort_mean,
                                                                                          cohort_std_dev)

    talker([
        f"Extrapolated raw exam mark: {round(raw_exam_mark, 2)}%",
        f"Moderated school mark: {round(moderated_school_mark, 2)}%",
        f"Raw combined mark: {round(combined_mark, 2)}%",
        f"Scaled combined mark: {round(scaled_combined_mark, 2)}%"
    ])

    if scaled_combined_mark > 50.00 and not scaled_combined_mark > 100.00:
        talker([
            "\nCongratulations!",
            "You're expected to attain English competency!",
            f"with a scaled combined score of {round(scaled_combined_mark, 2)}%!",
            "But do note, this is not a sign to go comfortable.",
            "Keep studying as nothing is guaranteed",
        ])
    elif scaled_combined_mark < 50.00 and not scaled_combined_mark < 0.00:
        talker([
            "\nUh oh!",
            "You're expected to not attain English competency!",
            f"with a scaled combined score of {round(scaled_combined_mark, 2)}%!",
            "But do note, this is not a sign to give up.",
            "Keep studying as nothing is guaranteed"
        ])
    elif scaled_combined_mark == 50.00:
        talker([
            "\nWoah!",
            "You're expected to just about attain English competency!",
            f"with a scaled combined score of {round(scaled_combined_mark, 2)}%!",
            "But do note, this is not a sign to give up or become comfortable.",
            "Keep studying as nothing is guaranteed"
        ])
    elif scaled_combined_mark > 100.00:
        talker([
            "\nWowser?!",
            f"The program calculated {scaled_combined_mark}% to be your combined score?!",
            "Obviously that's impossible.",
            "Unfortunately the program failed to accurately extrapolate a combined score ;(",
            "But!",
            "You must be in a good position to attain English competency.",
            "But do note, this is not a sign to become comfortable.",
            "Keep studying as nothing is guaranteed"
        ])
    elif scaled_combined_mark < 0:
        talker([
            "Wha?!",
            f"The program calculated {scaled_combined_mark}% to be your combined score?!",
            "Obviously that's impossible.",
            "Unfortunately the program failed to accurately extrapolate a combined score ;(",
            "But!",
            "You must not be in a good position to attain English competency.",
            "But do note, this is not a sign to give up.",
            "Keep studying as nothing is guaranteed"
        ])
    else:
        talker([
            "\nWhat the?!",
            f"The program calculated {scaled_combined_mark}% to be your combined score?!",
            "But that's not supposed to happen.",
            "Please reach out to tiancado to get this matter sorted.",
            "But in the meanwhile, keep studying as nothing is guaranteed"
        ])

    i = 1
    while i < 4:
        dots = '!' * i
        print("\r{}".format(dots), flush=True, end='')
        time.sleep(0.5)
        i += 1

    print("\n\nProgram ends in\n\n")
    for b in range(10, -1, -1):
        sys.stdout.write(f"\r{b} seconds")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\n\nProgram ended, GOODBYE :^)")


if __name__ == '__main__':
    try:
        print("Hello")
        print("The program may require 'wake up call' from user at times")
        print("Press 'Enter' key to wake up the program when required")
        print("If program rans smoothly, please ignore these messages")
        print("Press 'Enter' to continue")
        input(": ")
        print("\n\n\n")
        main()
    except Exception as e:
        print(f"An error occured: {e}")
