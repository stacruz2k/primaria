# https://www.codewars.com/kata/5a86073fb17101e453000258/train/python

def sort_emotions(arr, order):
    emoOrder = [':D',':)',':|',':(','T_T']
    newarr=[]
    for est in arr:
        newarr.append(emoOrder.index(est))
    newarr.sort()
    if not order:
        newarr.reverse()

    return [emoOrder[nest] for nest in newarr]

print (sort_emotions([ ':D', 'T_T', ':D', ':(' ],True))
