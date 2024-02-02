# вызываем Smartphone, создаем таблицу, наполняем её пятью экземплярами, выводим через цикл двумя способами.

from smartphone import Smartphone
catalog = []

smartphone_1 = Smartphone('Samsung', 'A52', '+71236548511')
smartphone_2 = Smartphone('Huawei', 'P13', '+71111111111')
smartphone_3 = Smartphone('Iphone', '14Pro', '+11236548511')
smartphone_4 = Smartphone('Redmi', 'A11', '+71200000001')
smartphone_5 = Smartphone('Nokia', '3310', '+79991112233')

catalog = [smartphone_1, smartphone_2, smartphone_3, smartphone_4, smartphone_5]

for smartphone in catalog:
    print(f"Марка: {smartphone.tel_brand}, Модель: {smartphone.tel_model}, Номер телефона: {smartphone.tel_number}")

for i in range(len(catalog)):
    print(catalog[i].tel_brand, catalog[i].tel_model, catalog[i].tel_number)    
