def alive(health):
    if health < 0:
        return False
    else:
        return True


a = int(input("enter your health:\n"))
print(alive(a))
