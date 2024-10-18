num = 3
if num <= 1:
    print(False)
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("素数ではない")
            break
    else:
        print("素数である")