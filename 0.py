# A really great calculator.
# @author A really great student.
import sys
#NFR1
memory = 0


# implemented from FR1
def add(val):
    # FR2
    global memory
    memory = memory + val
    print('Result: %d' % memory)

def subtraction(val:int)->None:
    #FR3
    global memory
    memory = memory - val
    print('Result: %d' % memory)
def about():
    #FR0
    print("""A really great calculator.
Version 1.0.""")

def multiplication(val:int)->None:
    #FR4
    global memory
    memory = memory * val
    print('Result: %d' % memory)
def  division(val:int)->None:
    #FR5
    global memory
    memory = memory / val
    print("Result: %d" % memory)
def  convert()->None:
    #FR7
    #NFR5
    global memory
    original = memory
    memory = memory/100
    print("Original {}Result: {}".format(original ,memory))
def clear()->None:
    #FR6
    global memory
    memory = 0
    print('Result: %d' % memory)
def quit_calculator():
    sys.exit()


def main():
    # add any new commands to the following list
    # command - the name of the command for the user to invoke
    # function - the reference to the function that will invoke the command
    # needs_argument - true if the function needs a number inputted from the user
    functions = [
        {'command': 'add', 'function': add, 'needs_argument': True},
        {'command': 'subtraction', 'function':subtraction, 'needs_argument': True},
        {'command': 'multiplication', 'function':multiplication, 'needs_argument':True},
        {'command': 'division', 'function':division, 'needs_argument': True},
        {'command': 'clear', 'function':clear, 'needs_argument':False},
        {'command': 'about', 'function': about, 'needs_argument': False},
        {'command': 'convert', 'function':convert, 'needs_argument':False},
        {'command': 'quit', 'function': quit_calculator, 'needs_argument': False}
    ]

    while True:

        # request a command from the user
        # we really should handle upper and lowercase commands here
        print(f"<Enter a command:({'|-|'.join([i['command'] for i in functions])})>", end='')
        k = input()
        # loop through the command list and see if we have a match
        for f in functions:
            if k == f['command']:
                try:
                    # NFR8 NFR9 NFR10 NFR12 NFR11 NFR13 NFR14
                    if f['needs_argument']:
                        print('Enter a value:\n>', end='')#NFR2 #NFR3 NFR4
                        v = input()  # read from the command line
                        v = float(v)  # convert to float. We really should do error checking here
                        f['function'](v)
                    else:
                        f['function']()
                except ZeroDivisionError:
                    print('zero division error')
                except Exception as e:
                    print(f'get error{e}')
        # really should handle if the user did not input a valid command


if __name__ == '__main__':
    main()