score = 'Bs'

match score:
    case "B":
        print("YES")
    case "C":
        print("No")
    case _: # _表示 default
        print('score is ??????')



age = 15

match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old')
    case 11 | 12 | 13 | 14 | 15| 16 | 17 | 18:
        print("11~18 years old.")
    case 19:
        print('19 years old')
    case _:
        print('not sure.')


print('\n')

# 匹配列表

args = ['gcc', 'hello.c', 'world.c']
#args = ['clean']
# args = ['gcc']

match args:
    case ['gcc']:
        print ('gcc: missing sources file(s).')
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')