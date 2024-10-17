def checker(s):
   stack = []
   checker = {'(': ')', '{': '}', '[': ']'}
    
    for char in s:
        if char in checker:  
            stack.append(char)
        elif char in checker.values():  
            if not stack or checker[stack.pop()] != char:
                return False
    
    return not stack

string = str(input("Enter a String: "))
if(checker(string)):
    print("Valid String")
else:
    print("Invalid String")  

def check_valid(valid):
    stk=[]
    t1=('{','[','(')
    t2=('}',']',')')
    for i in valid:
        if i in t1:
            stk.append(i)
        elif i in t2:
                if(len(stk)==0):
                    print("Invalid")
                    return
                else:
                    a=stk.pop()
                    while a not in t1:
                        stk.pop()
                    
    
    if len(stk)==0:
        print("Valid")
        
    else:
        print("Invalid")
        
        
p='((()))))'
if (len(p)%2)!=0:
    print("Invalid")
else:
    check_valid(p)              



 
 
