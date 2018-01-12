string = 'ABCDCDC'
sub_string = 'CDC'
count = 0
for i in range(len(string)):
    if string[i: i + len(sub_string)] == sub_string[:]:
        count +=1
                
            

print(count)
                
        
