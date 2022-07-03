def isPrime(i):
    for x in range(round(i/2)):
            if x != i and x != 1 and x != 0:
                try:
                    if (i % x) == 0:
                        return [False, x]
                except: 
                    pass
    return [True, 0]


check_until = 10000
start_at = 100

if __name__ == "__main__":
    for i in range(check_until):
        i += start_at
        success, reason = isPrime(i)
        if success:
            print(f"{i}", end=" ")
