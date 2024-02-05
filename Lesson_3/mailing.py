# создаем класс Mailing почтовое отправление

from address import Address

class Mailing:

    to_address = Address
    from_address = Address
    cost = 0
    track = 'No track'

    def __init__(self, _to_address, _from_address, _cost, _track):
        self.to_address = _to_address
        self.from_address = _from_address
        self.cost = _cost
        self.track = _track
        