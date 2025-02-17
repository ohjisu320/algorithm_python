
N = int(input())

Quarter = 25
Dime= 10
Nickel= 5
Penny = 1
Q_cnt,D_cnt,N_cnt,P_cnt = 0,0,0,0

for _ in range(N) :
      pay = int(input())
      while pay > 0 :
            pay -= Quarter
            Q_cnt+= 1
            if pay-Quarter < 0 :
                  break
      while pay > 0 :
            pay -= Dime
            D_cnt += 1
            if pay-Dime < 0 :
                  break
      while pay > 0 :
            pay -= Nickel 
            N_cnt += 1
            if pay-Nickel < 0 :
                  break
      while pay > 0 :
            pay-=Penny 
            P_cnt += 1
            if pay - Penny < 0 :
                  break
      print(Q_cnt+" "+D_cnt+" "+ N_cnt+" "+ P_cnt)
      
