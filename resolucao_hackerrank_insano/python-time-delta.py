# When users post an update on social media,such as a URL, image, status update etc.,
# other users in their network are able to view this new post on their news feed.
# Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.
# Since sometimes posts are published and viewed in different time zones, this can be confusing.
# You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
# Day dd Mon yyyy hh:mm:ss +xxxx
# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.
import calendar
from datetime import datetime, timedelta
'Sun 10 May 2015 13:54:36 -0000'
# -  0  1   2    3        4
# Complete the time_delta function below.

def fix_extratime(e):
    h = int(int(e)/100)
    m = int(int(e) - (h*100))
    delta = timedelta(hours=h, minutes=m)
    return delta
    
def fix_time(t: str):
    t = t.split(' ')
    t.pop(0)
    for i in range(len(calendar.month_name)):
        if t[1] in calendar.month_name[i]:
            save = i
    t[1] = str(save)
    d, m, y, h, extra = t
    t = d +'/' + m + '/' +y +' ' + h
    t = datetime.strptime(t, '%d/%m/%Y %H:%M:%S')
    t = t - fix_extratime(extra)
        
        # print(t[1])
        # print(calendar.month_name[i])
    
    return t

def time_delta(t1, t2):
    result = t1 - t2
    result = int(result.total_seconds())
    if result > 0:
        return result
    return result * -1
    
if __name__ == '__main__':

    # t1 = fix_time('Sat 02 May 2015 19:54:36 +0530')
    # t2 = fix_time('Fri 01 May 2015 13:54:36 -0000')
    # a = time_delta(t1, t2)
    # print(a)
    # t1 = fix_time('Sun 10 May 2015 13:54:36 -0700')
    # t2 = fix_time('Sun 10 May 2015 13:54:36 -0000')
    # a = time_delta(t1, t2)
    # print(a)
    
    
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')


    t = int(input())
    lista = []
    for t_itr in range(t):
        t1 = input()
        t1 = fix_time(t1)

        t2 = input()
        t2 = fix_time(t2)

        delta = time_delta(t1, t2)

        # fptr.write(delta + '\n')
        lista.append(delta)
        # print(delta)
    for i in lista:
        print(i)

# rascunho

# import math
# import os
# import random
# import re
# import sys
# import calendar

# # Complete the time_delta function below.
# def time_delta(t1, t2):
#     ...
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input())

#     for t_itr in range(t):
#         t1 = input()

#         t2 = input()

#         delta = time_delta(t1, t2)

#         fptr.write(delta + '\n')

#     fptr.close()
