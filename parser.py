#!/usr/bin/python3
import argparse

def parser_func():
   parser = argparse.ArgumentParser()
   parser.add_argument("name", help="your name")
   parser.add_argument("color", help="fave color")
   parser.add_argument("-v","--verbose", help="increase verbosity", action="count", default=0)
   args = parser.parse_args()
   if args.verbose >=2:
       print("'{}' favority color is '{}'".format(args.name, args.color))
   elif args.verbose >=1:
       print("'{}' likes '{}'".format(args.name, args.color))
   else:
       print("'{}' '{}'".format(args.name, args.color))


if __name__ == '__main__':
    #parser.py is executed as a script
    parser_func()
