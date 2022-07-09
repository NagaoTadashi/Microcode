from onedivision_pooring import b
import math

class c(b):
    #入力の配置指定
    def input_placement(self):
        input_placement_min2_list=[]
        input_placement_min_list=[]
        input_placement_mid_list=[]
        input_placement_list=[]
        input_data=[]
        for i in self.data:
            input_data.extend([i[1]])
        #入力サイズがpbarrayサイズよりも大きい場合
        if self.info[0]>=int(self.info[10]/2):
            for i in input_data:
                output_placement=self.output_placement[input_data.index(i)]
                zero=0
                for j in output_placement:
                    if j==0:
                        zero=zero+1
                zero=zero/2
                n1=0
                n2=0
                for j in range(int(self.roop_number/self.info[3])):
                    for k in range(self.info[3]):
                        if zero==0:
                            for l in range(int((i[1]-i[0]+1)/2)):
                                for l1 in range(n1+n2+k+(i[2]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10])))
                                                ,n1+n2+k+(i[2]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10])))+int(self.info[10]/2)):
                                    input_placement_min2_list.append(l1)
                                input_placement_min_list.extend([input_placement_min2_list])
                                input_placement_min2_list=[]
                                n2=n2+self.info[0]*math.ceil(self.info[2]/self.info[10])
                        elif zero!=0:
                            if zero>0 and zero<(self.info[3]-1):
                                if k<(self.info[3]-zero):
                                    for l in range(int((i[1]-i[0]+1)/2)):
                                        for l1 in range(n1+n2+k+(i[2]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10])))
                                                        ,n1+n2+k+(i[2]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10])))+int(self.info[10]/2)):
                                            input_placement_min2_list.append(l1)
                                        input_placement_min_list.extend([input_placement_min2_list])
                                        input_placement_min2_list=[]
                                        n2=n2+self.info[0]*math.ceil(self.info[2]/self.info[10])
                                elif k>=(self.info[3]-zero):
                                    for l in range(int((i[1]-i[0]+1)/2)):
                                        for l1 in range(n1+n2+k+(i[2]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10])))
                                                        ,(n1+n2+(i[3]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10]))))+1):
                                            input_placement_min2_list.append(l1)
                                        while len(input_placement_min2_list)<(int(self.info[10]/2)):
                                            input_placement_min2_list.append(0)
                                        input_placement_min_list.extend([input_placement_min2_list])
                                        input_placement_min2_list=[]
                                        n2=n2+self.info[0]*math.ceil(self.info[2]/self.info[10])
                            elif zero>=(self.info[3]-1):
                                for l in range(int((i[1]-i[0]+1)/2)):
                                    for l1 in range(n1+n2+k+(i[2]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10])))
                                                    ,(n1+n2+(i[3]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10]))))+1):
                                        input_placement_min2_list.append(l1)
                                    while len(input_placement_min2_list)<(int(self.info[10]/2)):
                                        input_placement_min2_list.append(0)
                                    input_placement_min_list.extend([input_placement_min2_list])
                                    input_placement_min2_list=[]
                                    n2=n2+self.info[0]*math.ceil(self.info[2]/self.info[10])
                        input_placement_mid_list.extend([input_placement_min_list])
                        input_placement_min_list=[]
                        n2=0
                    n1=n1+self.info[0]
                input_placement_list.extend([input_placement_mid_list])
                input_placement_mid_list=[]
        #入力サイズがpbarrrayサイズよりも小さい場合
        elif self.info[0]<int(self.info[10]/2):
            for i in input_data:
                output_placement=self.output_placement[input_data.index(i)]
                one=0
                for j in output_placement:
                    if j==1:
                        one=one+1
                n1=0
                n2=0
                n3=int(one/self.info[7])
                n4=0
                for j in range(int(self.roop_number/self.info[3])):
                    for k in range(self.info[3]):
                        for l in range(2):
                            for l1 in range(int(n3/2)):
                                for m in range(n1+n2+n4+k+(i[2]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10])))
                                                ,n1+n2+n4+(i[3]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10])))+1):
                                    input_placement_min2_list.append(m)
                                for m in range(k):
                                    input_placement_min2_list.append(0)
                                if l1==int(n3/2)-1:
                                    for m in range(int(self.info[10]/2)-self.info[0]*int(n3/2)):
                                        input_placement_min2_list.append(0)
                                input_placement_min_list.extend([input_placement_min2_list])
                                input_placement_min2_list=[]
                                n4=n4+2*(self.info[0]*math.ceil(self.info[2]/self.info[10]))
                            n4=0
                            n2=n2+self.info[0]*math.ceil(self.info[2]/self.info[10])
                        input_placement_mid_list.extend([input_placement_min_list])
                        input_placement_min_list=[]
                        n2=0
                    n1=n1+self.info[0]
                input_placement_list.extend([input_placement_mid_list])
                input_placement_mid_list=[]
        return input_placement_list

    #フィルタの配置指定  
    def filter_placement(self):
        filter_placement_min_list=[]
        filter_placement_mid_list=[]
        filter_placement_list=[]
        filter_data=[]
        for i in self.data:
            if (i[2][5]-i[2][4]+1)<self.info[10]:
                i[2][5]=i[2][4]+(self.info[10]-1)
                filter_data.extend([i[2]])
            else:    
                filter_data.extend([i[2]])
        for i in filter_data:
            q=math.floor((filter_data[filter_data.index(i)][5]+1)/self.info[10])
            start1=int(self.info[3]*self.info[4]*self.info[10]*q*(filter_data[filter_data.index(i)][6]/self.info[10]))
            for j in range(self.info[3]*self.info[4]):
                for k in range(q):
                    for l in range(start1,start1+self.info[10]):
                        filter_placement_min_list.append(l)
                    filter_placement_mid_list.extend([filter_placement_min_list])
                    filter_placement_min_list=[]
                    start1=start1+self.info[10]
            filter_placement_list.extend([filter_placement_mid_list])
            filter_placement_mid_list=[]
        return filter_placement_list

    #出力のアドレス
    def output_adress1(self):
        output_data=[]
        output_adress1_min_list=[]
        output_adress1_list=[]
        for i in self.data:
            x1=int(i[3][0]/2)
            x2=x1+int((i[3][1]-i[3][0]+1)/2)-1
            x3=int(i[3][2]/2)
            x4=x3+int((i[3][3]-i[3][2]+1)/2)-1
            i[3][0]=x1
            i[3][1]=x2
            i[3][2]=x3
            i[3][3]=x4
            output_data.extend([i[3]])
        if self.info[9]>self.info[10]:
            for i in output_data:
                for j in range(i[1]-i[0]+1):
                    for k in range(i[3]-i[2]+1):
                        for l in range(4):
                            output_adress1_min_list.append(int((int(self.info[8]/2)*(i[4]/self.info[10])+int(self.info[8]/2)*(self.info[9]/self.info[10])*(i[0]+j)+i[2])+k))
                output_adress1_list.extend([output_adress1_min_list])
                output_adress1_min_list=[]
        elif self.info[9]<=self.info[10]:
            for i in output_data:
                for j in range(i[1]-i[0]+1):
                    for k in range(i[3]-i[2]+1):
                        for l in range(4):
                            output_adress1_min_list.append(int((int(self.info[8]/2)*(i[4]/self.info[10])+int(self.info[8]/2)*(self.info[10]/self.info[10])*(i[0]+j)+i[2])+k))
                output_adress1_list.extend([output_adress1_min_list])
                output_adress1_min_list=[]
        return output_adress1_list
    
    def output_adress2(self):
        output_adress2_min_list=[]
        output_adress2_list=[]
        for i in self.output_adress1():
            for j in i:
                x=j-i[0]
                output_adress2_min_list.append(x)
            output_adress2_list.extend([output_adress2_min_list])
            output_adress2_min_list=[]
        return output_adress2_list

    #pbarrayのアドレス
    def pbarray_adress(self):
        pbarray_adress_min_list=[]
        pbarray_adress_list=[]
        for i in self.output_placement:
            for k,j in enumerate(i[0:int(self.info[10]/2)]):
                if j==1:
                    pbarray_adress_min_list.append(k) 
                    if k%2!=0:
                        pbarray_adress_min_list.append(k-1+int(self.info[10]/2))
                        pbarray_adress_min_list.append(k+int(self.info[10]/2))
            pbarray_adress_list.extend([pbarray_adress_min_list])
            pbarray_adress_min_list=[]
        return pbarray_adress_list   

class d:
    def __init__(self):
        self.input_placement=p2.input_placement()
        self.filter_placement=p2.filter_placement() 
        self.output_adress1=p2.output_adress1()
        self.output_adress2=p2.output_adress2()
        self.pbarray_adress=p2.pbarray_adress()
        self.pbarray_asize=p2.info[10]
        self.filter_size=p2.info[4]

p2=c()
#print(p2.output_adress2())
#print(p2.pbarray_adress())