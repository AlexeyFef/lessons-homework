# создаем класс Address

class Address:

    address_index = 'No index'
    address_city = "No city"
    address_street = 'No street'
    address_buildind = 'No building'
    address_flat = 'No flat' 

    def __init__(self, _address_index, _address_city, _address_street, _address_buildind, _address_flat):
        self.address_index = _address_index
        self.address_city = _address_city
        self.address_street = _address_street
        self.address_buildind = _address_buildind
        self.address_flat = _address_flat
