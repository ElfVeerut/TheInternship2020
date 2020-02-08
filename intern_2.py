


inputt = float(input('Insert the Float Number From 1.0 to 10.0: '))

def is_prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):  
        if n%i==0:
            return False    

    return True

if inputt > 10.0:
    print('number too much')

else:
    while inputt != 0.0:
        str_float = str(inputt)

        separate = str_float.find('.')
        addup_float = ''
        result = []

        for i in range(0,separate):
            addup_float = addup_float+str_float[i]
        for i in range(separate+1,separate+4):
            addup_float = addup_float+str_float[i]
            result.append(is_prime(int(addup_float)))

        if True in result:
            print('TRUE')
        else:
            print('FALSE')
        
        inputt = float(input('Insert the Float Number From 1.0 to 10.0: '))