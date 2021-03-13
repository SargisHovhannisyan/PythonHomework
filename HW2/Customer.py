import ProductCheck as pc

def buy(product,num,price):
    if(pc.check(product,num)):
        print('You bought {} and spent {} price'.format(product, num*price))
    else:
        print('Sorry we are out of this product')
        
        
if __name__ == '__main__':
    buy('juice', 3, 100)