#from oneroop import d
from oneroop_pooring import d

class e(d):
    #入力、重みを転送するタイミング
    def timing(self):
        #x=xsend,w=wsend,c=change(切り替え),s=slide(ずらす),r=return(出力をSRAMに戻す)
        all_list=[]
        onedivision_list=[]
        oneroop_list=[]
        x=0
        for i in range(len(self.input_placement)):
            for j in range(0,len(self.input_placement[i]),self.filter_size):
                if j==0:
                    if len((self.input_placement[i][j]))>1:
                        for l in range(len(self.input_placement[i][j])):
                            for k,ax in enumerate(self.input_placement[i][j][l]):
                                if k>0 and ax==0:
                                    pass
                                else:
                                    oneroop_list.extend([["x",ax,k]])
                            oneroop_list=[oneroop_list[0][0],oneroop_list[0][1],x,len(oneroop_list)]
                            onedivision_list.extend([oneroop_list])
                            oneroop_list=[]
                            x=x+len(self.input_placement[i][j][l])
                        x=0
                    elif len((self.input_placement[i][j]))==1:
                        for k,ax in enumerate(self.input_placement[i][j][0]):
                            if k>0 and ax==0:
                                pass
                            else:
                                oneroop_list.extend([["x",ax,k]])
                        oneroop_list=[oneroop_list[0][0],oneroop_list[0][1],oneroop_list[0][2],len(oneroop_list)]
                        onedivision_list.extend([oneroop_list])
                        oneroop_list=[]
                if j+self.filter_size==len(self.input_placement[i]):
                    for aw in self.filter_placement[i][j]:
                        oneroop_list.extend([["w",aw]])
                    oneroop_list=[oneroop_list[0][0],oneroop_list[0][1],len(oneroop_list)]
                    onedivision_list.append(["c"])
                    onedivision_list.extend([oneroop_list])        
                    oneroop_list=[]               
                else:
                    if len(self.input_placement[i][j])>1:
                        cnt1=0
                        cnt2=0
                        cnt3=0
                        for l in range(len(self.input_placement[i][j+self.filter_size])):
                            for ax in self.input_placement[i][j+self.filter_size][l]:
                                if  ax!=0:
                                    oneroop_list.extend([[["x",ax,cnt3],["w",self.filter_placement[i][j][cnt3]]]])   
                                    cnt1=cnt1+1
                                    cnt3=cnt3+1
                                elif ax==0:
                                    oneroop_list.extend([["w",self.filter_placement[i][j][cnt3]]])
                                    cnt2=cnt2+1
                                    cnt3=cnt3+1
                            if cnt2==0:
                                oneroop_list=[["xw",oneroop_list[0][0][1],oneroop_list[0][0][2],oneroop_list[0][1][1],cnt1]]
                            elif cnt2>0:
                                oneroop_list=[["xw",oneroop_list[0][0][1],oneroop_list[0][0][2],oneroop_list[0][1][1],cnt1],[oneroop_list[cnt1][0],oneroop_list[cnt1][1],cnt2]]
                            if l==0:
                                onedivision_list.append(["c"])
                            onedivision_list.extend(oneroop_list)
                            oneroop_list=[]
                            cnt1=0
                            cnt2=0  
                    elif len(self.input_placement[i][j])==1:
                        cnt1=0
                        cnt2=0
                        for k,(ax,aw) in enumerate(zip(self.input_placement[i][j+self.filter_size][0],self.filter_placement[i][j])):
                            if  ax!=0:
                                oneroop_list.extend([[["x",ax,k],["w",aw]]])   
                                cnt1=cnt1+1
                            elif ax==0:
                                oneroop_list.extend([["w",aw]])
                                cnt2=cnt2+1
                        if cnt2==0:
                            oneroop_list=[["xw",oneroop_list[0][0][1],oneroop_list[0][0][2],oneroop_list[0][1][1],cnt1]]
                        elif cnt2>0:
                            oneroop_list=[["xw",oneroop_list[0][0][1],oneroop_list[0][0][2],oneroop_list[0][1][1],cnt1],[oneroop_list[cnt1][0],oneroop_list[cnt1][1],cnt2]]
                        onedivision_list.append(["c"])
                        onedivision_list.extend(oneroop_list)
                        oneroop_list=[]    
                for k in range(self.filter_size-1):
                    onedivision_list.append(["s"])
                    cnt=0
                    n=len(self.input_placement[i][j+k+1])
                    for m in range(n):
                        if self.input_placement[i][j+k+1][m][len(self.input_placement[i][j+k+1][m])-1]!=0:
                            oneroop_list.extend(["xf",self.input_placement[i][j+k+1][m][len(self.input_placement[i][j+k+1][m])-1],
                                                    cnt+len(self.input_placement[i][j+k+1][m])-1,1])
                            onedivision_list.extend([oneroop_list])        
                            oneroop_list=[]
                            cnt=cnt+len(self.input_placement[i][j+k+1][m])                 
                    for l in self.filter_placement[i][j+k+1]:
                        oneroop_list.extend([["w",l]])
                    oneroop_list=[oneroop_list[0][0],oneroop_list[0][1],len(oneroop_list)]
                    onedivision_list.extend([oneroop_list])        
                    oneroop_list=[]
                
            #出力をSRAMに戻す
            """onedivision_list.extend([["r",self.output_adress1[i][0],self.pbarray_adress[i][0],len(self.output_adress1[i])]])
            all_list.extend([onedivision_list])
            onedivision_list=[]
            """
            onedivision_list.extend([["rp",self.output_adress1[i][0],self.pbarray_adress[i][0],len(self.output_adress1[i])]])
            all_list.extend([onedivision_list])
            onedivision_list=[]
        return all_list

p3=e()
print(len(p3.timing()))
#print(p3.timing()[0])
print(p3.timing()[len(p3.timing())-1])
