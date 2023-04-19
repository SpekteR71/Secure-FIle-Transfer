import string
import random
 
def random_string_generator(n):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
    res = bytes(res, 'utf-8')
    return res


#print("The generated random string : " + str(res))
#print(random_string_generator(16))
