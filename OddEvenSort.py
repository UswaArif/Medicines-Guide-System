#Odd/Even Sort Ascending Function

def oddEvenSortOldpriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
   n = len(OldpriceInt)
   isSorted = 0 # isSorted is used as flag

   while isSorted == 0:
      isSorted = 1
      temp = 0
      tempOld = 0
      tempNew = 0
      tempQ = 0
      tempS = 0
      tempR = 0
      tempDis = 0
      tempDescript = 0
      #For Odd Numbers
      for i in range(1, n-1, 2):
         if OldpriceInt[i] > OldpriceInt[i+1]:
            tempOld = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[i+1]
            OldpriceInt[i+1] = tempOld

            temp = MedicineName[i]
            MedicineName[i] = MedicineName[i+1]
            MedicineName[i+1] = temp
            
            tempNew = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[i+1]
            NewPriceInt[i+1] = tempNew

            tempQ = Quantity[i]
            Quantity[i] = Quantity[i+1]
            Quantity[i+1] = tempQ

            tempS = Stars[i]
            Stars[i] = Stars[i+1]
            Stars[i+1] = tempS

            tempR = RatingInt[i]
            RatingInt[i] = RatingInt[i+1]
            RatingInt[i+1] = tempR

            tempDis = Discount[i]
            Discount[i] = Discount[i+1]
            Discount[i+1] = tempDis

            tempDescript = Description[i]
            Description[i] = Description[i+1]
            Description[i+1] = tempDescript
            isSorted = 0
       
      #For Even Numbers      
      for i in range(0, n-1, 2):
         if OldpriceInt[i] > OldpriceInt[i+1]:
            tempOld = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[i+1]
            OldpriceInt[i+1] = tempOld

            temp = MedicineName[i]
            MedicineName[i] = MedicineName[i+1]
            MedicineName[i+1] = temp
            
            tempNew = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[i+1]
            NewPriceInt[i+1] = tempNew

            tempQ = Quantity[i]
            Quantity[i] = Quantity[i+1]
            Quantity[i+1] = tempQ

            tempS = Stars[i]
            Stars[i] = Stars[i+1]
            Stars[i+1] = tempS

            tempR = RatingInt[i]
            RatingInt[i] = RatingInt[i+1]
            RatingInt[i+1] = tempR

            tempDis = Discount[i]
            Discount[i] = Discount[i+1]
            Discount[i+1] = tempDis

            tempDescript = Description[i]
            Description[i] = Description[i+1]
            Description[i+1] = tempDescript
            isSorted = 0

   return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def oddEvenSortNewPriceAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
   n = len(NewPriceInt)
   isSorted = 0 # isSorted is used as flag

   while isSorted == 0:
      isSorted = 1
      temp = 0
      tempOld = 0
      tempNew = 0
      tempQ = 0
      tempS = 0
      tempR = 0
      tempDis = 0
      tempDescript = 0
      #For Odd Numbers
      for i in range(1, n-1, 2):
         if NewPriceInt[i] > NewPriceInt[i+1]:
            tempOld = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[i+1]
            OldpriceInt[i+1] = tempOld

            temp = MedicineName[i]
            MedicineName[i] = MedicineName[i+1]
            MedicineName[i+1] = temp
            
            tempNew = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[i+1]
            NewPriceInt[i+1] = tempNew

            tempQ = Quantity[i]
            Quantity[i] = Quantity[i+1]
            Quantity[i+1] = tempQ

            tempS = Stars[i]
            Stars[i] = Stars[i+1]
            Stars[i+1] = tempS

            tempR = RatingInt[i]
            RatingInt[i] = RatingInt[i+1]
            RatingInt[i+1] = tempR

            tempDis = Discount[i]
            Discount[i] = Discount[i+1]
            Discount[i+1] = tempDis

            tempDescript = Description[i]
            Description[i] = Description[i+1]
            Description[i+1] = tempDescript
            isSorted = 0
       
      #For Even Numbers      
      for i in range(0, n-1, 2):
         if NewPriceInt[i] > NewPriceInt[i+1]:
            tempOld = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[i+1]
            OldpriceInt[i+1] = tempOld

            temp = MedicineName[i]
            MedicineName[i] = MedicineName[i+1]
            MedicineName[i+1] = temp
            
            tempNew = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[i+1]
            NewPriceInt[i+1] = tempNew

            tempQ = Quantity[i]
            Quantity[i] = Quantity[i+1]
            Quantity[i+1] = tempQ

            tempS = Stars[i]
            Stars[i] = Stars[i+1]
            Stars[i+1] = tempS

            tempR = RatingInt[i]
            RatingInt[i] = RatingInt[i+1]
            RatingInt[i+1] = tempR

            tempDis = Discount[i]
            Discount[i] = Discount[i+1]
            Discount[i+1] = tempDis

            tempDescript = Description[i]
            Description[i] = Description[i+1]
            Description[i+1] = tempDescript
            isSorted = 0

   return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def oddEvenSortRatingAscending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
   n = len(RatingInt)
   isSorted = 0 # isSorted is used as flag

   while isSorted == 0:
      isSorted = 1
      temp = 0
      tempOld = 0
      tempNew = 0
      tempQ = 0
      tempS = 0
      tempR = 0
      tempDis = 0
      tempDescript = 0
      #For Odd Numbers
      for i in range(1, n-1, 2):
         if RatingInt[i] > RatingInt[i+1]:
            tempOld = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[i+1]
            OldpriceInt[i+1] = tempOld

            temp = MedicineName[i]
            MedicineName[i] = MedicineName[i+1]
            MedicineName[i+1] = temp
            
            tempNew = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[i+1]
            NewPriceInt[i+1] = tempNew

            tempQ = Quantity[i]
            Quantity[i] = Quantity[i+1]
            Quantity[i+1] = tempQ

            tempS = Stars[i]
            Stars[i] = Stars[i+1]
            Stars[i+1] = tempS

            tempR = RatingInt[i]
            RatingInt[i] = RatingInt[i+1]
            RatingInt[i+1] = tempR

            tempDis = Discount[i]
            Discount[i] = Discount[i+1]
            Discount[i+1] = tempDis

            tempDescript = Description[i]
            Description[i] = Description[i+1]
            Description[i+1] = tempDescript
            isSorted = 0
       
      #For Even Numbers      
      for i in range(0, n-1, 2):
         if RatingInt[i] > RatingInt[i+1]:
            tempOld = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[i+1]
            OldpriceInt[i+1] = tempOld

            temp = MedicineName[i]
            MedicineName[i] = MedicineName[i+1]
            MedicineName[i+1] = temp
            
            tempNew = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[i+1]
            NewPriceInt[i+1] = tempNew

            tempQ = Quantity[i]
            Quantity[i] = Quantity[i+1]
            Quantity[i+1] = tempQ

            tempS = Stars[i]
            Stars[i] = Stars[i+1]
            Stars[i+1] = tempS

            tempR = RatingInt[i]
            RatingInt[i] = RatingInt[i+1]
            RatingInt[i+1] = tempR

            tempDis = Discount[i]
            Discount[i] = Discount[i+1]
            Discount[i+1] = tempDis

            tempDescript = Description[i]
            Description[i] = Description[i+1]
            Description[i+1] = tempDescript
            isSorted = 0

   return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

#Odd/Even Sort Descending Function

def oddEvenSortOldpriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
   n = len(OldpriceInt)
   isSorted = 0 # isSorted is used as flag

   while isSorted == 0:
      isSorted = 1
      temp = 0
      tempOld = 0
      tempNew = 0
      tempQ = 0
      tempS = 0
      tempR = 0
      tempDis = 0
      tempDescript = 0
      #For Odd Numbers
      for i in range(1, n-1, 2):
         if OldpriceInt[i] > OldpriceInt[i+1]:
            tempOld = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[i+1]
            OldpriceInt[i+1] = tempOld

            temp = MedicineName[i]
            MedicineName[i] = MedicineName[i+1]
            MedicineName[i+1] = temp
            
            tempNew = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[i+1]
            NewPriceInt[i+1] = tempNew

            tempQ = Quantity[i]
            Quantity[i] = Quantity[i+1]
            Quantity[i+1] = tempQ

            tempS = Stars[i]
            Stars[i] = Stars[i+1]
            Stars[i+1] = tempS

            tempR = RatingInt[i]
            RatingInt[i] = RatingInt[i+1]
            RatingInt[i+1] = tempR

            tempDis = Discount[i]
            Discount[i] = Discount[i+1]
            Discount[i+1] = tempDis

            tempDescript = Description[i]
            Description[i] = Description[i+1]
            Description[i+1] = tempDescript
            isSorted = 0
       
      #For Even Numbers      
      for i in range(0, n-1, 2):
         if OldpriceInt[i] > OldpriceInt[i+1]:
            tempOld = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[i+1]
            OldpriceInt[i+1] = tempOld

            temp = MedicineName[i]
            MedicineName[i] = MedicineName[i+1]
            MedicineName[i+1] = temp
            
            tempNew = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[i+1]
            NewPriceInt[i+1] = tempNew

            tempQ = Quantity[i]
            Quantity[i] = Quantity[i+1]
            Quantity[i+1] = tempQ

            tempS = Stars[i]
            Stars[i] = Stars[i+1]
            Stars[i+1] = tempS

            tempR = RatingInt[i]
            RatingInt[i] = RatingInt[i+1]
            RatingInt[i+1] = tempR

            tempDis = Discount[i]
            Discount[i] = Discount[i+1]
            Discount[i+1] = tempDis

            tempDescript = Description[i]
            Description[i] = Description[i+1]
            Description[i+1] = tempDescript
            isSorted = 0
   
   MedicineName.reverse()
   OldpriceInt.reverse()
   NewPriceInt.reverse()
   Quantity.reverse()
   Stars.reverse()
   RatingInt.reverse()
   Discount.reverse()
   Description.reverse()
   return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def oddEvenSortNewPriceDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
   n = len(NewPriceInt)
   isSorted = 0 # isSorted is used as flag

   while isSorted == 0:
      isSorted = 1
      temp = 0
      tempOld = 0
      tempNew = 0
      tempQ = 0
      tempS = 0
      tempR = 0
      tempDis = 0
      tempDescript = 0
      #For Odd Numbers
      for i in range(1, n-1, 2):
         if NewPriceInt[i] > NewPriceInt[i+1]:
            tempOld = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[i+1]
            OldpriceInt[i+1] = tempOld

            temp = MedicineName[i]
            MedicineName[i] = MedicineName[i+1]
            MedicineName[i+1] = temp
            
            tempNew = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[i+1]
            NewPriceInt[i+1] = tempNew

            tempQ = Quantity[i]
            Quantity[i] = Quantity[i+1]
            Quantity[i+1] = tempQ

            tempS = Stars[i]
            Stars[i] = Stars[i+1]
            Stars[i+1] = tempS

            tempR = RatingInt[i]
            RatingInt[i] = RatingInt[i+1]
            RatingInt[i+1] = tempR

            tempDis = Discount[i]
            Discount[i] = Discount[i+1]
            Discount[i+1] = tempDis

            tempDescript = Description[i]
            Description[i] = Description[i+1]
            Description[i+1] = tempDescript
            isSorted = 0
       
      #For Even Numbers      
      for i in range(0, n-1, 2):
         if NewPriceInt[i] > NewPriceInt[i+1]:
            tempOld = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[i+1]
            OldpriceInt[i+1] = tempOld

            temp = MedicineName[i]
            MedicineName[i] = MedicineName[i+1]
            MedicineName[i+1] = temp
            
            tempNew = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[i+1]
            NewPriceInt[i+1] = tempNew

            tempQ = Quantity[i]
            Quantity[i] = Quantity[i+1]
            Quantity[i+1] = tempQ

            tempS = Stars[i]
            Stars[i] = Stars[i+1]
            Stars[i+1] = tempS

            tempR = RatingInt[i]
            RatingInt[i] = RatingInt[i+1]
            RatingInt[i+1] = tempR

            tempDis = Discount[i]
            Discount[i] = Discount[i+1]
            Discount[i+1] = tempDis

            tempDescript = Description[i]
            Description[i] = Description[i+1]
            Description[i+1] = tempDescript
            isSorted = 0
   MedicineName.reverse()
   OldpriceInt.reverse()
   NewPriceInt.reverse()
   Quantity.reverse()
   Stars.reverse()
   RatingInt.reverse()
   Discount.reverse()
   Description.reverse()
   return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

def oddEvenSortRatingDescending(MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description):
   n = len(RatingInt)
   isSorted = 0 # isSorted is used as flag

   while isSorted == 0:
      isSorted = 1
      temp = 0
      tempOld = 0
      tempNew = 0
      tempQ = 0
      tempS = 0
      tempR = 0
      tempDis = 0
      tempDescript = 0
      #For Odd Numbers
      for i in range(1, n-1, 2):
         if RatingInt[i] > RatingInt[i+1]:
            tempOld = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[i+1]
            OldpriceInt[i+1] = tempOld

            temp = MedicineName[i]
            MedicineName[i] = MedicineName[i+1]
            MedicineName[i+1] = temp
            
            tempNew = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[i+1]
            NewPriceInt[i+1] = tempNew

            tempQ = Quantity[i]
            Quantity[i] = Quantity[i+1]
            Quantity[i+1] = tempQ

            tempS = Stars[i]
            Stars[i] = Stars[i+1]
            Stars[i+1] = tempS

            tempR = RatingInt[i]
            RatingInt[i] = RatingInt[i+1]
            RatingInt[i+1] = tempR

            tempDis = Discount[i]
            Discount[i] = Discount[i+1]
            Discount[i+1] = tempDis

            tempDescript = Description[i]
            Description[i] = Description[i+1]
            Description[i+1] = tempDescript
            isSorted = 0
       
      #For Even Numbers      
      for i in range(0, n-1, 2):
         if RatingInt[i] > RatingInt[i+1]:
            tempOld = OldpriceInt[i]
            OldpriceInt[i] = OldpriceInt[i+1]
            OldpriceInt[i+1] = tempOld

            temp = MedicineName[i]
            MedicineName[i] = MedicineName[i+1]
            MedicineName[i+1] = temp
            
            tempNew = NewPriceInt[i]
            NewPriceInt[i] = NewPriceInt[i+1]
            NewPriceInt[i+1] = tempNew

            tempQ = Quantity[i]
            Quantity[i] = Quantity[i+1]
            Quantity[i+1] = tempQ

            tempS = Stars[i]
            Stars[i] = Stars[i+1]
            Stars[i+1] = tempS

            tempR = RatingInt[i]
            RatingInt[i] = RatingInt[i+1]
            RatingInt[i+1] = tempR

            tempDis = Discount[i]
            Discount[i] = Discount[i+1]
            Discount[i+1] = tempDis

            tempDescript = Description[i]
            Description[i] = Description[i+1]
            Description[i+1] = tempDescript
            isSorted = 0
   MedicineName.reverse()
   OldpriceInt.reverse()
   NewPriceInt.reverse()
   Quantity.reverse()
   Stars.reverse()
   RatingInt.reverse()
   Discount.reverse()
   Description.reverse()
   return MedicineName,OldpriceInt,NewPriceInt,Quantity,Stars,RatingInt,Discount,Description

