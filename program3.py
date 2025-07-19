def towers_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    towers_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    towers_of_hanoi(n - 1, auxiliary, target, source)

n = int(input("Enter number of disks: "))
towers_of_hanoi(n, 'A', 'C', 'B')
# This code implements the Towers of Hanoi problem, which is a classic recursive problem.
# The function towers_of_hanoi takes the number of disks and the names of the source, target, and auxiliary rods.