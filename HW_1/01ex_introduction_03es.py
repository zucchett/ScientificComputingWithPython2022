from scipy.spatial import distance
#giving the points
u=(3,0) #u=(x1,y1)
v=(0,4) #v=(x2,y2)

#using scipy which has euclidean module pre built into it
euc= distance.euclidean(u,v)

print("euclidean distance = ",euc)    