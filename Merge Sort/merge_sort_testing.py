from merge_sort import mergesort
import time
import random
import matplotlib.pyplot as plt
import seaborn as sns

# we want to creat list with different length
#lengths_to_run = [5, 50, 500, 1000, 10000]
# lengths_to_run = [random.randint(1, 100) for i in range(1, random.randint(6, 100))]
lengths_to_run = [i for i in range(1, 5000, 50)]

best_case, worst_case, base_case = [], [], []
time_to_run = 0
total = []
max_iterations = 10

def run_sort(list_, scenario):
    iterations = 0
    while iterations < max_iterations:
        iterations += 1

        if scenario == "good":
            pass
        elif scenario == "base":
            random.shuffle(list_)
        elif scenario == "worse":
            list_ = list_[::-1]

        time_begin = time.perf_counter()
        mergesort(list_)
        time_end = time.perf_counter()
        #total_time = time_end - time_begin
        total.append(time_end - time_begin)

    #print(f"total: {total}")
    #time_to_run = sum(total) / len(total)
    #print(f"total time: {total_time}")
    return sum(total) / len(total)


def results(scenario):
    for lengths in lengths_to_run:
        global total
        total = []
        list_to_be_sorted = list(range(0, lengths))
        time_elapsed = run_sort(list_=list_to_be_sorted, scenario=scenario)
        #print(time_elapsed)
        if scenario == "good":
            best_case.append(time_elapsed)
            #print(f"good senario list {best_case}")
        elif scenario == "base":
            base_case.append(time_elapsed)
        elif scenario == "worse":
            worst_case.append(time_elapsed)


results("good")
results("base")
results("worse")

sns.set_context("paper")

plt.plot(lengths_to_run, base_case, color="blue", label="base case")
plt.plot(lengths_to_run, best_case, color="green", label="best case")
plt.plot(lengths_to_run, worst_case, color="red", label="worst case")
plt.xlabel("List length")
plt.ylabel("Avg. seconds per operation")

plt.legend()
plt.show()
