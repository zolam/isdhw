Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def BinSearch(list,value):
    begin = 0
    if list[0] == value:
        return 0

    end = len(list)-1
    while(begin < end):
        mid = begin + (end - begin)//2
        if list[mid]>value:
            end = mid - 1
        elif list[mid] <value:
            begin = mid + 1
        else:
            return mid

    if(begin == end):
        if(value == list[begin]):
            return begin
        else:
            return -1

        
>>> list=['a','b','c','d','e','f','g','h']
>>> value='h'
>>> aa=BinSearch(list,value)
>>> aa
7
>>> value='a'
>>> aa=BinSearch(list,value)
>>> aa
0
>>> list=['a']
>>> value='a'
>>> aa=BinSearch(list,value)
>>> aa
0
>>> value='h'
>>> aa=BinSearch(list,value)
>>> aa
-1
>>> 
