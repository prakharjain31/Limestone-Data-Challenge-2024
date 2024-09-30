import pandas as pd 
import numpy as np

df = pd.read_csv("input_game.csv")
# print(df)

player_ids = [i for i in range(1,202)]
players_trust_list = []
for p_id in range(1,202):
    
    trust_list = np.zeros(15)
    titfortattotal = 0
    titfortat = 0
    total0 = 0
    totalTfor0 = 0
    totalTC = 0
    totalTforTC = 0
    totalCC = 0
    totalTforCC = 0
    totalTT = 0
    totalTforTT = 0
    totalCT = 0
    totalTforCT = 0
    ntrust = 0
    ncheat = 0

    df2 = df[(df["p1_id"] == p_id)]
    l = [0 for uj in range(16)]
    for ind in df2.index:
        if (df2['turn'][ind]>=4):
            p=4
            sum=0
            for g in range(3):
                if(df2['p2_action'][ind-1-g]=='TRUST'):
                    sum+=p
                p=p/2
            sum *=2
                
            if(df2['p1_action'][ind]=='TRUST'):
                sum+=1
            l[int(sum)]+=1
        if(df2["p1_action"][ind] == "TRUST"):
            ntrust+=1
        else:
            ncheat+=1
        if(df2["turn"][ind] == 1):
            total0 += 1
            if(df2["p1_action"][ind] == "TRUST"):
                totalTfor0 += 1
        else:
            if(((df2["p1_action"][ind-1] == "TRUST") & (df2["p2_action"][ind-1] == "CHEAT"))):
                totalTC += 1
                if(df2["p1_action"][ind] == "TRUST"):
                    totalTforTC += 1
            if(((df2["p1_action"][ind-1] == "CHEAT") & (df2["p2_action"][ind-1] == "CHEAT"))):
                totalCC += 1
                if(df2["p1_action"][ind] == "TRUST"):
                    totalTforCC += 1
            if(((df2["p1_action"][ind-1] == "TRUST") & (df2["p2_action"][ind-1] == "TRUST"))):
                totalTT += 1
                if(df2["p1_action"][ind] == "TRUST"):
                    totalTforTT += 1
            if(((df2["p1_action"][ind-1] == "CHEAT") & (df2["p2_action"][ind-1] == "TRUST"))):
                totalCT += 1
                if(df2["p1_action"][ind] == "TRUST"):
                    totalTforCT += 1
            if((df2["p2_action"][ind-1] == df2["p1_action"][ind])):
                titfortat += 1
        
    titfortattotal += len(df.index)

    df2 = df[(df["p2_id"] == p_id)]
    for ind in df2.index:
        if (df2['turn'][ind]>=4):
            p=4
            sum=0
            for g in range(3):
                if(df2['p1_action'][ind-1-g]=='TRUST'):
                    sum+=p
                p=p/2
            sum *=2
                
            if(df2['p2_action'][ind]=='TRUST'):
                sum+=1
            l[int(sum)]+=1
        if(df2["p2_action"][ind] == "TRUST"):
            ntrust+=1
        else:
            ncheat+=1
        if(df2["turn"][ind] == 1):
            total0 += 1
            if(df2["p2_action"][ind] == "TRUST"):
                totalTfor0 += 1
        else:
            if(((df2["p2_action"][ind-1] == "TRUST") & (df2["p1_action"][ind-1] == "CHEAT"))):
                totalTC += 1
                if(df2["p2_action"][ind] == "TRUST"):
                    totalTforTC += 1
            if(((df2["p2_action"][ind-1] == "CHEAT") & (df2["p1_action"][ind-1] == "CHEAT"))):
                totalCC += 1
                if(df2["p1_action"][ind] == "TRUST"):
                    totalTforCC += 1
            if(((df2["p2_action"][ind-1] == "TRUST") & (df2["p1_action"][ind-1] == "TRUST"))):
                totalTT += 1
                if(df2["p1_action"][ind] == "TRUST"):
                    totalTforTT += 1
            if(((df2["p2_action"][ind-1] == "CHEAT") & (df2["p1_action"][ind-1] == "TRUST"))):
                totalCT += 1
                if(df2["p2_action"][ind] == "TRUST"):
                    totalTforCT += 1
            if((df2["p1_action"][ind-1] == df2["p2_action"][ind])):
                titfortat += 1
    titfortattotal += len(df.index)

    trust_list[0] = (totalTfor0 / total0)*100
    trust_list[1] = (totalTforTC / totalTC)*100
    trust_list[2] = (totalTforCC / totalCC)*100
    trust_list[3] = (totalTforTT / totalTT)*100
    trust_list[4] = (totalTforCT / totalCT)*100
    trust_list[5] = (titfortat / titfortattotal)*100
    trust_list[6] = (ntrust / (ncheat+ntrust))*100
    
    for i in range(8):
        trust_list[7+i]=l[2*i]/(l[2*i]+l[2*i+1])*100
    players_trust_list.append(trust_list)
    # print(p_id , trust_list)
# print(players_trust_list)




