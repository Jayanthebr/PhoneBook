def main():
    print("-----$---THE PHONE BOOK----$---")
    print("\033[0;31m 0.Delete")
    print("\033[0;32m 1.Add")
    print("\033[1;33m 2.Search")
    print("\033[0;36m 3.Exit")
    container={}
    while True:
        n=int(input('\033[3m  Enter the number    '))
        if n==1:
            try:
                name=input("  \033[3m   Enter the name    ")
                phonenumber=int(input("  \033[3m   Enter the phone number    "))
                container[name]=phonenumber
            except ValueError:
                print('......Please enter a valid number......')
        elif n==2:
            try:
                name1=input(" \033[3m    Search here   ")
                print("\033[3m     phone number of",name1,"is",container[name1]  )
            except:
                print('......Please enter a valid name......')
        elif n==0:
            try:
                name2=input("\033[3m     Enter the name    ")
                del container[name2]
                print('......The file has been succesfully deleted....')
            except:
                 print('       WRONG INPUT(Try something else *___*)       ')
        elif n==3:
                print('    Thank you for using our service  Have a good day    ') 
                break
    print(container)
    with open('enqiury.txt',"w") as reacts:
        pass
    with open('enqiury.txt',"a") as react:
        for key,value in container.items():
            react.write(key+":"+ str(value)+"\n")
    restart=input('    Do You Want To Restart Operation    ')
    if restart==("yes"):
        main()
    else:
        exit()
main()
    

