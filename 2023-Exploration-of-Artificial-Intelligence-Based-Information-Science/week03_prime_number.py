# week03 prime_number v0.9
start_no, end_no = map(int, input("Enter starting number and ending number : ").split())

is_prime = True

for k in range(start_no, end_no+1):
    is_prime = True
    if k < 2:
        is_prime = False
    else:
        for i in range(2, k):
            if k % i == 0:
                is_prime = False
                break
        if is_prime:
            print(k, end=' ')
