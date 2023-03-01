import argparse

def input_parse():
    # initialize parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument("--name", type=str, default="Bob")
    parser.add_argument("--age", type=int, required=True) # this is so it gives a more clear error if age is missing
    # parse arguments from command line
    args = parser.parse_args()
    # get the name
    return args

def hello(name, age):
    print("Hello, my name is " + name + "!")
    print("I am " + str(age) + " years old!")

def main():
    # run input parse to get name
    args = input_parse()
    # pass name amd age to hello()
    hello(args.name, args.age)

# if code is being executed from cmd line, then run it
# otherwise, e.g. if it's run from another script, it will just define functions but not run
if __name__=="__main__":
    main()