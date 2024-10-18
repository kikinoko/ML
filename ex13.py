def get_all_primes(n):
    prime = True 

    for num in range(2, n+1):
        #ex12.pyを利用
        if num <= 1:
            continue 
        else:
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    break  
            else:
               
                if not prime:
                    print(",", end="")
                print(num, end="")
                prime = False
    
    print()  

n = int(input())
get_all_primes(n)
