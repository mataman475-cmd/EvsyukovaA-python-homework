from smartphone import Smartphone

catalog = []
catalog.append(Smartphone("Apple", "iPhone 15", "+79001112233"))
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79004445566"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79007778899"))
catalog.append(Smartphone("Google", "Pixel 7", "+79000001122"))
catalog.append(Smartphone("OnePlus", "Nord N30", "+79003334455"))

print("Каталог смартфонов:")
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
