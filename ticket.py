def calculate(adult,child):
    adult=37555.0
    child=37555/3
    total=adult+child
    service_tax=total*0.07
    discount=(total+service_tax)*0.10
    total_cost=(total+service_tax)-discount
    return total_cost
x=int(input('enter no adult:'))
y=int(input('enter no child:'))
print('discount')
print('service_tax')
print('total_cost')
