VAR out = PYTHONIFY("(lambda s: len(s))(s=[1,2,3,4,5,6,7,8,9,10])") # This is how you can run python code in your pangolang code.
PRINT("Your output is:")                                            # It is still buggy and dangerous to use so avoid it as 
PRINT(out)                                                          # much as possible. It is also very slow.                                  