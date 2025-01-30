def list_of_names(scores, /):
    #if statement checking if dictionary is empty
    sort = dict(sorted(scores.items(), key = lambda item: item[1]["lastname"]))
    return sort

def student_hw_avg(scores, /, *, id):
    if id not in scores:
        print('Invalid student ID')
        return None
    else:
        for key ,value in scores.items():
            if value and "HW_scores" in key.value():
                #sum += value["HW_scores"]
                add = sum(value["HW_scores"])
                length = len(value["HW_scores"])
                average = add/length                  
        return average


def class_hw_avg(class_ave, /, *, hw_index):
    if index > 1 or index < 0:
        print('Error: Index out of range')
        return None
    else:
        for index, value in scores.items():
            if value and "HW_scores" in index.value():
                add = sum(value["HW_scores"])
        return add
                

