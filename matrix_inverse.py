

def taking_input():
    #print("Enter values of the matrix row2 following row one. 2 value at a time")
    
    firstRow=input()
    if firstRow=="":
        firstRow=input()
        if firstRow == "":
            return None
    a,b=firstRow.split()
    c, d=input().split()
    a, b, c, d=[int(a), int(b), int(c), int(d)]
    input_matrix=[a, b, c, d]
    return input_matrix
   

def checking_values():
    input_matrices = []
    for i in range(5):
        input_matrix = taking_input()
        if input_matrix!=None:
            input_matrices.append(input_matrix)
            
        else:
            break
    determinant(input_matrices)
            
       
def determinant(input_matrices):
    for i in range(len(input_matrices)):
        a = input_matrices[i][0]
        b= input_matrices[i][1]
        c = input_matrices[i][2]
        d = input_matrices[i][3]
        determinant=((a*d)-(b*c))
        if determinant == 0:
            print("Inverse does not exist")
        else:
            inverse_a=int(d/determinant)
            inverse_b=int(-b/determinant)
            inverse_c=int(-c/determinant)
            inverse_d=int(a/determinant)
            inverse_matrices = [[inverse_a, inverse_b],[inverse_c, inverse_d]]
            print("Case ",i+1,":")
            for i in range(2):
                
                print(inverse_matrices[i][0]," ", inverse_matrices[i][1])
            
        
        



def main():
    checking_values()



if __name__ == "__main__":
    main()

