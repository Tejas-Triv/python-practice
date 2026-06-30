print ('Compound Interest Analyser')

principal = float (input ('enter principal amount'))
r = float(input('enter rate of interest'))
t = int(input('enter time in years'))
inflation_choice = input('do u want to take in account for inflation?: enter y or n')#adding inflation calculation

realprincipal = principal
current_principal = principal
interest = 0

if inflation_choice.lower()=='y':
    inflation = float(input('enter yearly inflation rate(in%)'))
else:
    inflation = 0

for year in range(1,t+1):
    interest = current_principal * r / 100 #rearranged interest and newprincipal order to display correct year interest
    current_principal += interest
    realprincipal = current_principal * (1 - (inflation / 100)) ** (year) #added power^i to make code correct
    
    if inflation_choice.lower()=='y':
        print ('Year-',year,'interest acquired=',round(interest),'Current Principal(raw)=',round(current_principal),'total gains(raw)=',round(current_principal-principal),'inflation adjusted principal=',round(realprincipal),'net gains=',round(realprincipal-principal),sep='|')
    else:
        print ('Year-',year,'interest acquired=',round(interest),'Current Principal(raw)=',round(current_principal),'total gains(raw)=',round(current_principal-principal),sep='|')
        
print ('Initial Principal was:',principal,'Final Principal(raw) after',t,'years is:',round(current_principal),'net gains(raw)=',round(current_principal-principal),'Real Principal=',round(realprincipal),'net gains=',round(realprincipal-principal))
