customer_name = input('Customer Name: ')
price_size = {'l':15.99, 'm':12.99, 's':10.99}
name_size = {'l':'Large','m':'Median','s':'Small'}
toppings_options = {'1':'Peperoni','2':'Beef','3':'Pineapple','4':'Sausage','5':'Chicken','6':'Veggie'}

toppings_all_pizza = []
size_selected = []
num_of_pizza = 1
total = []


def choose_size():
    while 1:
        for i in name_size.keys():
            print(f'{name_size[i]} = ${price_size[i]}')
        size = input('Size of Pizza: l --> large, m --> median, s --> small: ')
        if size not in ['l','m','s']:
            continue
        else:
            break
    return size  #'s','m', or 'l'

def choose_toppings():   
    while True:
        out_of_menu = False
        print('Each additional topping is $3. Please choose your toppings. We have:')
        for count, i in enumerate (toppings_options.values()):
            print(count+1,i)
        toppings_selected = input('Choose your toppings. Use comma "," to seperate your selection.\n\
        If you want for example two Peperoni and one Beef, enter "1,1,2": ').split(',')
        try:
            for i in toppings_selected:
                if int(i) > len(toppings_options):
                    print(i,' is out of menu')
                    out_of_menu = True
                    break
            if out_of_menu == True:
                continue
            break
        except ValueError:
            print('Invalid input...')
            continue  
    return toppings_selected     # ['1','2','3']    

def calc_price():   
    price = price_size[size] + len(toppings_selected)*3
    return price
           
def print_cart():
    toppings_one_pizza = []
    size_selected.append(name_size[size]) # make a size list
    
    for i in toppings_selected:
        toppings_one_pizza.append(toppings_options[i])
    toppings_all_pizza.append(toppings_one_pizza) # make a topping list
    total.append(price) # make a price list
    
    for i in range(num_of_pizza):
        print(f'You have 1 {size_selected[i]} pizza with {",".join(toppings_all_pizza[i])} in your cart. ${total[i]:.2f}')
    
    print(f'Your total is ${sum(total):.2f}')

def more_order():
    while True:
        more = input('Order more pizza? y/n: ').lower()
        if more in ['no','n']:
            print('Thank you. We will get your order ready')
            return more
        elif more not in ['y','yes']:
            continue
        else:
            return more
    
more_pizza = True
while more_pizza:
    size = choose_size()
    toppings_selected = choose_toppings()
    price = calc_price()
    print_cart()
    more = more_order()
    num_of_pizza += 1
    if more in ['n','no']:
        break
    
