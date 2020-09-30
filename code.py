# --------------
#Palindrome funtion 
def palindrome(num):
    while True:
        num=num+1
        x=num
        sum1=0
        while (x!=0):
            x1=x%10
            sum1=sum1*10+x1
            x=x//10
        if(sum1==num):
            break
    return num
x=palindrome(1331)
print(x)
        
        


# --------------
#scramble function to ....
def a_scramble(str_1, str_2):
    str_1=str_1.lower()
    str_2=str_2.lower()
    list1=[i for i in str_2]
    l2=0
    i=0
    l=len(list1)-1
    while(i<l):
        l2=l2+str_1.count(list1[i])
        i=i+1
    if(l2>=len(str_2)):
        return True
    else:
        return False

print(a_scramble("labratory","Bat"))


    




# --------------
#Check_fib function to ....
def check_fib(num):
    a=0
    b=1
    c=0
    while(c<=num-1):
        c=a+b
        print(c)
        a=b
        b=c
    if(c==num):
        return True
    else:
        return False
    
    
check_fib(987)


# --------------
#Compress funtion .......
def compress(word):
    word=word.lower()
    res = ""

    count = 1

    #Add in first character
    res += word[0]

    #Iterate through loop, skipping last one
    for i in range(len(word)-1):
        if(word[i] == word[i+1]):
            count+=1
        else:
            if(count >= 1):
                #Ignore if no repeats
                res += str(count)
            res += word[i+1]
            count = 1
    #print last one
    if(count >= 1):
        res += str(count)
    return res
    

print(compress("Ss"))

    


# --------------
#Distinct Funtion to .....
def k_distinct(string,k):
    l=dup(string.lower())
    lenght=len(l)
    print(lenght)
    if(lenght==k):
        return True
    else:
        return False

def dup(stri):
    s=""
    j=0
    for x in stri:
        if(stri.index(x)==j):
          s+=x  
        j+=1
    return s

k_distinct('Messoptamia',8)


