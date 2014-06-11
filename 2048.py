
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
def merge(line):
    i=0;l=line[0];s=[];x=len(line)
    while(i<x):
        if(i<x-1 and line[i]==line[i+1] and line[i]!=0):
            s.append(2*line[i])
            line[i+1]=0
            i=i+1
            continue
        elif(i==0 and line[i+1]==0 and line[i+2]==0):
            if(line[i]==line[i+3]):
                s.append(2*line[i])
                line[i+3]=0
                i=i+1
            elif(line[i+3]==0):
                s.append(line[i])
                i=i+1
            else:
                i=i+1
            
        elif(i<x-2 and line[i+1]==0  and line[i]==line[i+2]):
            s.append(2*line[i])
            line[i+2]=0;i=i+1
        elif(line[i]!=0):
            s.append(line[i]);i=i+1
        else:
            i=i+1
    while(len(s)<x):
        s.append(0)
    if(s[0]==0):
        while(i<4-1):
            q=s[i+1]
            s[i]=q
            s[i+1]=0
    return s

class TwentyFortyEight:
    def __init__(self, grid_height, grid_width):
        self.grid_height=grid_height
        self.grid_width=grid_width
        self.n=[[0 for x in range(self.grid_height)] for y in range(self.grid_width)]
        
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
        self.n=[[0 for x in range(self.grid_height)] for y in range(self.grid_width)]
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
                a=0
            if(x==-1):
                a=-1
            w=0    
            while(w<self.grid_width):
                l=[];q=0
                if(x==1):
                    a=0
                if(x==-1):
                    a=-1
                while(q<self.grid_height):
                    l.append(self.n[a][b])
                    a+=i;q+=1
                if(x==1):
                    a=0
                if(x==-1):
                    a=-1
                r=0;o=0
                z=merge(l)
                while(r<self.grid_height):
                    self.n[o][b]=z[a]
                    a+=i;r+=1;o=o+1
                b+=1;w+=1
        else:
            b=0
            if(y==1):
                a=0
            if(y==-1):
                a=-1
            w=0    
            while(w<self.grid_width):
                l=[];q=0
                if(y==1):
                    a=0
                if(y==-1):
                    a=-1
                while(q<self.grid_height):
                    l.append(self.n[b][a])
                    a+=i;q+=1
                if(y==1):
                    a=0
                if(y==-1):
                    a=-1
                r=0;o=0
                z=merge(l)
                while(r<self.grid_height):
                    self.n[b][a]=z[o]
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
        return self.n[row][col]    
def game_start():
    z=0
    t=TwentyFortyEight(4,4)
    while(1):
        if(z==0):
            print  "One second your move please ! or press i for instructions or key in 'e' to exit the game if you feel borred "
            print "here is your grids friend have fun"
            print1(t.new_tile())
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
        print1(x)
        z=1

def print1(n):
    
    for i in range(4):
        print n[:][i]

game_start()
