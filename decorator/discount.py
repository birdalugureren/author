from datetime import datetime


def discount(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            print("sale price: 35 €")
    return wrapper


@discount
def make_a_sale():
    print("sale price: 50 €")


#make_a_sale = discount(make_a_sale)

make_a_sale()