# bubble sort

def bubble_sort(sequence):

    for y in range(len(sequence)-1):
        for x in range(len(sequence)- 1 - y):
            if sequence[x] > sequence[x+1]:
                sequence[x], sequence[x+1] = sequence[x+1], sequence[x]
    print (sequence)

sequence_1 = []
sequence_2 = [1,2,5,3,1,7,9,1,12,83,1,5,3,2]
sequence_3 = [1,1,1,1,1,1,1,2,1,1,1]
sequence_4 = [2,2,2,2]
sequence_5 = [1,2]
sequence_6 = [2,1]

bubble_sort(sequence_1)
bubble_sort(sequence_2)
bubble_sort(sequence_3)
bubble_sort(sequence_4)
bubble_sort(sequence_5)
bubble_sort(sequence_6)
