import math
       
def closest_pair_1D(s):
    '''Function closest_pair_1D() returns the indices of the closest pair of points of a one-dimensional (single) array.'''
    
    def sort_i_x_1D(s):
        return [u for (u, i) in sorted(enumerate(s), key = lambda p: p[1])]

    s_x = sort_i_x_1D(s)

    def distance(i,j):
        return abs(s[i]-s[j])

    def search(i, j):
        if i >= j:
            return None
        elif i + 1 == j:
            return (s_x[i], s_x[j])
        else:
            k = (i + j) // 2
            left = search(i, k)
            right = search(k, j)
            (i_left, j_left) = left
            (i_right, j_right) = right

            if left is None:
                (i_min, j_min) = right
            elif right is None:
                (i_min, j_min) = left
            else:
                d_left = distance(i_left, j_left)
                d_right = distance(i_right, j_right)
                if d_left < d_right:
                    (i_min, j_min) = left
                else:
                    (i_min, j_min) = right
            return (i_min, j_min)
    return search(0, len(s) - 1)


print (closest_pair_1D([8,4,7,10,14]))
# Function closest_pair_1D([8,4,7,10,14]) returns: (2, 0).

print (closest_pair_1D([103, 1, 14, 29, 1008, 18, 99, 81, 67, 2, 34, 208, 534, 391, 120, 4000]))
#Function closest_pair_1D([103, 1, 14, 29, 1008, 18, 99, 81, 67, 2, 34, 208, 534, 391, 120, 4000]) returns: (1, 9).
