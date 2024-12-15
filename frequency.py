test={'science': 17,'math': 19,'english': 17,'hindi': 17,'kannada':17,'social':19}
print("the original dictionary: ",str(test))
tval=17
count=0
for key in test :
    if test[key]==tval :
        count=count+1

print("number of occurrences of 17 : "+str(count))