is_hot=False
is_cold=False
if is_hot:
    print('it is hot today')
    print('drink plenty of water')
elif is_cold:
    print('its a cold day')
    print('wear hot clothes')
else:
    print("neutral day")
    

Price=1000000
good_credit=False
if good_credit:
    putdown=(Price * 10)/100
    Price=Price-putdown
else:
    putdown=(Price*20)/100
    Price = Price - putdown
print(f"Down payment {Price  }")
