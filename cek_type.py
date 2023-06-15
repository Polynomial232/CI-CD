import argparse

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--obj')

    args = parser.parse_args()
    print(type(args.obj))