import numpy as np
import random
import string
import time


# INITIALIZATION
def init(s1, s2):
    m = np.zeros((len(s1) + 1, len(s2) + 1))

    counter = 0
    for i in m:
        if counter == 0:
            # initializing the first row
            m[0] = np.arange(i.size)
        # initializing the first column
        i[0] = counter
        counter += 1
    return m


# Minimum Edit Distance (MED)
# CLASSIC DYNAMIC PROGRAMMING ALGORITHM
def med_classic(s1, s2):
    # # setting timer for running time
    start_time = time.time()
    # INITIALIZATION
    m = init(s1, s2)
    for i in range(1, m.shape[0]):
        for j in range(1, m.shape[1]):

            # first condition : i is an insertion
            con1 = m[i - 1, j] + 1

            # second condition : j is a deletion
            con2 = m[i, j - 1] + 1

            # third condition : i and j are a substitution
            if s1[i - 1] == s2[j - 1]:
                # if same letters, we add nothing
                con3 = m[i - 1, j - 1]
            else:
                # if different letters, we add one
                con3 = m[i - 1, j - 1] + 1

            # assign minimum value
            m[i][j] = min(con1, con2, con3)
    # # printing running time
    print("--- %s seconds ---" % (time.time() - start_time))
    print(m)
    return m[m.shape[0] - 1][m.shape[1] - 1]


def string_generator(size=13, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


s1 = string_generator()
s2 = string_generator()
print('String #1 : ' + s1)
print('String #2 : ' + s2)



# CLASSIC DP
result = med_classic(s1, s2)
print("{} {}".format("MINIMUM EDIT DISTANCE :", result))
