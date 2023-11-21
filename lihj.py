while True:
    
    dic={'A':100,'T':54.50,'C':14}
    ch = int(input("Enter choice:"))

    if ch==1:
        x = int(input("Enter total no of elements to enter"))
        for j in range(x):
            e = input("Enter element code")
            f = int(input("enter mrp"))
            dic[e]=f
    

        s = 0
        n = 1
        v = []
        s1 = []
        hj = []
        m = []
        while True:
                for i in range(n):
                        a = input("enter product code")
                        if a in dic:
                                b = eval(input("enter quan"))
                                s = s+dic[a]*b
                                k = dic[a]*b
                                m.append(dic[a])
                                s1.append(k)
                                v.append(b)
                                hj.append(a)
                        else:
                            print("ERROR")
                g = input("do u wanna con")
                if g=='n':
                        print('\n',"products ordered:",hj,'\n',"product quantity:",v,'\n',"MRP",m,'\n',"product total:",s1,'\n',"sum total:",s,'/-')
                        print("THANKYOU FOR PURCHASE!...VISIT AGAIN")
                        break
                else:
                    n = 1
    d = input("DUWC")
    if d=='n':
        break
    
        
