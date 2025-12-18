import math
latitude_A = float(input("latitude titik awal : "))
radLat_A = math.radians(latitude_A)
longitude_A = float(input("longitude titik awal : "))
radLong_A = math.radians(longitude_A)
latitude_B = float(input("latitude titik akhir : "))
radLat_B = math.radians(latitude_B)
longitude_B = float(input("longitude titik akhir : "))
radLong_B = math.radians(longitude_B)
deltaLat = radLat_B - radLat_A
deltaLong = radLong_B - radLong_A
R = 6371
a = (((math.sin(deltaLat/2))**2) + (math.cos(radLat_A) * math.cos(radLat_B) * (math.sin(deltaLong/2)**2)))
d = round(2 * R * math.asin(math.sqrt(a)), 2)
print("Jarak antara 2 titik = " + str(d) +" Km")
