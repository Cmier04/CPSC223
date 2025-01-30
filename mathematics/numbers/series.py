def total_sum(*, number_list):
    '''adds up numbers in a list'''
    if number_list == []:
        return("List is empty")
    else:
        return sum(number_list)

def average(*, number_list):
    '''takes the average of numbers in a list'''
    if number_list == []:
        return("List is empty")
    return total_sum(number_list=number_list) / len(number_list) if number_list else 0
