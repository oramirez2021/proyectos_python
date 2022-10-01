from timeit import timeit
import orjson
import simplejson
import json
import os

def show_menu():
    print('#######################')
    print('Choise the kind of function that you want to execute:')
    print('1. Testing time of parsing json libraries')
    print('2. Testing time of processing numbers algorithms')
    print('3. Testing time of processing strings algorithms')
    print('#######################')


with open("campaign.json") as file:
    response = json.load(file)

def serialize(lib):
    lib.dumps(response)

def sec_convertion(sec, some_text):
    hours = sec // 3600
    left_seconds = sec % 3600
    minutes = left_seconds // 60
    seconds = left_seconds % 60
    text = '{}: It got {} hours ' + ' {} minutes' + ' {} seconds'
    
    print(text.format(some_text,hours,minutes,seconds))

def testing_json_libraries(library_name):
    print(library_name)
    json_time = timeit(lambda: serialize(eval(library_name)), number = 100)
    sec_convertion(json_time, library_name)

def general_function_executor(function_name, arg):
    eval(function_name)(arg)

os.system("cls")
while True:
    show_menu()
    opt = input('Enter here your choice number --> ')
    if opt == "1":
        print("Write the name of the function and the library to mesuere the execution time of parsing a big json: ")
        print('funcion name: testing_json_libraries')
        function = input()
        print('argument value: json, simplejson')
        library = input()
        general_function_executor(function,library)
    elif opt == "2":
        print('opt 2')
        sec_convertion(80000)
    elif opt == "2":
        print('opt 3')
    else:
        print('You wrote an invalid option. Try again')

