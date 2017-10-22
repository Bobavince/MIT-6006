def prompt():
    print("Python Peak Finder 1D\n_____________________\n")

def get_1D_Standard_Peak(data):
    for index, element in enumerate(data):
        #Case 1 : first case of the tab
        if index == 0 and element > data[index+1]:
            return element
        #Case 3 : last case of the tab
        elif index == [len(data)-1] and element > data[index-1]:
            return element
        #Case 2 : random case of the tab
        elif element > data[index-1] and element > data[index+1]:
            return element
    return None

def get_1D_Efficient_Peak(data):
    index = int(len(data) /2)
    element = data[index]
    #Case 1 : le tableau n'a plus qu'une case
    if len(data)==1:
        return element
    #Case 2 : la case est plus grande que sa voisine de gauche et droite
    elif element > data[index-1] and element > data[index+1]:
        return element
    #Case 3 : la case n'est pas un pic, sa voisine est plus grande (gauche)
    elif element < data[index-1]:
        return get_1D_Efficient_Peak(data[index:len(data)-1])
    #Case 4 : la case n'est pas un pic, sa voisine est plus grande (droite)
    elif element < data[index+1]:
        return get_1D_Efficient_Peak(data[0:index])
    return None
    
def launch1DStandardFinder(data):
    peak = get_1D_Standard_Peak(data)
    print("Input tab : ", data, end ='\n')
    print("Peak : ", peak, end ='\n')

        
def launch1DEfficientFinder(data):
    peak = get_1D_Efficient_Peak(data)
    print("Input tab : ", data, end ='\n')
    print("Peak : ", peak, end ='\n')
