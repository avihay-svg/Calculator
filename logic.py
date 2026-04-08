# Global variables
A = 0
operator = None
B = None


# Clear all function
def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None


# Removing decimal in case the number has none
def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)
