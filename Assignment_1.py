import re
sl=0
bl=0
sc=0
di=0
print("""enter 1 Register
enter 2 forgot password
enter 3 login""")
s=input()
if s=='1':
    def valida(username):
        return re.match(r'[\w-]{1,20}@\w{2,20}\.\w{2,3}$',username)
    print('Enter the username:',end='')
    username=input()
    va=valida(username)
    print('Enter the password:',end='')
    password=input()
    if len(password)>=5 and len(password)<=16:
        for i in password:
            if i in 'a' and 'z':
                sl=1
            elif i in 'A' and 'Z':
                bl=1
            elif i in '1234567890':
                di=1
            else:
                sc=1
    if va:
        if sl==bl==di==sc==1:
            print('Register is successfull')
            file=open('email.txt','w')
            file.write(username)
            file.write(' ')
            file.write(password)
            file.close()
        else:
            print('Invalid username or password')
    else:
        print('Invalud username or password')
file=open('email.txt','r')
temp=file.read()
file.close()
r=temp.split()
if s=='3':
    print('Enter the username:',end='')
    k=input()
    if k in temp:
        print('login successfully')
    else:
        print('please Register')

if s=='2':
    print('Enter the username:',end='')
    k=input() 
    if k not in temp:
        print('enter valid username')
    else:
        print('''1 for retrive the old password
2 provide new password''')
        d=input()
        if d=='1':
            print(r[-1])
        if d=='2':
            print('enter the new password:',end='')
            new_pass=input()
            file=open('email.txt','w')
            file.write(k)
            file.write(' ')
            file.write(new_pass)
            file.close()
            print('new password updated successfully')
            
            
            
        
    
  
