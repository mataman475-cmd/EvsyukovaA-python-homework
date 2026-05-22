from address import Address
from mailing import Mailing

address_to = Address(
    index="101000",
    city="Москва",
    street="Арбат",
    house="1",
    apartment="15"
)

address_from = Address(
    index="630000",
    city="Новосибирск",
    street="Ленина",
    house="100",
    apartment="42"
)

my_mailing = Mailing(
    to_address=address_to,
    from_address=address_from,
    cost=500.50,
    track="RU123456789"
)


print(
    f"Отправление {my_mailing.track} из {my_mailing.from_address.index},"
    f"{my_mailing.from_address.city}, {my_mailing.from_address.street}, "
    f"{my_mailing.from_address.house} - {my_mailing.from_address.apartment} в "
    f"{my_mailing.to_address.index}, {my_mailing.to_address.city}, "
    f"{my_mailing.to_address.street}, "
    f"{my_mailing.to_address.house} - {my_mailing.to_address.apartment}."
    f"Стоимость {my_mailing.cost} рублей."
)
