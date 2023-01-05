# Solving hanoitower problem: count how many moves of n disks by recursive
# if we move 3 disks, we have to solve the subproblem of moving 2 disks(1,2) plus 1 move of disk 3
# if we move 4 disks, we have to sole the subproblem of moving 3 disks(1,2,3) plus 1 move of disk 4

def hanoitower(numDisks) :
    if  numDisks <= 2:
        return (2 * numDisks - 1)
    else:
        return 2 * hanoitower(numDisks - 1) + 1

num = 4
print(f"In hanoi tower, to move {num} disks we need {hanoitower(num)} moves")
