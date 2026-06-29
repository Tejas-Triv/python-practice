print('Compound Interest Analyser')
principal=float(input('enter principal amount'))
r=float(input('enter rate of interest'))
t=int(input('enter time in years'))
newprincipal=principal
interest=0
for i in range(0,t):
    interest=(newprincipal*r)/100
    newprincipal+=(newprincipal*r)/100
    print('Year-',i+1,'New Principal=',round(newprincipal),'interest acquired this year=',round(interest),'total gains=',round(newprincipal-principal),sep='|')
print('Initial Principal was:',principal,'Final Principal after',t,'years is:',round(newprincipal),'net gains=',round(newprincipal-principal))
