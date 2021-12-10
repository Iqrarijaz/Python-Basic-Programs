first='john'
last='smith'
message=first + ' [ '+ last +' ] is a coder '
print(message)
msg=f'{first} [  {last} ] is a coder'
print(msg)

Q="Im a software engineer and dedicated programmer "
print(len(Q))
print(Q.capitalize())
print(Q.upper())
print(Q.casefold())
print(Q.find('t'))
print(Q.replace( 'engineer','developer'))
print('programmer' in Q)
print(Q.title())