

import random as r
   

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
def merge(l):
    x=len(l)
    l=remove(l)
    l=add(l)
    l=remove(l)
    while(len(l)<x):
        l.append(0)
    return l
def remove(l):
    s=[];x=len(l)
    for i in range(x):
        if(l[i]==0):
            continue
        else:
            s.append(l[i])
    return s
def add(l):
    x=len(l);s=[];i=0;l.append(0)
    while(i<x):
        if(l[i]==l[i+1]):
            
            s.append(2*l[i])
            l[i+1]=0
            i=i+1
            
        else:
            s.append(l[i])
            i=i+1
            
    return s

class TwentyFortyEight:
    def __init__(self, grid_height, grid_width):
        self.grid_height=grid_height
        self.grid_width=grid_width
        self.n=[[0 for x in range(self.grid_width)] for y in range(self.grid_height)]
        
        UP = 1
        DOWN = 2
        LEFT = 3
        RIGHT = 4
        OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
        pass
    
    def reset(self):
        self.n=[[0 for x in range(self.grid_width)] for y in range(self.grid_height)]
        pass
    


    def get_grid_height(self):
        return self.grid_height
    
    def get_grid_width(self):
        return self.grid_width
                            
    def move(self, d):
        x=OFFSETS[d][0];y=OFFSETS[d][1]
        
        if(x ==1 or y==1):
            i=1
        if(x ==-1 or y==-1):
            i=-1
        if(y==0 and abs(x)==1):
            b=0
            if(x==1):
                t=0
            if(x==-1):
                t=-1
            w=0    
            while(w<self.grid_width):
                l=[];q=0
                a=t
                while(q<self.grid_height):
                    l.append(self.n[a][b])
                    a+=i;q+=1
                a=t
                r=0;o=0
                z=merge(l)
                
                while(r<self.grid_height):
                    self.n[o][b]=z[a]
                    a+=i;r+=1;o=o+1
                b+=1;w+=1
        else:
            b=0
            if(y==1):
                t=0
            if(y==-1):
                t=-1
            w=0    
            while(w<self.grid_height):
                l=[];q=0
                a=t
                while(q<self.grid_width):
                    l.append(self.n[b][a])
                    a+=i;q+=1
                a=t
                r=0;o=0
                z=merge(l)
                while(r<self.grid_width):
                    self.n[b][o]=z[a]
                    a+=i;r+=1;o=o+1
                b+=1;w+=1
        self.n=self.new_tile()
        return self.n
        pass
                
    def new_tile(self):
        sum=0
        l=[2,2,2,2,2,2,2,2,2,4]
        for i in range(self.grid_height):
            for j in range(self.grid_width):
                if(self.n[i][j]!=0):
                    sum+=1
        if(sum==self.grid_height**2):
            return self.n
        else:
            while(1):
                x=r.randint(0,self.grid_height-1)
                y=r.randint(0,self.grid_width-1)
                if(self.n[x][y]==0):
                    self.n[x][y]=r.choice(l)
                    break
            return self.n
    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        # replace with your code
        return self.n[row][col]        


    def get_tile(self, row, col):
        return self.n[row][col]    
def game_start():
    z=0;
    h=raw_input("please enter the grid height  ------->")
    w=raw_input("please enter the grid width  ------->")
    t=TwentyFortyEight(int(h),int(w))
    while(1):
        if(z==0):
            print  "One second press i for instructions or key in 'e' to exit the game if you feel borred "
            print "UP:1    DOWN:2    LEFT:3    RIGHT:4"
            q=raw_input("Set your target friend ----->")
            print "here is your grids friend have fun"
            x=t.new_tile()
            print1(x,int(h))
        if(game_check(x,int(q),int(h),int(w))==True):
            
            print "Great my friend you did it "
            return None
        m=raw_input("Your input please   -------->")
        if(m=='i'):
            print "UP:1    DOWN:2    LEFT:3    RIGHT:4"
            z=1
            continue
        elif(m=='e'):
            print "good bye my friend see you around soon"
            return None
        x=t.move(int(m))
        print "here is your new grid"
        
        print1(x,int(h))
        z=1
def print1(n,w):
    
    for i in range(w):
        print n[:][i]
def game_check(x,m,h,w):
    for i in range(h):
        for j in range(w):
            if(x[i][j]==m):
                return True
    return False
game_start()
