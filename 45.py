def palindrome(string):
    list(string)

    start = 0
    end = len(string)-1

    flag = 0 

    while start < end:

        if string[start] == string[end]:
            start+=1
            end-=1
        else:
            flag = 1
            break

    if flag == 0:
        print("STring is palindrome")
    else:
        print("String is not palindrome")


palindrome(input())

