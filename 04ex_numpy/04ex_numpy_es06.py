"""
6.Broadcasting
Use broadcasting to create a grid of distances.
Route 66 crosses the following cities in the US: Chicago, Springfield, Saint-Louis, Tulsa, Oklahoma City,
Amarillo, Santa Fe, Albuquerque, Flagstaff, Los Angeles.
The corresponding positions in miles are: 0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448
  * Build a 2D grid of distances among each city along Route 66
  * Convert the distances in km
  6.广播
使用广播来创建一个距离的网格。
66号公路穿越了美国的以下城市。芝加哥、斯普林菲尔德、圣路易、塔尔萨、俄克拉荷马城。
阿马里洛、圣菲、阿尔布开克、弗拉格斯塔夫、洛杉矶。
以英里为单位的相应位置是：。0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448
  * 沿着66号公路建立一个每个城市之间距离的2D网格
  * 将距离转换为公里数
"""
import numpy as np
# evenly spaced:
#cities = np.array(["Chicago", "Springfield", "Saint-Louis", "Tulsa", "Oklahoma City","Amarillo", "Santa Fe", "Albuquerque", "Flagstaff", "Los Angeles"])
miles = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])

dist_miles = np.abs(miles - miles[:, np.newaxis])

# print("Distance in miles: \n", dist_miles)
print(miles[:, np.newaxis])

dist_km = dist_miles * 1.60934
print("\nDistance in km: \n", dist_km.round())