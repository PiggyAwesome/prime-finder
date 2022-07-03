# prime-finder
a simple Python program for finding prime numbers

This can be imported as a library or you can test it by running it directly.

### Example:
```py
from primefinder import isPrime

start_at = 0 # the number that the program should start checking at
check_until = 100 # the number that the program should stop checking at

for i in range(check_until):
  i += start_at
  success, reason = isPrime(i)
  if success:
    print(f"{i}", end=" ")

```
this will print all the prime numbers between 0 and 100 
