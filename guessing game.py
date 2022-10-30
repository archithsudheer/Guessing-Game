class Game:
    def __init__(self,mini,maxi):
        self.mn=mini
        self.mx=maxi
    def run(self):
        x=random.randint(self.mn,self.mx)
        c=0
        while True:
            c+=1
            try:
                k=int(input("enter your guess"))
            except:
                print("enter a number")
            
            if k==x:
                print(f"correct in {c}tries")
                return
            #elif k not in string.ascii_letters:
                
                
            elif k>x:
                print("try a smaller number")
            else:
                print("try a bigger number")
