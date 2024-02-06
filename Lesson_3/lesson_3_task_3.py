# импортируем классы Address, Mailing, создаем новый экземпляр класса Mailing, выводим сообщение об отправлении.

from address import Address
from mailing import Mailing

new_mailing = Mailing(Address('123456', 'Москва', 'Ленина', '100', '112'), 
                      Address('352896', 'Казань', 'Попова', '22', '1'),
                      1000, '0125895-254')

print("Отправление № ", new_mailing.track, " из ", new_mailing.from_address.address_index,", город ", new_mailing.from_address.address_city, ", улица ",
new_mailing.from_address.address_street, ", дом/квартира ", new_mailing.from_address.address_buildind, "-", new_mailing.from_address.address_flat, 
", в ", new_mailing.to_address.address_index, ", город ", new_mailing.to_address.address_city, ", улица ", new_mailing.to_address.address_street, ", дом/квартира ",
new_mailing.to_address.address_buildind, "-", new_mailing.to_address.address_flat, ". Стоимость ", new_mailing.cost, " рублей.", sep = '')
