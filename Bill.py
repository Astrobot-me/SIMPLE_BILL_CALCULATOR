import string
x = 0
t = 0
q = 0
while True:
    y = input('Enter the price of the Product or else q to Quit:-')
    if y=='q':
        print("Thanks for Choosing Us. Your Bill Total:- ₹"+ str(x))
        break
    else:
        z = input("Enter the quentity of the product:-")
        y = int(y) * int(z)
        x=x+int(y)
        print('Your Bill Total:- ₹' + str(x))

p = input("Wanna Calculate Gst on the Bill(Yes or No):-")
z = p.upper()
if z=='YES':
    g = int(input('Enter Gst percent:-'))
    t = x*g
    q = t/100
    x = int(x)+int(q)
    print('Thanks for choosing us, Your Total Sum:- ₹'+ str(x))
else:
    pass

print('Made by Aditya')

