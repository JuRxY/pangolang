# This is an inline function
FUN fibonacci(n) -> IF(n <= 1) THEN RETURN n ELSE RETURN fibonacci(n - 1) + fibonacci(n - 2)

# An example of a for loop that loops 20 times
FOR i=0 TO 20 THEN
    PRINT(fibonacci(i))
END
