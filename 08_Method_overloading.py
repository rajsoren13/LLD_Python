class calculation:
   #Make c optional with a default value:
    #def add(self, a:int, b:int,c:int=0):
        #return a+b+c

    #accept any number of arguments:
     def add(self, *args: int):
        return sum(args)

cal=calculation()
print(cal.add(1,6))
print(cal.add(5,6,7))

