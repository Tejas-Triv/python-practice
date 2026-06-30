print('Compound Interest Analyser')
principal=float(input('enter principal amount'))
realprincipal=principal
newprincipal=principal
interest=0
r=float(input('enter rate of interest'))
t=int(input('enter time in years'))
ask=input('do u want to take in account for inflation?: enter y or n')#adding inflation calculation
if ask.lower()=='y':
    inflation=float(input('enter yearly inflation rate(in%)'))
else:
    inflation=0
for i in range(0,t):
    interest=(newprincipal*r)/100 #rearranged interest and newprincipal order to display correct year interest
    newprincipal+=interest
    realprincipal=newprincipal*(1-(inflation/100))**(i+1) #added power^i to make code correct
    if ask.lower()=='y':
        print('Year-',i+1,'interest acquired=',round(interest),'New Principal(raw)=',round(newprincipal),'total gains(raw)=',round(newprincipal-principal),'inflation adjusted principal=',round(realprincipal),'net gains=',round(realprincipal-principal),sep='|')
    else:
        print('Year-',i+1,'interest acquired=',round(interest),'New Principal(raw)=',round(newprincipal),'total gains(raw)=',round(newprincipal-principal),sep='|')
print('Initial Principal was:',principal,'Final Principal(raw) after',t,'years is:',round(newprincipal),'net gains(raw)=',round(newprincipal-principal),'Real Principal=',round(realprincipal),'net gains=',round(realprincipal-principal))
