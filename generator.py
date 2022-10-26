import argparse

parser = argparse.ArgumentParser(description="Generate C++ CMakeProject based on arguments provided")
parser.add_argument('-n','--name',help="Name of the project",type=str, required=True)
parser.add_argument('-t','--type',help="Type of the project, executable(exec) or library(lib)?", type=str, required=True)
parser.add_argument('-s','--standard',help="C++ standard of the project",type=str)
parser.add_argument('-cv','--cmake_version',help="Version of the cmake",type=str)

project_types = ['lib','exec']
standards = ['03','11','14','17','20','23']

args = parser.parse_args()

if args.type not in ['lib','exec']:
    raise ValueError(f'Invalid project type, type of the project may only be lib or exec but is {args.type}')

if args.standard is not None:
    if args.standard not in standards:
        raise ValueError(f'Invalid standard only {standards} are supported but current value is {args.standard}')
else:
    args.standard = '17' # defaulting to 17 standard of C++

name = args.name
p_type = args.type
standard = args.standard
cmake_version = args.cmake_version or '3.23' # defaulting to cmake 3.23

# Creating CMakeLists.txt
with open('CMakeLists.txt','w') as CMakeLists:
    content = f'''cmake_minimum_required(VERSION {cmake_version})

project({name})

set(CMAKE_CXX_STANDARD {standard})

'''
    content += f'add_executable({name} main.cpp)' if p_type == 'exec' else f'add_library({name} main.cpp)'
    CMakeLists.write(content)

# Creating main.cpp
with open('main.cpp','w') as main_cpp:
    content = '''#include <iostream>

// Project generated by cmake project generator
int main()
{
    std::cout<<"Hello World!"<<std::endl;
    return 0;
}
'''
    main_cpp.write(content)




    

