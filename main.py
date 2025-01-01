#imports
from sympy import *
x, y, z = symbols('x y z')
from sympy.series.sequences import RecursiveSeq
n=Symbol("n")
init_printing(use_unicode=True)
import os

#paths
p="SFProject.txt" #for equation storage
sgf="funnystyleguide.txt" #guide for writing function equations
sgr="cursedstyleguide.txt" #guide for writing sequence equations

#dictionary presets: pre-existing examples for program
sdict={
    'fibo': ['Fibo', 'Fibonacci Sequence', 'a(n-1)+a(n-2)', '[1, 1]', '2', 'A very famous sequence.', 's'],
    'arth1': ['Arth1', 'Arithmetic Sequence (d=2)', 'a(n-1)+2', '[1]', '1', 'A simple arithmetic recursive sequence.', 's'],
    'geo1': ['Geo1', 'Geometric Sequence d=(1/2)', 'a(n-1)*0.5', '[1]', 'A overcomplicated way of writing a basic geometric sequence', 's']
    }

fdict={
    'lin': ['Lin', 'Linear Parent Function', 'x', 'R', 'R', 'A basic linear function.', 'f'], 
    'quad': ['Quad', 'Quadratic Parent Function', 'x**2', 'R', 'R', 'A basic quadratic function', 'f']
    }

#class definitions
class func():
    def __init__(self, name, eq, d ,r, desc):
        self.name=name
        self.eq=sympify(eq)
        self.d=d
        self.r=r
        self.desc=desc

    def __str__(self):
        string=(self.name+': '+'y='+str(self.eq)+'\n '+self.desc+'\n '+'Domain: '+self.d+'\n '+'Range: '+self.r)
        return string
    
    #basic methods
    def n_term(self):
        """
        sig:self->none
        prints terms between user inputed a and b
        """
        while True:
            ans=input('x=')
            try:
                ans=float(ans)
                print(self.eq.subs(x, ans))
                wait=input('Press ENTER to continue.')
                print('\n')
                return exist_f([self.name, self.eq, self.d, self.r, self.desc])
            except ValueError:
                print('Invalid input, please enter a number')

    #calculus methods
    def gen_derive_base(self):
        """
        sig:self->expr
        returns general derivative form
        """
        while True:
            z=input('Which derivative would you like? (first, second, third, etc.): ')
            try:
                z=int(z)
                d=diff(self.eq, x, z)
                return d
            except ValueError:
                print('Invalid input, please enter a positive integer.')

    def gen_derive(self):
        """sig:self->none
        finds general form of derivative for function"""
        print(self.gen_derive_base())
        wait=input('Press ENTER to continue.')
        print('\n')
        return exist_f([self.name, self.eq, self.d, self.r, self.desc])

    def point_deriv(self):
        """sig: self->none
        finds derivative at a point"""
        e=self.gen_derive_base()
        while True:
            p=input('At which point would you like the derivative of?')
            try:
                p=float(p)
                print(e.subs(x, p))
                wait=input('Press ENTER to continue.')
                print('\n')
                return exist_f([self.name, self.eq, self.d, self.r, self.desc])
            except ValueError:
                print('Invalid input, please enter a real number.')
    
    def indefintegral(self):
        """sig:self->none
        finds indefinite integral for function"""
        print(integrate(self.eq, x))
        wait=input('Press ENTER to continue.')
        print('\n')
        return exist_f([self.name, self.eq, self.d, self.r, self.desc])

    def defintegral(self):
        """sig:self->none
        finds definite integral between two points"""
        a=input('please input the first, smaller, boundry: ')
        try:
            a=float(a)
            while True:
                b=input('Please enter the second, larger, boundry: ')
                try:
                    b=float(b)
                    if a>b:
                        int('hello') #induces ValueError
                    else:
                        print(integrate(self.eq, (x, a, b)))
                        wait=input('Press ENTER to continue.')
                        print('\n')
                        return exist_f([self.name, self.eq, self.d, self.r, self.desc])
                except ValueError:
                    print('Invalid input, please enter a number larger than the first')
        except ValueError:
            print('Invalid input, please enter a number')

class recurse():
    def __init__(self, name, eq, t, i, desc):
        self.a=Function("a")
        self.name=name
        self.eq=sympify(eq)
        self.t=s2t(t)
        self.i=i
        self.desc=desc
        self.R=RecursiveSeq(self.eq, self.a(n), n, self.t)

    def __str__(self):
        string=(self.name+': '+'a(n)='+str(self.eq)+'\n '+'Terms: '+str(self.t))
        return string

    #quality methods
    def seq_info(self):
        """
        sig:self->none
        prints information about the sequence
        """
        self.seq_type()
        print('   ', self.desc)
        wait=input('Press ENTER to continue')
        print('\n')
        return (exist_recurse([self.name, str(self.eq), str(self.t), self.i, self.desc]))

    def seq_type(self):
        """
        sig:self->none
        finds information about the sequence's type
        """
        h=[]
        ty=''#empty string
        d=0
        for x in zip(range(10), self.R):
            a=x[1]
            h.append(a)
        if h[2]-h[1]==h[4]-h[3]:
            d=h[2]-h[1]
            return print('    This sequence is an arithmetic sequence with a difference of', d)
        elif h[2]/h[1]==h[4]/h[3]:
            d=h[2]/h[1]
            return print('    This sequence is a geometric sequence with a rate of', d)
        else:
            return print('    This sequence is not arithmetic or geometric.')

    #sequence methods
    def n_terms(self):
        """sig:self->none
        returns list of terms between user inputed a and b"""
        while True:
            a=input('Please type the first, lower boundary: ')
            try:
                a=int(a)
                if a<=0:
                    int('hello') #induces ValueError
                else:
                    while True:
                        b=input('Please type the second boundary: ')
                        try:
                            b=int(b)
                            if a>b:
                                int('hello') #induces ValueError
                            elif a<b:
                                print(self.R[a:b+1])
                                wait=input('Press ENTER to continue')
                                print('\n')
                                return (exist_recurse([self.name, str(self.eq), str(self.t), self.i, self.desc]))
                        except ValueError:
                            print('Invalid input! Please enter an integer!')
            except ValueError:
                print('Invalid input! Please enter a postive integer.')

    def n_sums(self):
        """sig:self->none
        returns sum of terms between two points"""
        while True:
            a=input('Please type the first, lower boundary: ')
            try:
                a=int(a)
                if a<=0:
                    int('hello') #induces ValueError
                else:
                    while True:
                        b=input('Please type the second boundary: ')
                        try:
                            b=int(b)
                            if a>=b:
                                int('hello') #induces ValueError
                            elif a<b:
                                t=[]
                                for x in zip(range(b), self.R):
                                    v=x[1]
                                    t.append(v)
                                if a==0:
                                    h=t[0:]
                                else:
                                    h=t[a-1:]
                                acc=0
                                for val in h:
                                    acc+=val
                                print(acc)
                                wait=input('Press ENTER to continue')
                                print('\n')
                                return (exist_recurse([self.name, str(self.eq), str(self.t), self.i, self.desc]))
                        except ValueError:
                            print('Invalid input! Please enter an integer larger than the first!')
            except ValueError:
                print('Invalid input! Please enter a positive integer.')   

    #series methods
    def n_ps(self):
        """sig:self->none
        returns list of partial sums between a and b"""
        acc=[]
        ps=0
        while True:
            a=input('Please type the first, lower boundary: ')
            try:
                a=int(a)
                if a<=0:
                    int('hello') #induces ValueError
                else:
                    while True:
                        b=input('Please type the second boundary: ')
                        try:
                            b=int(b)
                            if a>=b:
                                int('hello') #induces ValueError
                            else:
                                t=[]
                                for x in zip(range(b), self.R):
                                    v=x[1]
                                    t.append(v)
                                if a==0:
                                    h=t[0:]
                                else:
                                    h=t[a-1:]
                                for val in h:
                                    ps+=val
                                    acc.append(ps)
                                print(ps)
                                wait=input('Press ENTER to continue')
                                print('\n')
                                return (exist_recurse([self.name, str(self.eq), str(self.t), self.i, self.desc]))
                        except ValueError:
                            print('Invalid input! Please enter an integer larger than the first!')
            except ValueError:
                print('Invalid input! Please enter a positive integer.')

#file-related functions
def filing(code, t):
    """sig: str, [str]->none
    adds function/series to file"""
    global fdict
    global sdict
    if t[-1]=='f':
        f=open(p, 'a')
        string=code.lower()+'`~`'+code+'`~`'+t[0]+'`~`'+t[1]+'`~`'+t[2]+'`~`'+t[3]+'`~`'+t[4]+'`~`f\n'
        f.write(string)
        f.close()
    if t[-1]=='s':
        f=open(p, 'a')
        string=code.lower()+'`~`'+code+'`~`'+str(t[0])+'`~`'+str(t[1])+'`~`'+str(t[2])+'`~`'+str(t[3])+'`~`'+str(t[4])+'`~`s\n'
        f.write(string)
        f.close()
    return

def dict_gather(dict, status):
    """
    sig: dict, str->dict
    goes through lines of file, formats lines, and adds to dictionary
    """
    f=open(p, 'r')
    for line in f:
        acc=[]
        t=str.split(line, '`~`')
        if status in t[-1]:
            acc=t[1:len(t)-1]
            acc.append(status)
            dict[t[0]]=acc
    f.close()
    return dict

def s2t(s):
    """sig:str->[int]
    turns lists of type string to type list"""
    acc=''#empty string
    for char in s:
        if char=='[' or char==']' or char=="'":
            pass
        else:
            acc+=char
    acc=str.split(acc, ',')
    for i in range(0, len(acc)):
        acc[i]=int(acc[i])
    return acc

#menu functions
def boot_up():
    """sig:none->none
    serves as boot-up menu"""
    print('Welcome to the Sequences and Functions Database!')
    print('  [M] Main Menu\n  [C] Config\n  [Q] Quit')
    while True:
        boot=input('Please select an option: ')
        if boot.lower() in 'main menu' or boot.lower()=='m':
            return main_menu()
        if boot.lower()=='config' or boot.lower()=='c':
            return config_menu()
        if boot.lower()=='quit' or boot.lower()=='q':
            return
        else:
            print('Invalid response!')

def main_menu():
    """sig:none->none
    serves as main menu"""
    print('Main Menu')
    print('  [N] Create a new equations\n  [E] View existing equations\n  [R] Back to START (Enter "R" at anytime to return to previous menu)')
    while True:
        main=input('Please select an option: ')
        if main.lower()=='n':
            return new_menu()
        if main.lower()=='e':
            return existing_menu()
        if main.lower()=='r':
            return boot_up()
        else:
            print('Invalid input!')

def config_menu():
    """sig:none->none
    serves as config menu"""
    print('The Sequences and Functions file is locatd at', p)
    config=input('Press ENTER to return to START')
    return boot_up()

def new_menu():
    """sig:none->none
    serves as menu to create new function"""
    print('Select the type of equation you would like to input')
    print('  [F] Function\n  [S] Recursive Sequence')
    new=input('Please select an option: ')
    if new.lower()=='f':
        return new_func()
    if new.lower()=='s':
        return new_recurse()
    if new.lower()=='r':
         return main_menu()

def new_func():
    """sig:none->none
    creates new function and calls another function to file it"""
    while True:
        code=input("Please enter a code to easily identify the function for later: ")
        while True:
            while True:
                name=input("Please enter the function's name: ")
                while True:
                    desc=input("Please enter a description of the function: ")
                    while True:
                        eqput=input("Please enter the function's equation or enter G to see the style guide: ")
                        if eqput.lower()=='g':
                            style_guide('f')
                        else:
                            while True:
                                d=input("Domain (Type 'R' for all real numbers): ")
                                if d.isalpha():
                                    d=d.upper()
                                while True:
                                    r=input("Range (Type 'R' for all real numbers): ")
                                    if r.isalpha():
                                        r=r.upper()
                                    filing(code, [name, eqput, d, r, desc, 'f'])
                                    return new_menu()

def new_recurse():
    """sig:none->none
    creates new sequence and calls another function to file it"""
    t=[]
    while True:
        code=input("Please enter a code to easily identify the sequence for later: ")
        if code.lower() in sdict:
            print('This code already exists, please use another code!')
        else:
            while True:
                name=input("Please enter the sequence's name: ")
                while True:
                    desc=input("Please enter a description of the sequence: ")
                    while True:
                        eqput=input("Please enter the sequence's equation or enter G to see the style guide: ")
                        if eqput.lower()=='g':
                            style_guide('s')
                        else:
                            while True:
                                i=input('What is the degree of your sequence?')
                                try:
                                    i=int(i)
                                    try:
                                        for e in range(0, i):
                                            th=input('Please enter term ' + str(e+1) +':')
                                            float(th)
                                            t.append(th)
                                    except ValueError:
                                        print('Invalid, please enter an integer.')
                                    else:
                                        filing(code, [name, eqput, t, i, desc, 's'])
                                        return new_menu()
                                except ValueError:
                                    print('Invalid, please enter an integer.')

def existing_menu():
    """sig:none->none
    serves as menu for exisitng functions/sequences"""
    global fdict
    global sdict
    sdict=dict_gather(sdict, 's')
    fdict=dict_gather(fdict, 'f')
    print('Function Database')
    print('  Functions:')
    for key in fdict:
        print('   ['+str(fdict[key][0])+']: '+ str(fdict[key][1]))
    print('  Sequences:')
    for key in sdict:
        print('   ['+str(sdict[key][0])+']: '+str(sdict[key][1]))
    while True:
        existing=input('Please enter a code: ')
        if existing.lower() in fdict:
            return exist_f(fdict[existing][1:])
        elif existing.lower() in sdict:
            return exist_recurse(sdict[existing][1:])
        elif existing.lower()=='r':
            return main_menu()
        else:
            print('Invalid input, please enter a code from above.')

def exist_f(t):
    """sig:[str]->none/methods
    serves as menu to execute methods for functions"""
    fun=func(t[0], t[1], t[2], t[3], t[4])
    print(fun)
    print('Please select an option\n  [E] Evaluate function at a point\n  [GD] Find the general derivative form\n  [D] Find the derivative at a specific point\n  [I] Find the indefinite integral\n  [DI] Find the definite integral between two points')
    while True:
        exist=input('Please select an option: ')
        if exist.lower()=='e':
            return fun.n_term()
        elif exist.lower()=='gd':
            return fun.gen_derive()
        elif exist.lower()=='d':
            return fun.point_deriv()
        elif exist.lower()=='i':
            return fun.indefintegral()
        elif exist.lower()=='di':
            return fun.defintegral()
        elif exist.lower()=='r':
            return existing_menu()
        else:
            print('Invalid input, please try again!')

def exist_recurse(t):
    """sig:[str]->none/methods
    serves as menu to execute methods for sequence"""
    try:
        cursed=recurse(t[0], t[1], t[2], t[3], t[4])
    except ValueError:
        print('Sequence corrupted: you may have entered the wrong degree, please try to recreate this sequence!')
        wait=input('Press ENTER to continue')
        return existing_menu()
    print(cursed)
    print('Please select an option\n  [I] More information\n  [T] Terms between two bounds\n  [S] Sum of terms between two bounds\n  [P] Partial Sums between two bounds')
    while True:
        exist=input('Please select an option: ')
        if exist.lower()=='i':
            return cursed.seq_info()
        elif exist.lower()=='t':
            return cursed.n_terms()
        elif exist.lower()=='s':
            return cursed.n_sums()
        elif exist.lower()=='p':
            return cursed.n_ps()
        elif exist.lower()=='r':
            return existing_menu()
        else:
            print('Invalid input.')

def style_guide(status):
    """
    sig:str->none
    opens style guide based on status string
    """
    if status=='f':
        f=open(sgf, 'r')
        print(f.read())
        f.close()
    if status=='s':
        f=open(sgr, 'r')
        print(f.read())
        f.close()
    stylish=input('Press ENTER to return to creator')
    return

#main
if os.path.exists(p):
    boot_up()
else:
    f=open(p, 'w')
    f.close()
    boot_up()