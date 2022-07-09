import math

class a:
    def __init__(self,x1,y1,z1,x2,y2,z2,n2,x3,y3,z3,pb_array):
        #入力
        self.ax=x1
        self.ay=y1
        self.az=z1
        #フィルタ
        self.bx=x2
        self.by=y2
        self.bz=z2
        self.bn=n2
        #出力 
        self.cx=x3
        self.cy=y3
        self.cz=z3
        #self.cx=self.ax-(self.bx-1)
        #self.cy=self.ay-(self.by-1)
        #self.cz=self.bn
        #pb array
        self.pb_array=pb_array   
    
    #出力の配置
    def output_placement(self):
        output_placement_list=[]
        output_placement_min_list=[]
        if self.cx>=self.pb_array:
            q=self.cx//self.pb_array
            mod=self.cx%self.pb_array
            for i in range(self.cy*(math.ceil(self.cz/self.pb_array))):
                for j in range(q):
                    for k in range(self.pb_array):
                        output_placement_min_list.append(1)
                    output_placement_list.extend([output_placement_min_list])
                    output_placement_min_list=[]
                if mod!=0:
                    for i in range(mod):
                        output_placement_min_list.append(1)
                    for i in range(self.pb_array-mod):
                        output_placement_min_list.append(0)
                    output_placement_list.extend([output_placement_min_list])
                    output_placement_min_list=[]
            return output_placement_list
        elif self.cx<self.pb_array:
            pb_size=self.pb_array
            cnt1=0
            while self.cx<=pb_size:
                for i in range(self.cx):
                    output_placement_min_list.append(1)
                pb_size=pb_size-self.cx
                cnt1+=1
                if pb_size<=(self.bx-1):
                    for i in range(pb_size):
                        output_placement_min_list.append(0)
                    pb_size=0
                    break
                elif pb_size>(self.bx-1):
                    for i in range(self.bx-1):
                        output_placement_min_list.append(0)
                    pb_size=pb_size-(self.bx-1)
            if pb_size>0:
                for i in range(pb_size):
                    output_placement_min_list.append(0)
            for i in range(math.ceil(self.cz/self.pb_array)):
                for j in range(math.floor(self.cy/cnt1)):
                    output_placement_list.extend([output_placement_min_list])
                if self.cy-(cnt1*math.floor(self.cy/cnt1))>0:
                    output_placement_min2_list=[]
                    pb_size=self.pb_array
                    cnt2=0
                    for j in range(self.cy-(cnt1*math.floor(self.cy/cnt1))):
                        for k in range(self.cx):
                            output_placement_min2_list.append(1)
                        cnt2+=1
                        for k in range(self.bx-1):
                            output_placement_min2_list.append(0)
                        pb_size=pb_size-(self.cx+(self.bx-1))
                    if pb_size>0:
                        for j in range(pb_size):
                            output_placement_min2_list.append(0)
                    output_placement_list.extend([output_placement_min2_list])
            return output_placement_list

    #分轄数の計算
    def division_number(self):
        return len(self.output_placement())
       

    #ループ数の計算
    def roop_number(self):
        return (self.bx*self.by)*(math.ceil(self.bz/self.pb_array))
    
    #1分割分における出力データ
    def output_data(self):
        output_data_list=[]
        output_data_min_list=[]
        n=0 
        if self.cx>=self.pb_array:
            mod_x=self.cx
            mod_z=self.cz
            for i in range(0,self.cz,self.pb_array):
                for j in range(self.cy):
                    for k in range(0,self.cx,self.pb_array):
                        if mod_z>=self.pb_array:
                            if mod_x>=self.pb_array:
                                output_data_min_list=[j,j,k,(k+self.pb_array)-1,i,(i+self.pb_array)-1]
                                output_data_list.extend([output_data_min_list])
                                output_data_min_list=[]
                                n=n+1
                                mod_x=mod_x-self.pb_array
                                if mod_x==0:
                                    break
                            elif mod_x>0 and mod_x<self.pb_array:
                                output_data_min_list=[j,j,k,(k+mod_x)-1,i,(i+self.pb_array)-1]
                                output_data_list.extend([output_data_min_list])
                                output_data_min_list=[]
                                n=n+1
                        elif mod_z>0 and mod_z<self.pb_array:
                            if mod_x>=self.pb_array:
                                output_data_min_list=[j,j,k,(k+self.pb_array)-1,i,(i+mod_z)-1]
                                output_data_list.extend([output_data_min_list])
                                output_data_min_list=[]
                                n=n+1
                                mod_x=mod_x-self.pb_array
                                if mod_x==0:
                                    break
                            elif mod_x>0 and mod_x<self.pb_array:
                                output_data_min_list=[j,j,k,(k+mod_x)-1,i,(i+mod_z)-1]
                                output_data_list.extend([output_data_min_list])
                                output_data_min_list=[]
                                n=n+1
                    mod_x=self.cx
                mod_z=mod_z-self.pb_array
                if mod_z==0:
                    break
            return output_data_list
        
        elif self.cx<self.pb_array:
            output_placement=self.output_placement()
            output_placement=output_placement[0]
            cnt=0
            for i in output_placement:
                if i==1:
                    cnt=cnt+1
            q=int(cnt/self.cx)
            mod_y=self.cy
            mod_z=self.cz
            for i in range(0,self.cz,self.pb_array):
                for j in range(0,self.cy,q):
                    if mod_z>=self.pb_array:
                        if mod_y>=q:
                            output_data_min_list=[j,(j+q)-1,0,self.cx-1,i,(i+self.pb_array)-1]
                            output_data_list.append(output_data_min_list)
                            output_data_min_list=[]
                            n=n+1
                            mod_y=mod_y-q
                            if mod_y==0:
                                break
                        elif mod_y>0 and mod_y<q:
                            output_data_min_list=[j,(j+mod_y)-1,0,self.cx-1,i,(i+self.pb_array)-1]
                            output_data_list.append(output_data_min_list)
                            output_data_min_list=[]
                            n=n+1
                    elif mod_z>0 and mod_z<self.pb_array:
                        if mod_y>=q:
                            output_data_min_list=[j,(j+q)-1,0,self.cx-1,i,(i+mod_z)-1]
                            output_data_list.append(output_data_min_list)
                            output_data_min_list=[]
                            n=n+1
                            mod_y=mod_y-q
                        elif mod_y>0 and mod_y<q:
                            output_data_min_list=[j,(j+mod_y)-1,0,self.cx-1,i,(i+mod_z)-1]
                            output_data_list.append(output_data_min_list)
                            output_data_min_list=[]
                            n=n+1
                mod_y=self.cy
                mod_z=mod_z-self.pb_array
                if mod_z==0:
                    break
            return output_data_list
    
    #１分割分におけるフィルタデータ
    def filter_data(self):
        filter_data_min_list=[]
        filter_data_list=[]
        output_data=self.output_data()
        for i in output_data:
            filter_data_min_list=[0,self.bx-1,0,self.by-1,0,self.bz-1,i[4],i[5]]
            filter_data_list.extend([filter_data_min_list])
            filter_data_min_list=[]
        return filter_data_list
    
    #1分割分における入力データ
    def input_data(self):
        input_data_min_list=[]
        input_data_list=[]
        output_data=self.output_data()
        for i in output_data:
            input_data_min_list=[i[0],i[1]+(self.bx-1),i[2],i[3]+(self.bx-1),0,self.az-1]
            input_data_list.extend([input_data_min_list])
            input_data_min_list=[]
        return input_data_list
    
    #1分割分における全データ
    def data(self):
        division_number=self.division_number()
        input_data=self.input_data()
        filter_data=self.filter_data()        
        output_data=self.output_data()
        data_min_list=[]
        data_list=[]
        for i in range(division_number):
            data_min_list=[i,input_data[i],filter_data[i],output_data[i]]
            data_list.extend([data_min_list])
            data_min_list=[]
        return data_list

#分割数、ループ数、出力の配置、1分割分のデータ（入力、フィルタ、出力）
class b:
    def __init__(self):
        self.info=[p1.ax,p1.ay,p1.az,p1.bx,p1.by,p1.bz,p1.bn,p1.cx,p1.cy,p1.cz,p1.pb_array]
        self.division_number=p1.division_number()
        self.roop_number=p1.roop_number()
        self.output_placement=p1.output_placement()
        self.data=p1.data()  

#p1=a(32,32,3,1,1,3,32,32,32,32,32)
p1=a(6,6,64,3,3,64,16,4,4,16,32)



    
        
       









