def peru(total,months,usage):
    state = 0
    extra = 0
    carry_over = 0
    total1=total
    for state in months:
     if extra == total - usage[state] >=0:
      extra = total - usage
      carry_over = extra
     else:
       extra = 0
     total =+ carry_over
    print(total1+total)
peru("10,3,[4,6,2]")