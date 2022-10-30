print 'choose: '
a = raw_input (' apple[a], grape[g], quit[q] ')
if a=='a':
    print 'apple'
elif a=='g':
    print 'grape'
elif a=='q':
    print 'quit'
    print 'Are you sure?'
    print 'yes[y], no[n]'
    b=raw_input ('Choose: ')
    if b=='y':
        quit()
    elif b=='n':
      print 'returning to menu'