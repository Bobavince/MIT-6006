def prompt():
    print("Python Peak Finder 1D\n_____________________\n")

def get_2D_Standard_Peak(data):
    for indexLine, listeLine in enumerate(data):
        for index, element in enumerate(listeLine):
            isAPeak = True
            #Case 1 : there is a higher right element
            if index < len(listeLine)-1 and element < listeLine[index+1]:
                isAPeak = False
            #Case 2 : there is a higher left element
            if index > 0 and element < listeLine[index-1]:
                isAPeak = False
            #Case 3 : there is a higher upper element
            if indexLine > 0 and element < data[indexLine-1][index]:
                isAPeak = False
            #Case 4 : there is a higher down(er?) element
            if indexLine < len(data)-1 and element < data[indexLine+1][index]:
                isAPeak = False
            # Conclusion
            if isAPeak:
                return element
    return None

def getMaxIndex(line):
    maxIndex = -1
    maxValue = line[0]
    for index, element in enumerate(line):
        if maxValue < element :
            maxValue = element
            maxIndex = index
    return maxIndex

def get_2D_Efficient_Peak(data):

    #We take the row of the middle to begin with
    rowIndex = int(len(data) /2)
    #We take the middle row to begin with
    current_row = data[rowIndex]
    
    #We find the max of the row
    indexOfMaxInRow = getMaxIndex(current_row)
    #We take the value of the max in the row
    current_element = current_row[indexOfMaxInRow]
    

    for i in range(0,len(data)) :
        #We want to detect if we found a peak
            #Case 1 : we are on the first line 
        if rowIndex == 0 and current_element > data[rowIndex+1][indexOfMaxInRow]:
            return current_element
            #Case 2 : we are on the last line
        elif rowIndex == len(data)-1 and current_element > data[rowIndex-1][indexOfMaxInRow]:
            return current_element
            #Case 3 : we are on a random line
        elif rowIndex > 0 and rowIndex < len(data)-1 and current_element > data[rowIndex+1][indexOfMaxInRow] and current_element > data[rowIndex-1][indexOfMaxInRow]:
            return current_element
            
        #We want to find where we go then
        nextHighestElement = current_element
        indexOfNextHighestElement = [rowIndex,indexOfMaxInRow]
        
        if indexOfMaxInRow > 0 and nextHighestElement < data[rowIndex][indexOfMaxInRow-1]:
            #We prepare next jump
            nextHighestElement = data[rowIndex][indexOfMaxInRow-1]
            indexOfNextHighestElement = [rowIndex,indexOfMaxInRow-1]
        elif indexOfMaxInRow < len(current_row)-1 and nextHighestElement < data[rowIndex][indexOfMaxInRow+1]:
            #We prepare next jump
            nextHighestElement = data[rowIndex][indexOfMaxInRow+1]
            indexOfNextHighestElement = [rowIndex,indexOfMaxInRow+1]
        elif rowIndex > 0 and nextHighestElement < data[rowIndex-1][indexOfMaxInRow]:
            #We prepare next jump
            nextHighestElement = data[rowIndex-1][indexOfMaxInRow]
            indexOfNextHighestElement = [rowIndex-1,indexOfMaxInRow]
        elif rowIndex < len(data)-1 and  nextHighestElement < data[rowIndex+1][indexOfMaxInRow]:
            #We prepare next jump
            nextHighestElement = data[rowIndex+1][indexOfMaxInRow]
            indexOfNextHighestElement = [rowIndex+1,indexOfMaxInRow]
        
        #Prepare for the next iteration
        rowIndex = indexOfNextHighestElement[0]
        indexOfMaxInRow = indexOfNextHighestElement[1]
        current_element = nextHighestElement
    
    return None

def launch2DStandardFinder(data):
    peak = get_2D_Standard_Peak(data)
    print("Input tab : ", data, end ='\n')
    print("Peak : ", peak, end ='\n')

        
def launch2DEfficientFinder(data):
    peak = get_2D_Efficient_Peak(data)
    print("Input tab : ", data, end ='\n')
    print("Peak : ", peak, end ='\n')