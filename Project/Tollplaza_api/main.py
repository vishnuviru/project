from Tollplaza_api_app.models import Main
import random
for i in range(1,2):
    v_no = random.choice(['DL09ML6778','MH05TL9000','TN06BC2323'])
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
    user = random.choice(['aravind','dinesh','gurunath','raju','venkatram','vignesh','ravi','sandeep'])
    off = random.choice(['ravishandran','shankar','hari','vishnu'])
    ax = random.randint(2,7)
    vt = random.choice(['HCVN1N3'])
    loc = "TADA"
    laneno = random.randint(1,10)
    di = random.choice(['incoming','outgoing'])
    w = random.randrange(1000,4000,200)
    h = random.randint(10, 20)
    m = random.randint(10, 57)
    s = random.randint(10, 58)
    a = random.randint(1, 9)
    c = random.randint(1, 9)
    b = random.randint(10, 27)
    tim = "2017-"+"0"+str(a)+"-"+str(b)+" "+str(h)+":"+str(m)+":"+str(s)
    reg = random.choice(['2001-03-29','1999-07-18','2007-10-15','2010-01-02','2002-12-22'])
    ch = random.choice(['MHCSFR2536','HJSFGT562G','SGHJRUC23J','JSHDYE2234'])
    en = random.choice(['DF23HJ34','HDJK5623'])
    fuel = random.choice(['PETROL'])
    engcc = random.choice(['1000cc','700cc','900cc','1150cc','2000cc','300cc','1400cc','500cc','600cc','850cc'])
    tax = "2017-0"+str(g)+"-"+str(ee)
    ins = "2017-0"+str(r)+"-"+str(y)
    naper = "2017-0"+str(p)+"-"+str(q)
    aut = "2017-0"+str(r)+"-"+str(y)
    fine = random.randrange(100,1000,50)
    comment = random.choice(['permit','denied'])
    clas = random.choice(['LMV-TR'])
    sh = random.randint(4, 8)
    sl = random.randint(7, 12)
    sb = random.randint(5, 9)
    sa = random.randint(3,7)
    unla = random.randrange(500,800,50)
    la = w-unla
    sta = random.choice(['OK','NOTOK'])
    image1 = "/media/images/image"+str(a)+".jpg"
    image2 = "/media/images/image"+str(c)+".jpg"
    z = Main(Transaction_Id = i,Vehicle_Number = v_no,Dimension_Height = dh,Dimension_Length = dl,Dimension_Breadth = db,Pollution = poll,Fitness = fit,Permit= per,User_Name= user,Officer_Name = off,Axle= ax,Vehicle_Type = vt,Location = loc,Lane_Number = laneno,Direction = di,Weight = w,Timestamp = tim,Registration_Date = reg,Chassis_Number = ch,Engine_Number = en,Vehicle_Fuel_Type = fuel,Engine_Cubic_Capacity = engcc,Tax = tax,Insurance = ins,National_Permit = naper,Authorization = aut,Laden_Weight = la,Unladen_Weight = unla, Fine_Amount = fine,Comment = comment,Vehicle_Class = clas,Sensor_Height = sh,Sensor_Length  = sl,Sensor_Breadth = sb,Sensor_Axle = sa,Vehicle_Status = sta,Image_1 = image1,Image_2 = image2)
    z.save()

    
    
    
    
    
