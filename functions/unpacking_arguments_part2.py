def saving_return_value_in_different_variable(a,b):
    return a+b,a-b,a*b
add,sum,multiply = saving_return_value_in_different_variable(2,8)
print(add,sum,multiply)
# print(saving_return_value_in_different_variable(5,4))
