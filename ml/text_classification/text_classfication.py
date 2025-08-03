# first we genrating vocablary dictionary here 


vocab={}
i=1

with open('t1.txt') as f:
    x=f.read().lower().split()
    
for word in x:
    if word in vocab:
        continue
    else:
        vocab[word]=i
        i+=1
        
with open('t2.txt') as h:
    y=h.read().lower().split()

for word in y:
    if word in vocab:
        continue
    else:
        vocab[word]=i
        i+=1    
 
#here we are creating the vocabulary dictionary here .....    
print(vocab)
print(len(vocab))    
    
#now we are doing feature extraction 

one=['t1.txt']+[0]*len(vocab)


with open('t1.txt') as f:
    x=f.read().lower().split()
    
for word in x:
    one[vocab[word]]+=1
  
  
two=['t2.txt']+[0]*len(vocab)    
          
with open('t2.txt') as h:
    y=h.read().lower().split()
  
for word in y:
    two[vocab[word]]+=1    


print("one here ", one)
print('\n')
print("two here", two)

