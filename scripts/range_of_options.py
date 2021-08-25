# Find the range of options in the sample of configurations
from options import all_options  

def FindMinMaxLength(lst):
    #maxList = min((x) for x in lst)
    min_length = min(len(x) for x in lst )
    max_length = max(len(x) for x in lst )
  
    return min_length, max_length
      
print("Min: " + str(FindMinMaxLength(all_options)[0]))
print("Max: " + str(FindMinMaxLength(all_options)[1]))