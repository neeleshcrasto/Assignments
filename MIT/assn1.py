
n = int(input('Enter which n(th) Prime number you want: '))

# for first prime number
if n == 1:
    prime = 2
    print ('The no.',n,'prime number is', prime)


# Generate number
if n > 1:
    nos = 1
    i = 2
    iter = 0
    while iter < n:
        iter = iter + 1
        nos = nos + 2
        for i in range(2, nos):
        # while i < nos:
            # print ('i is',iter)
            if nos%i == 0:
                print(nos,'is not prime')
                break
                # i = i + 1
            # elif nos%i != 0:
            #     print(nos)
            # # i = i + 1
        print(nos,'is prime')
        
    print('The number',n,'prime number is ',nos)
        



# check if number is prime & print it out