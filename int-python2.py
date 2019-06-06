# Name: Shreya Sinha
# School:Champion School
# Division: Intermediate

import os
import numpy as np
import sys

# Sets direction matrices
T90 = np.matrix('0 1; -1 0')
T180 = np.matrix('1 0; 0 1')
T0 = T180
T270 = np.matrix('0 -1; 1 0')
T360 = np.matrix('-1 0; 0 -1')
fname = 'test.txt'

# Finds the value of translation
def T_val(a, pi):
    # And call translator
    if a[pi[0]][pi[1]] == 0:
        t = T0
    elif a[pi[0]][pi[1]] == 1:
        t = T90
        a[pi[0]][pi[1]] = 2
    elif a[pi[0]][pi[1]] == 2:
        t = T180
        a[pi[0]][pi[1]] = 3
    elif a[pi[0]][pi[1]] == 3:
        t = T270
        a[pi[0]][pi[1]] = 4
    elif a[pi[0]][pi[1]] == 4:
        t = T360
        a[pi[0]][pi[1]] = 1
    return t, a


# Scan the input and create the 2D array from input line #1
# Form the original array A
def originalarraycreator(firstline):
    a = np.zeros(shape =(8, 8))
    for x in range(0, len(firstline)):
        n = int(x)
        ai = np.array ([int(x) for x in bin(int(firstline[x], 16))[2:].zfill(8)])
        a[n] = ai
    return a


# Translator function input: Input position (P_i), Direction (D_i), Steps (s), Original array (A). Output: Final position (P_f)
# Apply the below operation s times
# D_f = D_i*A_r; P_f = (P_i) + D_f
def finalpos(a_r, p_i, d_i, s_i):
    for x in range (0,s):
        T, a_r = T_val(a_r, p_i)
        d_f = d_i * T
        p_f = p_i + d_f
        p_f = np.squeeze(np.asarray(p_f))
        # Wrap around properly for row, col
        if p_f[0] > 7:
            p_f[0] = 0
        elif p_f[0] < 0:
            p_f[0] = 7
        if p_f[1] > 7:
            p_f[1] = 0
        elif p_f[1] < 0:
            p_f[1] = 7
        d_i = np.squeeze(np.asarray(d_f))
        p_i = p_f
    return p_f


# Main
if __name__ == "__main__":

    # Checks if filename exists
    if os.path.exists(fname):
        pass
    else:
        print("Expression Input File test.txt doesn't exist")
        exit(1)
    z = True

    # Opens file and reads first line
    with open(fname) as f:
        firstline = f.readline().strip().split()
        # Check for error in the row value input
        if len(firstline) != 8:
            print("error")
            sys.exit()
        else:
            pass
        A = originalarraycreator(firstline)

        while z:
            A = originalarraycreator(firstline)
            # Scan inputs and get the Input position (P_i), Direction (D_i) and number of Steps s

            first_input = f.readline().strip().split()

            # Checks to see if first_input is valid
            if len(first_input) != 4 and len(first_input) != 0:
                print("error")
                sys.exit()
            else:
                pass

            # changes starting location to index
            if first_input:
                P_i = np.array([int(first_input[0])-1, int(first_input[1])-1])

                # Convert into direction vector
                if (first_input[2] == 'L'):
                    D_i = np.array([0, 1])
                elif (first_input[2] == 'R'):
                    D_i = np.array([0, -1])
                elif (first_input[2] == 'A'):
                    D_i = np.array([1, 0])
                elif (first_input[2] == 'B'):
                    D_i = np.array([-1, 0])

                # Get steps s
                s = int(first_input[3])

                P_f = finalpos(A, P_i, D_i, s)
                Final = P_f + 1
                print("%d %d")% (Final[0], Final[1])
            else:
                z = False
    f.close()
