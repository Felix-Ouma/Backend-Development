def d():
    animal = 'Elephant'
    def e():
        nonlocal animal
        animal = "Girafe"
        print('Inside nested funnction: ' + animal)
    print('Before calling funtion: '+ animal)
    e()
    print('After calling function: ' + animal)
animal = 'Camel'
d()
print('Global animal: ' + animal)