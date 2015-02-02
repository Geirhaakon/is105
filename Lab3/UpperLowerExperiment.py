for l in 'abcdefgijklmnopqrstuvwxyz':
    la = ord(l)
    ua = la - 32
    print 'Lowercase \"%s\" is nr \t %i \t in the ascii table, \t output of \t chr(%i) is \t %s' % (l, la, la, chr(la))
    print 'Uppercase \"%s\" is nr \t %i \t in the ascii table, \t output of \t chr(%i) is \t %s' % (l, ua, ua, chr(ua))
for l in 'abcdefgijklmnopqrstuvwxyz':
    la = ord(l)
    ua = la - 32
    print 'Bitwise or with mask \'100000\' on \"%s\" gives \t%s\t which is the character \t%s' % (chr(ua), ua|32, chr(ua|32))
    print 'Bitwise Xor with mask \'100000\' on \"%s\" gives \t%s\t which is the character \t%s' % (l, la^32, chr(la^32))
