FUN get_input()
    PRINT("Input: ")
    VAR msg = INPUT()
    RETURN msg
END

VAR recived_msg = get_input()

PRINT("your msg was: " + recived_msg)
