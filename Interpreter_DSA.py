import sys
#from pythonds.basic.stack import Stack

dic={}
print (dic)
class program(object):
    
    def __init__(self,lines):
        self.lines= lines
    
        
        #print(self.lines)
        #print("OOO")
        
    def eval(self):
        i=0
        
        while (i<len(self.lines)):
            cif=0
            elsflag=0
            cfi=0
            cwhile=0
            cend=0
            #print(self.lines[i])
            if(self.lines[i].find('=')!= -1 and self.lines[i].find("if")==-1 and self.lines[i].find("!")==-1 and self.lines[i].find(">")==-1  and self.lines[i].find("<")==-1):
                a1=assignment(self.lines[i],self.lines[i].find('='))
                #print("hmm" +self.lines[i]+str(self.lines[i].find('=') ))
                a1.eval()
            elif(self.lines[i].find('print')!=-1):
                a1 = display(self.lines[i])
                a1.eval()
            elif (self.lines[i].find("if")!=-1):
               # print("value" + str(i))
                cif=1
                for j in range(i+1,len(self.lines)):
                    
                    if(self.lines[j].find("if")!=-1):
                        cif+=1
                    elif (self.lines[j]==("fi")):
                        cfi+=1
                    if(cif==cfi):
                        #print("sefd" + str(j) + self.lines[j])
                        break
                for k in range(j,i,-1):
                    if(self.lines[k]=="else"):
                        elsflag=1
                        #print("sefd" + str(k) + self.lines[k+1])
                        break
                if(elsflag==0):
                    k=j
                self.con = condition()
                #print(self.lines[i])
                #print("HERE")
                
                if(self.con.eval(self.lines[i][2:])):
                    #print("TRUEEEEEEEEEE")
                    #print(self.lines[i][2:])
                    #print(self.lines[i+2:k])
                    p=program(self.lines[i+2:k])
                    p.eval()
                else:
                    p=program(self.lines[k+1:j])
                    p.eval()
                
                i=j+1
                continue
            elif (self.lines[i].find('while')!=-1):
                cwhile=1
                #print(self.lines[i:])
                #print("i==" + str(i))
                #print(self.lines)
                for j in range (i+1,len(self.lines)):
                    if(self.lines[j].find("while")!=-1):
                        cwhile+=1
                    elif (self.lines[j]==("end")):
                        cend+=1
                    if(cwhile==cend):
                        #print("sefwhiled" + str(j) + self.lines[j])
                        break
                self.con = condition()
                #print((self.lines[i][5:]))
                if(self.con.eval(self.lines[i][5:len(self.lines[i])-2])):
                    p=program(self.lines[i+1:j])
                    p.eval()
                    i=i
                    continue
                else:
                    i = j+1
                    continue
            else:
                raise Exception ("Syntax Error on line" + " " + str(i+1))
            i+=1
                    
                        
                    

class assignment(object):
    
    def __init__(self,word,pos):
        self.leftexp = word[:pos]  
        self.rightexp=word[pos+1:]  
    def eval(self):
        self.exp=expression()
        dic[self.leftexp]=self.exp.eval(self.rightexp)
        #print(dic[self.leftexp] + "dtdr")

class display(object):
    def __init__(self,word):
        self.word = word
            
        
    def eval(self):
        
        if self.word[6]=='"':
           
            
            for i in range(7,len(self.word)):
                if(self.word[i]=='"'):
                    print(self.word[7:i],end=' ')
                    break
        elif self.word[7]=="n":
            print("\n")
        else:
            x=self.word[6:]
            if(x.isalpha()):
                print(dic[x],end=' ')
            else:
                x2=expression()
                ans=x2.eval(x)
                print(ans)
            
            
class condition(object):
    def eval(self,part):
        #print(part)
        for r in range (0,len(part)):
            if (part[r]==">" or part[r]=="<" or (part[r]=="!" and part[r+1]=="=") or (part[r]==">" and part[r+1]=="=") or (part[r]=="=" and part[r]=="=") or (part[r]=="<" and part[r]=="=") ):
                 #print(r)
                 x = expression()
                 #print("part")
                 #print(part[0:r])
                 x1 =( x.eval(part[0:r]))
                 #print(str(x1)+ "value X1")
                 x1=float(x1)
                 y=expression()
                 #print(part[r+1:len(part)])
                 if((part[r]=="!" and part[r+1]=="=") or (part[r]=="=" and part[r]=="=") or(part[r]==">" and part[r]=="=") or (part[r]=="<" and part[r]=="=")  ):
                     #print(part[r+2:len(part)])
                     y1= (y.eval(part[r+2:len(part)]))
                 else:
                     y1= (y.eval(part[r+1:len(part)]))
                 #print(str(y1)+ "value Y1")
                 y1=float(y1)
                 #print("yehyaha")
                 #print(y1)
                 break
        o=operator()
        if (part[r]=="=" and part[r+1]=="="):
            oper = "=="
        elif(part[r]=="!" and part[r+1]=="="):
            oper="!="
        elif(part[r]==">" and part[r+1]=="="):
            oper=">="
        elif(part[r]=="<" and part[r+1]=="="):
            oper="<="
        else:
            oper =part[r]
        if(o.eval(oper,x1,y1)):
            return True
        else:
            #print("yupp")
            return False
                
                       
        
class expression(object):

     
    def eval(self,ex):            
        #print(ex+"oo")
        check=0
        flag=0
        count=0
        
        for i in range(0,len(ex)):
            check=0
            flag=0
            l=[]
            r=[]
            if(ex[i] == '+' or ex[i] == '*' or ex[i]=='-'):
                l=ex[:i]
                r=ex[i+1:]
                c1=0
                c2=0
                for j in l:
                    if(j=="("):
                        c1+=1
                    if(j==")"):
                        c2+=1
                if c1==c2:
                    check+=1
                c1=0
                c2=0
                for j in r:
                    if(j=="("):
                        c1+=1
                    if(j==")"):
                        c2+=1
                if c1==c2:
                    check+=1
                
                if check==2:
                    flag=1
                    break
        
            
        if (flag==0): 
            
            #print(ex[:])
            if(ex[:].isalpha()): 
                return dic[ex[:]]
            elif(ex[:].isnumeric()):
                 
                return str(ex[:])
                    
        if ex[i-1]==")":
            #print("hi"+ex[:i]+str( i))
            for j in range(i-1,-1,-1):
                if ex[j] == "(":
                    break
           # print(ex[j:i] + "ooolALALA")
            exp1=expression()
            left =exp1.eval(ex[j+1:i-1])
        else:
            left = ex[0:i] 
        if ex[i+1]=='(':
            for j in range(i+2,len(ex)):
                if ex[j] == ')':
                    break
            exp1=expression()
            
            right=exp1.eval(ex[i+2:j])
        else:
            right = ex[i+1:]

        #print("ghjgh"+" "+str((right)))
        #print("vbvbn"+str(left))

        if(left.isalpha()):
            #print("yes"+ dic[left])
            left =float( dic[left])
        else:
           # print("hii"+str(left))
            left = float(left)
        if(right.isalpha()):
            
            right = float(dic[right])
        else:
            #print("hiii"+str(right))
            right = float(right)

        if ex[i]=="+":
           # print("hiiii")
            return str(left + right)
        elif ex[i]=="*":
            return str(left * right)
        elif ex[i]=="-":
            return str(left - right)
class variable(object):
    def __init__(self,var_name,var_val):
        self.var_name = var_name
        self.var_val= var_val
    def eval(self):
        return self.var_val
class integer (object):
    def __init__(self,val):
        self.val= val
    def eval(self):
        return self.val

        

class operator(object):
    def eval(self,op, x ,y):
        if(op=='>'):
            if(x>y):
                return True
            else:
                return False
        if(op=='<'):
            if(x<y):
                return True
            else:
                return False
        if(op=="=="):
            if(x==y):
                return True
            else:
                return False
        if(op=="!="):
            if(x!=y):
                return True
            else:
                return False
        if(op==">="):
            
            if(x>=y):
                return True
            else:
                return False
        if(op=="<="):
            
            if(x<=y):
                return True
            else:
                return False
            
        
            
  
filename="dummy.txt"            
lines = [line.rstrip('\n') for line in open(filename)]
print(lines )

for i in range(0,len(lines)):
    
    if ';' in lines[i]:
        continue
    else:
        if ('while' in lines[i]) or ('if' in lines[i]):
            continue
        else:
            raise Exception ("Syntax Error on line" + " " + str(i))
    

lines = ([s.rstrip(';') for s in lines])
lines = ([s.rstrip(':') for s in lines])
for i in range(0,len(lines)):
    if "print" in lines[i]:
        continue
    else:
        lines[i]=lines[i].replace(' ','')


#lines= ([s.replace(' ','') for s in lines])


            

print(lines)
try:
    a=program(lines)
    a.eval()
except Exception as e:
    print(str(e))
    print("Syntax error!!")
    
#print(dic)







'''final=[]
for word in lines:
    temp=[]
   if(word[0]=='i' and word[1]=='f'):
       temp.append(word)
       for end in lines(word+1,len(lines)):
           if(end[0]=='f' and end[1]=='i')
               
           
           
       
     
   else:
       final.append(word)'''
       
        

#def assignment():


    
    
    
#def condition():
    