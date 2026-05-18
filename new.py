l="loveleetcode"
freq={}
for ele in l: 
    if ele in freq:
        freq[ele]+=1
    else: 
        freq[ele]=1 
#looping through   
for key in freq: 
    if freq[key]==1: 
        print(key)
        # print(freq)
        break
    
