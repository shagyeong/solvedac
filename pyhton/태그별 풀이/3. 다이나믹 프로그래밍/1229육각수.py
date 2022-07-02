#문제오류:
#예제입력 1 : 1 + 1 + 1 + 6 + 15 = 25, != 26

#def hex(n:int, time:int):
#    if n == 1:
#        return time
#    else:
#        hexnumber = 1
#        u = 2
#        c = 1
#        d = 2
#
#        while hexnumber < n:
#            hexnumber  = (hexnumber +
#                          u +
#                          c +
#                          d)
#            if hexnumber > n:
#                hexnumber  = (hexnumber -
#                          u -
#                          c -
#                          d)
#                break
#            u += 1
#            c += 2
#            d += 1
#        
#        time += 1    
#        n -= hexnumber
#
#        print(n)
#        
#        return hex(n, time)
#print(hex(26, 0))
#print()
#print(hex(130, 0))
#print()
#print(hex(146858, 0))
#print()
#print(hex(999999, 0))