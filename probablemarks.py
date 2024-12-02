import random
import math
import statistics
import numpy as np

min_val = 23
max_val = 99
mean_val = 65
no_ppl = 85
neu_mean = (no_ppl * mean_val - max_val - min_val) / (no_ppl - 2)

dit = {
    "S": lambda x: x * 1.65 + mean_val,
    "A": lambda x: x * 0.85 + mean_val,
    "B": lambda x: x * 0.12 + mean_val,
    "C": lambda x: -x * 0.65 + mean_val,
    "D": lambda x: -x * 1.3 + mean_val,
}

final_values = {}
final_values2 = {}
final_error_values = {}


# nin = 0


# def random_marks_gen(minimum, maximum, mean_value):
#     global nin
#     print(nin)
#     no1 = nin + random.randint(int(minimum * 10), int((mean_value + 0.5 - nin) * 10)) / 10
#     if (mean_value - no1) > (maximum - mean_value):
#         no2 = random.randint(int(mean_value * 10), int(maximum * 10)) / 10
#         nin = 2*mean_value - no2 - no1
#     else:
#         no2 = mean_value + mean_value - no1
#         nin = 0
#     print(nin)
#     yield no1, no2


def random_marks_gen(minimum, maximum, mean_value):
    if maximum - mean_value < mean_value - minimum:
        no1 = mean_value - random.randint(0, int((maximum - mean_value) * 10)) / 10
        no2 = 2 * mean_value - no1

    else:
        no1 = mean_value + random.randint(0, int((mean_value - minimum)) * 10) / 10
        no2 = 2 * mean_value - no1

    yield no1, no2


def std_dev_calc(l1):
    return statistics.stdev(data=l1)


def error_fun(x):
    yield (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0


with open("std_devs.txt", "w") as file:
    file.write("A random number generation method:\n\n")

for i in range(0, 25):
    marks = (min_val, max_val)
    # print(neu_mean)
    for k in range(0, 90):
        marks += tuple(*random_marks_gen(minimum=min_val, maximum=max_val, mean_value=neu_mean))
        # print(statistics.mean(marks))
    print(marks)
    mean2 = statistics.mean(marks)
    print(mean2)
    standard_dev = std_dev_calc(marks)
    print(standard_dev)
    final_values[i + 1] = {s: dit[s](standard_dev) for s in dit}
    print(final_values)
    with open("std_devs.txt", "a") as file:
        file.write(f"Case:{i + 1}\nMean: {mean2}\nStandard Deviation: {standard_dev}\n{final_values[i + 1]}\n")


with open("std_devs.txt", "a") as file:
    file.write(f"\n\nTriangular distribution\n\n")

mode = 3*mean_val - max_val - min_val
rng = np.random.default_rng()
if mode < min_val or mode > max_val:
    mode = mean_val

# print(rng.triangular(min_val, mode, max_val, no_ppl))

for j in range(0, 25):
    # marks = (min_val, max_val)
    # print(neu_mean)
    # for k in range(0, 90):
    #     marks += tuple(*random_marks_gen(minimum=min_val, maximum=max_val, mean_value=neu_mean))
    #     print(statistics.mean(marks))
    # print(marks)
    marks2 = rng.triangular(min_val, mode, max_val, no_ppl)
    mean3 = statistics.mean(marks2)
    print(mean3)
    standard_dev2 = std_dev_calc(marks2)
    print(standard_dev2)
    final_values2[j + 1] = {s: dit[s](standard_dev2) for s in dit}
    print(final_values2)
    with open("std_devs.txt", "a") as file:
        file.write(f"Case:{j + 1}\nMean: {mean3}\nStandard Deviation: {standard_dev2}\n{final_values2[j + 1]}\n")


# with open("std_devs.txt", "a") as file:
#     file.write(f"\n\nTriangular distribution")




# for s in dit:
#     print(dit[s](1))
#
# for s in dit:
#     print(dit[s](3))


