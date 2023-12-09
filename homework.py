import random
import string
import time
import matplotlib as plt


def generate_random_names(num_names, min_length=4, max_length=8):
    names = []
    for _ in range(num_names):
        first_name_length = random.randint(min_length, max_length)
        last_name_length = random.randint(min_length, max_length)
        first_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(first_name_length)).capitalize()
        last_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(last_name_length)).capitalize()
        names.append({"first_name": first_name, "last_name": last_name})
    return names

def selection_sort(names_list):
    n = len(names_list)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            first_name_i = names_list[min_index]["first_name"]
            last_name_i = names_list[min_index]["last_name"]
            first_name_j = names_list[j]["first_name"]
            last_name_j = names_list[j]["last_name"]

            if first_name_i > first_name_j:
                min_index = j
            elif first_name_i == first_name_j:
                if last_name_i > last_name_j:
                    min_index = j

        # Swap the minimum element with the current element
        names_list[i], names_list[min_index] = names_list[min_index], names_list[i]

    return names_list

time_ = []
for i in range(10, 10000):
    start = time.time()
    selection_sort(generate_random_names(i))
    end = time.time()
    time_.append(end-start)

x_axis = range(10, 10000)
plt.plot(x_axis, time_)