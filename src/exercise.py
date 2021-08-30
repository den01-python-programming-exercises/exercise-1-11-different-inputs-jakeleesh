def main():
    #write your code below this line
    value_str = input("Give a string:")
    value_int = int(input("Give an integer:"))
    value_float = float(input("Give a float:"))
    value_bool = input("Give a boolean:")
    print("You gave the string " + value_str)
    print("You gave the integer " + str(value_int))
    print("You gave the float " + str(value_float))
    print("You gave the boolean " + value_bool)

if __name__ == '__main__':
    main()
