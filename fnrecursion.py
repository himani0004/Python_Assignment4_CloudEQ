#using function 

# def my_function1(fname,mname,lname,gname):
#     print(fname +" "+ mname +" "+lname+" "+ gname ,"hello")
# my_function1("himani", "sharma","vashisht","guddi")
# my_function1("shivani", "sharma","vashisht","shivu")
# my_function1("riya", "sharma","vashisht","riyu")

#recursive function(when fn calls itsel again and again)
def recursive_fn(i):
    if (i>0):
        result = i + recursive_fn(i-1)
        print(result)
        return result
    else:
        result= 0
        return result
        
        # print("not any value")
recursive_fn(3)