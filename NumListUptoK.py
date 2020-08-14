Good morning.

This is your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

We will be sending the solution tomorrow, along with tomorrow's question. As always, feel free to shoot us an email if there's anything we can help with.

Thanks for being a supporter, and have a great day!

def findnum(input_list,k):
    flag = 0
    curr_element=list[0]
    length = len(input_list)
    for i in input_list:
        
        for j in input_list:
            
            sum = i + j
            
            if (i + j == k):
                flag = 1
    
    if (flag ==1):
        return True
    else:
        return False
                
        
    
