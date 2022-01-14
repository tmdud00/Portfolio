import random

행맨=[
    
   '''
  +---+

  |   |

      |

      |

      |

      |

 ========''',

   '''
  +---+

  |   |

  O   |

      |

      |

      |
      
 ========''',

   '''
  +---+

  |   |

  O   |
  |
      |

      |

      |

 ========''',

   '''
  +---+

  |   |

  O   |
 /|
      |

      |

      |

 =======''',
    
   '''
  +---+

  |   |

  O   |
 /|＼
      |

      |

      |

 =======''',
    
   '''
  +---+

  |   |

  O   |
 /|＼
 /    |

      |

      |

 =======''',
    
        
   '''
  +---+

  |   |

  O   |
 /|＼
 / \  |

      |

      |

 =======''']

단어='apple banana candle dinner effect fade gmail house idea jungle konkuk lemon monkey naver opinion park queen rabbit stream travel universe vet wave xmas yaght zebra'.split( )
    
def 게임설명():
    print('='*30)
    print('알파벳을 1자씩 입력하여 숨겨진 단어를 맞춰주세요!')
    print('기회는 총 6번입니다!')
    print('='*30)

def 단어생성(단어):
    n=random.randint(0,len(단어)-1)
    return 단어[n]

def 화면생성(행맨,틀린단어,맞춘단어,비밀단어):
    print(행맨[len(틀린단어)])
    print()
    print('틀린단어 표시:',end=' ')
    for i in 틀린단어:
        print(i, end=' ')
    print()

    빈칸='_'*len(비밀단어)
    print()


    for i in range(len(비밀단어)):
        if 비밀단어[i] in 맞춘단어:
            빈칸=빈칸[:i]+비밀단어[i]+빈칸[i+1:]
    for i in 빈칸:
        print(i,end=' ')
    print()

def 맞추기(먼저맞춘것):
     while True:
         print()
         guess=input("알파벳을 입력해주세요:")
         guess=guess.lower()
         if len(guess)!=1:
             print("1글자만 입력해주세요!")
         elif guess in 먼저맞춘것:
             print("이미 입력한 글자입니다. 다른 알파벳을 입력해주세요!")
         elif guess not in 'abcdefghijklmnopqrstuvwxyz':
             print("알파벳이 아닙니다. 알파벳을 입력해주세요!")
         else:
             return guess

게임설명()
틀린단어=''
맞춘단어=''
비밀단어=단어생성(단어)
게임종료=False

while True:
    화면생성(행맨,틀린단어,맞춘단어,비밀단어)
    guess=맞추기(틀린단어+맞춘단어)
    if guess in 비밀단어:
        맞춘단어=맞춘단어+guess

        모두맞춤=True
        for i in range(len(비밀단어)):
            if 비밀단어[i] not in 맞춘단어:
                모두맞춤=False
                break

        if 모두맞춤:
            print('축하합니다. <'+비밀단어+'> 게임에서 이겼습니다!')
            게임종료=True
    else:
        틀린단어=틀린단어+guess
        if len(틀린단어)==len(행맨)-1:
            화면생성(행맨,틀린단어,맞춘단어,비밀단어)
            print("기회를 모두 사용하셨습니다!")
            print(str(len(틀린단어))+'번 틀림')
            print(str(len(맞춘단어))+'번 맞춤')
            print('비밀단어는 <'+비밀단어+'> 입니다')
            게임종료=True
    if 게임종료:
        break
