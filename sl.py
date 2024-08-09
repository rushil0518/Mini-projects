inp = input("Enter 1 for encode and 2 for decode : ")   
if (inp == "1") :
  a = str(input("Enter message : "))
  stnew = []
  x = a.split() 

  for i in x :
    if (len(i) >= 3) :
        r1 = "$fg"
        r2 = "n*k"
        new = r1 + i[1:] + i[0] + r2
        stnew.append(new)
        
    else :
        y = i[::-1]
        stnew.append(y)
  print(" ".join(stnew))


elif(inp == "2") :
   b = input("Enter message : ")
   stnew1 = []
   z = b.split()
   for i in z :
      if (len(i) >= 3) :
         mod = i[-4] + i[3:-4] 
         stnew1.append(mod)
      else :
          v = i[::-1]
          stnew1.append(v)
   print(" ".join(stnew1))  
      