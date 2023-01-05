# Solving hanoitower problem: print each moves when moving n disks by recursive
# if we move 3 disks, we have to solve the subproblem of moving 2 disks(1,2) plus 1 move of disk 3
# if we move 4 disks, we have to sole the subproblem of moving 3 disks(1,2,3) plus 1 move of disk 4

def hanoitower(numDisks, start, middle, destination) :
    if numDisks == 0:
        return
    elif numDisks <= 2:
    

print(hanoitower(3, "A","B", "C"))

