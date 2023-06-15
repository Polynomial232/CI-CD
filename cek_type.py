import argparse
import ast

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--obj')

    args = parser.parse_args()
    parsed_json = ast.literal_eval(args.obj)
    print(type(parsed_json))