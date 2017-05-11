from Tollapp.models import Rto
import random
for i in range(1,41):
    v_no = random.choice(['TN06CD1190','AP16T3680','KA19Y7777','MH11J8990','PY22K1919','GA01Q5233','GJ08U7567','TN02U0001','TN12T1234'])
    dh = random.randint(6, 9)
    dl = random.randint(4, 12)
    db = random.randint(4, 8)
    g = random.randint(1,9)
    ee = random.randint(10,28)
    p = random.randint(1,9)
    q = random.randint(10,28)
    r = random.randint(1,9)
    y = random.randint(10,28)
    fit = "2017-0"+str(p)+"-"+str(q)
    poll = "2017-0"+str(r)+"-"+str(y)
    per = "2017-0"+str(g)+"-"+str(ee)
    ax = random.randint(3,8)
    vt = random.choice(['HCVN1N3'])
    reg = random.choice(['2001-03-29','1999-07-18','2007-10-15','2010-01-02','2002-12-22'])
    ch = random.choice(['MHCSFR2536','HJSFGT562G','SGHJRUC23J','JSHDYE2234'])
    en = random.choice(['DF23HJ34','HDJK5623'])
    fuel = random.choice(['PETROL','DIESEL'])
    engcc = random.choice(['1000cc','700cc','900cc','1150cc','2000cc','300cc','1400cc','500cc','600cc','850cc'])
    tax = "2017-0"+str(g)+"-"+str(ee)
    ins = "2017-0"+str(r)+"-"+str(y)
    naper = "2017-0"+str(p)+"-"+str(q)
    aut = "2017-0"+str(r)+"-"+str(y)  
    clas = random.choice(['LMV-TR'])
    unla = random.randrange(500,800,50)
  
    z = Rto(id = i,Vehicle_Number = v_no,Diemension_Height = dh,Diemension_Length = dl,Diemension_Breadth = db,Pollution = poll,Fitness = fit,Permit= per,Axle= ax,Vehicle_Class_Type = clas,Registration_Date = reg,Chassis_Number = ch,Engine_Number = en,Vehicle_Fuel_Type = fuel,Engine_Cubic_Capacity = engcc,Tax = tax,Insurance = ins,National_Permit  = naper,Authorization = aut,Unladen_Weight = unla, Vehicle_Type = vt)
    z.save()

    
    
    
    
    
