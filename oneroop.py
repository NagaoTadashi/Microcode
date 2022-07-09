from onedivision import b
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
        if self.info[0]>=self.info[10]:
            for i in input_data:
                output_placement=self.output_placement[input_data.index(i)]
                zero=0
                for j in output_placement:
                    if j==0:
                        zero=zero+1
                n1=0
                for j in range(int(self.roop_number/self.info[3])):
                    for k in range(self.info[3]):
                        if zero==0:
                            for l in range(n1+k+(i[2]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10])))
                                            ,n1+k+(i[2]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10])))+self.info[10]):
                                input_placement_min_list.append(l)
                        elif zero!=0:
                            if zero>0 and zero<(self.info[3]-1):
                                if k<(self.info[3]-zero):
                                     for l in range(n1+k+(i[2]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10])))
                                                    ,n1+k+(i[2]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10])))+self.info[10]):
                                        input_placement_min_list.append(l)
                                elif k>=(self.info[3]-zero):
                                    for l in range(n1+k+(i[2]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10])))
                                                    ,(n1+(i[3]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10]))))+1):
                                        input_placement_min_list.append(l)
                                    while len(input_placement_min_list)<32:
                                        input_placement_min_list.append(0)
                            elif zero>=(self.info[3]-1):
                                for l in range(n1+k+(i[2]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10])))
                                                ,(n1+(i[3]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10]))))+1):
                                    input_placement_min_list.append(l)
                                while len(input_placement_min_list)<32:
                                    input_placement_min_list.append(0)
                        input_placement_mid_list.extend([[input_placement_min_list]])
                        input_placement_min_list=[]
                    n1=n1+self.info[0]
                input_placement_list.extend([input_placement_mid_list])
                input_placement_mid_list=[]
        #入力サイズがpbarrrayサイズよりも小さい場合
        elif self.info[0]<self.info[10]:
            for i in input_data:
                output_placement=self.output_placement[input_data.index(i)]
                one=0
                for j in output_placement:
                    if j==1:
                        one=one+1
                n1=0
                n2=0
                n3=int(one/self.info[7])
                for j in range(int(self.roop_number/self.info[3])):
                    for k in range(self.info[3]):
                        for l1 in range(n3):
                            for m in range(n1+n2+k+(i[2]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10])))
                                            ,n1+n2+(i[3]+i[0]*self.info[0]*(math.ceil(self.info[2]/self.info[10])))+1):
                                input_placement_min2_list.append(m)
                            for m in range(k):
                                input_placement_min2_list.append(0)
                            if l1==n3-1:
                                for m in range(int(self.info[10])-self.info[0]*n3):
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
            output_data.extend([i[3]])
        if self.info[9]>=self.info[10]:
            for i in output_data:
                for j in range(i[1]-i[0]+1):
                    for k in range(i[3]-i[2]+1):
                        output_adress1_min_list.append(int((self.info[8]*(i[4]/self.info[10])+self.info[8]*(self.info[9]/self.info[10])*(i[0]+j)+i[2])+k))
                output_adress1_list.extend([output_adress1_min_list])
                output_adress1_min_list=[]
        elif self.info[9]<self.info[10]:
            for i in output_data:
                for j in range(i[1]-i[0]+1):
                    for k in range(i[3]-i[2]+1):
                        output_adress1_min_list.append(int((self.info[8]*(i[4]/self.info[10])+self.info[8]*(self.info[10]/self.info[10])*(i[0]+j)+i[2])+k))
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
            for k,j in enumerate(i):
                if j==1:
                    pbarray_adress_min_list.append(k)
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