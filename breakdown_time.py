def breakdown_time(seconds):
   if type(seconds) != int or seconds < 0:
       return -1
   if seconds==0:
       return{}
   
   h = seconds // 3600
   seconds = seconds % 3600
    
   m=seconds//60
   s= seconds%60

   result={}
   if h:
       result[3600]=h
       print("hours:",h)
   if m:
       result[60]=m
       print("minutes:",m)
   if s:
       result[1]=s
       print("seconds:",s)
   return result
      


print(breakdown_time(512))

#%%
#breakdown_time(seconds)
#   Convert a non-negative integer number of seconds into as few units as
#   possible using 3600, 60, and 1. Return a dictionary like {3600: h, 60: m, 1: s}.
#   If input is invalid (not int or negative), return -1.
#  For seconds == 0, return {}.
#
#
#
