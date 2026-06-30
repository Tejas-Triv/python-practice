title_line = '=' * 184 #to make code clearer

print ('Welcome to Compound Interest Analyser')
print (title_line)

principal = float (input ('enter principal amount'))
rate = float(input('enter rate of interest'))
time = int(input('enter time in years'))

while True:#added while block to fix invalid errors
    inflation_choice = input('do u want to take in account for inflation? enter y or n: ')#adding inflation calculation
    inflation_choice=inflation_choice.lower()#making it lowercase beforehand to avoid writing long strings in code later

    print (title_line)

    if inflation_choice not in ['y','n']:
        print ('Please Enter Correct Response(y/n)')
        print (title_line)

    else:
        break

real_principal = principal
current_principal = principal

if inflation_choice =='y':
    inflation_percent = float(input('enter yearly inflation rate(in%): '))
else:
    inflation_percent = 0

inflation_factor = 1 + inflation_percent / 100 #improve readability

for year in range(1,time+1):
    interest = current_principal * rate / 100 #rearranged interest and newprincipal order to display correct year interest
    current_principal += interest
    real_principal = current_principal / inflation_factor ** (year) #added power^year to make code correct
    
    if inflation_choice =='y':
        print ('Year-',year,'interest acquired=',round(interest),'Current Principal(raw)=',round(current_principal),'total gains(raw)=',round(current_principal-principal),'inflation adjusted principal=',round(real_principal),'net gains=',round(real_principal-principal),sep='|')
    else:
        print ('Year-',year,'interest acquired=',round(interest),'Current Principal(raw)=',round(current_principal),'total gains(raw)=',round(current_principal-principal),sep='|')

    print (title_line)
if inflation_choice =='y':
    print ('Initial Principal was:',principal,'Final Principal(raw) after',time,'years is:',round(current_principal),'net gains(raw)=',round(current_principal-principal),'Real Principal=',round(real_principal),'net gains=',round(real_principal-principal),sep='|',end='|\n')

else:
    print ('Initial Principal was:',principal,'Final Principal after',time,'years is:',round(current_principal),'net gains=',round(current_principal-principal),sep='|',end='|\n')
    
print (title_line)
print ('Thanks for Using!')
