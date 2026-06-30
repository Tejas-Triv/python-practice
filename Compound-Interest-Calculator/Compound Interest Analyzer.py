title_line = '=' * 184 #to make code clearer

print ('Compound Interest Analyser')
print (title_line)

principal = float (input ('enter principal amount'))
r = float(input('enter rate of interest'))
t = int(input('enter time in years'))
inflation_choice = input('do u want to take in account for inflation? enter y or n: ')#adding inflation calculation

print (title_line)

realprincipal = principal
current_principal = principal

if inflation_choice.lower()=='y':
    inflation_percent = float(input('enter yearly inflation rate(in%)'))
else:
    inflation_percent = 0

inflation_factor = 1 + inflation_percent / 100 #improve readability

for year in range(1,t+1):
    interest = current_principal * r / 100 #rearranged interest and newprincipal order to display correct year interest
    current_principal += interest
    realprincipal = current_principal / inflation_factor ** (year) #added power^year to make code correct
    
    if inflation_choice.lower()=='y':
        print ('Year-',year,'interest acquired=',round(interest),'Current Principal(raw)=',round(current_principal),'total gains(raw)=',round(current_principal-principal),'inflation adjusted principal=',round(realprincipal),'net gains=',round(realprincipal-principal),sep='|')
    else:
        print ('Year-',year,'interest acquired=',round(interest),'Current Principal(raw)=',round(current_principal),'total gains(raw)=',round(current_principal-principal),sep='|')

    print (title_line)

print ('Initial Principal was:',principal,'Final Principal(raw) after',t,'years is:',round(current_principal),'net gains(raw)=',round(current_principal-principal),'Real Principal=',round(realprincipal),'net gains=',round(realprincipal-principal))
print (title_line)
