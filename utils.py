
def dot_product(l1, l2):
    return_value = 0
    for i in range(len(l1)):
        return_value += l1[i]*l2[i]
    return return_value

def avr_lists(l):
    return_list = [sum(vals)/len(l) for vals in zip(*l)]
    return return_list
