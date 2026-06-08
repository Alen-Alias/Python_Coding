p=input()
fu=False
fl=False
fd=False
fs=False
fws=False

for i in p:
    if i.isUpper():
        fu=True
    elif i.isLower():
        fl=True
    elif i.isdigit():
        fd=True
    elif i.isspace():
        fws=True
    else:
        fs=True

if fw==True and fs==True and fws==True and fd==True and fl==True and len(p)>=8:
    print("Correct")
else:
    print("Incorrect")