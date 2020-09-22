# MAKE LIST OF ALL COMBOS OF 5 DIGITS (row_list5)
row_list3 = [[0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1]]
row_list2 = [[0,0], [0,1], [1,0], [1,1]]

row_list5 = []

for row3 in row_list3:
    for row2 in row_list2:
        row_list5.append(row3 + row2)

# remove rows with more than two 1's (which can't be in a starting grid)
rows5 = [row for row in row_list5 if sum(row) < 3]

#print(rows5)
#print(len(rows5))

# MAKE LIST OF ALL COMBOS OF STARTING ROWS
quintuples = []

for i in range(16):
    for j in range(16 - i):
        for k in range(16 - i - j):
            for l in range(16 - i - j - k):
                for m in range(16 - i - j - k - l):
                    quintuples.append([rows5[i], 
                    rows5[i+j], 
                    rows5[i + j + k], 
                    rows5[i + j + k + l], 
                    rows5[i + j + k + l + m]])

print(len(quintuples))

# ZIP INTO COLUMNS & REDUCE
quintT = [list(zip(*rows)) for rows in quintuples]

#print(len(quintT))


# take out impossible starting columns
quint_cols = [cols for cols in quintT if max([sum(t) for t in cols]) < 3]

# quint_cols = []
# for cols in quintT:
#     sums = [sum(t) for t in cols]
#     if max(sums) < 3:
#         quintuplesC.append(cols)

#print(len(quint_cols))

# take out non-unique column combinations
index1 = 0
check1 = quint_cols[index1]

index2 = 1
check2 = quint_cols[index2]

lastcheck = quint_cols[len(quint_cols) - 1]

while index1 < len(quint_cols):
    check1 = quint_cols[index1]    
    removed = 0

    for index2 in range(index1 + 1, len(quint_cols)):
        check2 = quint_cols[index2 - removed]
        nums1 = [rows5.index(list(x)) for x in check1]
        nums2 = [rows5.index(list(x)) for x in check2] #should be eg [1, 3, 2, 15, 5]

        while len(nums1) > 0:
            if max(nums1) == max(nums2):
                nums1.remove(max(nums1))
                nums2.remove(max(nums2))
            else:
                break
        
        if len(nums1) == 0:
            quint_cols.remove(check2)
            removed += 1
    
    index1 += 1

#print(len(quint_cols))

# transpose back to rows
quint_rows = list(zip(quint_cols))
#print(len(quint_rows))



