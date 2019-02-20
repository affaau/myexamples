import sys

def tryException():
    try:
        x = int(input("Enter number: "))
        print("Number is: ", x)
    except Exception as err:    
        print("Error: ")
        print(type(err), " - ", err)
        print(err.args)
    finally:
        print("Print this anyway.")

def eofError():        
    while True:
      # output to stdout:
      print("Yet another iteration ...")
      try:
        # reading from sys.stdin (stop with Ctrl-C):
        number = input("Enter a number: ")
      except EOFError:
        print("\nciao")
        break
      else:
        number = int(number)
        if number == 0:
          print("0 has no inverse", file=sys.stderr)
        else:
          print("inverse of %d is %f" % (number, 1.0/number))

if __name__ == "__main__":
    eofError()    # autotest by $> python exception_test.py < numbers.txt
    #tryException()