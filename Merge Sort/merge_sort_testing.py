from merge_sort import mergesort
from time import time
import random
import matplotlib.pyplot as plt

# we want to creat list with different length
#lengths_to_run = [5, 50, 500, 1000, 10000]
# lengths_to_run = [random.randint(1, 100) for i in range(1, random.randint(6, 100))]
lengths_to_run = [i for i in range(1, 5000, 50)]

sorted_lists_results = []
inversely_sorted_lists_results = []
random_lists_results = []
time_to_run = 0
total = []
# max_iterations = int(input("Enter the amount of iterations you want to do: "))
max_iterations = 1


def run_sort(list_, scenario):
    if scenario == "good":
        pass
    elif scenario == "base":
        random.shuffle(list_)
    elif scenario == "worse":
        list_ = list_[::-1]

    iterations = 0

    while iterations < max_iterations:
        iterations += 1

        time_begin = time()
        mergesort(list_)
        time_end = time()
        total_time = time_end - time_begin
        total.append(total_time)

    total_time = sum(total) / max_iterations
    return total_time


def results(scenario):
    global total
    total = []
    for lengths in lengths_to_run:
        list_to_be_sorted = list(range(0, lengths))
        time_elapsed = run_sort(list_=list_to_be_sorted, scenario=scenario)
        if scenario == "good":
            sorted_lists_results.append(time_elapsed)
        elif scenario == "base":
            random_lists_results.append(time_elapsed)
        elif scenario == "worse":
            inversely_sorted_lists_results.append(time_elapsed)


results("good")
results("base")
results("worse")

plt.plot(lengths_to_run, random_lists_results, color="blue", label="base")
plt.plot(lengths_to_run, sorted_lists_results, color="green", label="good")
plt.plot(lengths_to_run, inversely_sorted_lists_results, color="red", label="worse")

plt.legend()
plt.show()
print(max_iterations)
