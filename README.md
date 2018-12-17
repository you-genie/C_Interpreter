# C_Interpreter


# [CS420] Compiler Design

Members
=================
20150046 고찬혁, 20150691 정유진, 20184326 배우근  
@authored by Stag, Little Octo, Flying Fish 뿌힝힝


Contribution
=================
* 고찬혁: implement command line interface
* 정유진: implement interpreter
* 배우근: impelemnt parser

Implementation Environment
=================
* Python 3.7.1
* Ply 3.10

How to use
=================
* Linux or MacOS
1. wget http://www.dabeaz.com/ply/ply-3.10.tar.gz
2. tar xzf ply-3.10.tar.gz
3. cd ply-3.10
4. python setup.py install
5. Try to execute "import ply.lex" in python shell for check valid installation.

* Window
1. download zip file at <http://www.dabeaz.com/ply/ply-3.10.tar.gz>
2. unzip the file
3. cd ply-3.10
4. python setup.py install
5. Try to execute "import ply.lex" in python shell for check valid installation.

## [Wiki](https://github.com/krista2811/C_Interpreter/wiki) 두둠

## 구현 상황 ( Interpreter )
- [x] Abstract class 구현
- [x] TypeTable 구현
- [x] Ptr
- [x] Arrow
- [x] EnvTable
- [x] ValueTable(Memory)
- [x] History
- [x] Var
- [x] VarManager
- [x] Basic Grammar
- [x] Basic Interpreter
- [x] Advanced Grammar
- [x] Advanced Interp
- [x] TypeChecker
- [x] DupChecker  
- [x] Merge with Parser
