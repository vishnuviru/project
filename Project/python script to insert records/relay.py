from Tollapp.models import Relay_Panel
import random
for i in range(1,13):
       	
    l1 = 1
    l2 = 1
    l3 = 1
    l4 = 1
    l5 = 1
    l6 = 1
    l7 = 1
    l8 = 1
    l9 = 1
    l10 = 1
    l11 = 1
    l12 = 1
    l13 = 1
    l14 = 1
    l15 = 1
    l16 = 1
    

    z = Relay_Panel(id = i,Relay_Number  = i,Lane_1 = l1,Lane_2 = l2,Lane_3 = l3,Lane_4 = l4,Lane_5 = l5,Lane_6 = l6,Lane_7 = l7,Lane_8 = l8,Lane_9 = l9,Lane_10 = l10,Lane_11 = l11,Lane_12 = l12,Lane_13 = l13,Lane_14 = l14,Lane_15 = l15,Lane_16 = l16)
    z.save()
