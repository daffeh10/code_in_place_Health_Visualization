
MAX_NUM = 100

def even_numbers():
    """
    prints all even numbers less than 100
    """
    for i in range(MAX_NUM):
        if i % 2 == 0:
            print(i)

even_numbers()

