def perform_operation(num1, num2, operation):
    if operation == add:
        result = num1 + num2
    elif operation == subtract:
        result = num1 - num2
       # return result
    elif operation == multiply:
        result = num1 * num2
       # return result
    else:
        if num2 == 0:
            print("the second number can not be a zero")
         #   return
        else:
            result = num1 / num2
        #    return result
