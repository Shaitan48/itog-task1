import getpass as gt
import os
from time import gmtime, strftime
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--name', nargs='?', default=gt.getuser())
parser.add_argument('--path', nargs='?', default='.')
parser.add_argument('--datetimecur', nargs='?', default=strftime("%Y-%m-%d %H:%M:%S", gmtime()))

args = parser.parse_args()

print(f'Hello, {args.name}!')
print(f'Current time:  {args.datetimecur}')
print("Total number of files: ", len(os.listdir(args.path)))

files = os.listdir(args.path)
fullPath = []
for file in files:
    fullPath.append(os.path.join(args.path, file))

items = []
for file in fullPath:
    if os.path.isfile(file):
        items.append(file)

items.sort(key=lambda f: os.stat(f).st_size, reverse=True)


items = items[:10]

print('Top ', len(items), ' lagest files (in KB)')
for f in items:
    print(f'{f}: {round(os.path.getsize(f) / 1024, 2)} KB')