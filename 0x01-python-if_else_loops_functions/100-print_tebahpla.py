print(''.join(chr(122 - i if i % 2 == 0 else 89 - i // 2) 
              for i in range(26)))
