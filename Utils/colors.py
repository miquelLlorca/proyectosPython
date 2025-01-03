

def get_gradient(a, b, n):
    '''
    From 2 colors and n steps returns a list with the colors
    Args: (a, b, n)
    '''
    gradient = []
    diff = [(b[i]-a[i])/n for i in range(3)]
    for i in range(1,n+1):
        gradient.append([int(a[j]+diff[j]*i) for j in range(3)])
    return gradient



def get_big_gradient(cols, n):
    '''
    From a list of colors and n steps, returns a list with the colors
    Args: (cols, n)
    '''
    nc = len(cols)-1
    gradient = []
    for i in range(nc):
        gradient += get_gradient(cols[i], cols[i+1], int(n/nc)+1)
    return gradient
