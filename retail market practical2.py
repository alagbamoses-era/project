stock = {'Sugar' :31, 'Bread (sliced)': 311, 'Bread (unsliced)': 229, 'Egg' : 545,
         'Three crown (tin)': 201, 'Peak milk (tin)':230, 'Peak milk (sachet)': 791,
         'Bournvita (sachet)': 611, 'Milo (tin)': 367, 'Peak milk (Large Sachet)':889,
         'Milo (Large Sachet)': 934, 'Bournvita (Large Sachet)': 758, 'Custard (small sachet)': 383,
         'Corn flakes (small sachet)':647, 'Golden morn (small sachet)': 121,
         'Detergent (small Wawu)': 198, 'Detergent (small Aerial)': 354, 'Detergent (Big Wawu)':323,
         'Detergent (Big Aerial)':222, 'Corn flakes (big sachet)': 341, 'Golden morn (Large sachet)': 458,
         'Sprite (small)': 134, 'Pepsi (small)': 674, 'Fanta (small)': 757, 'Lacasera (small)': 127,
         'Sprite (big)': 956, 'Pepsi (big)':374, 'Fanta (big)': 267, 'Lacasera (big)':786, 'Coke (big)':546 }

price= {'Sugar' :50, 'Bread (sliced)' :200, 'Bread (unsliced)': 150, 'Egg' : 50,
         'Three crown (tin)': 150, 'Peak milk (tin)':120, 'Peak milk (sachet)': 50,
         'Bournvita (sachet)': 50, 'Milo (tin)': 500, 'Peak milk (Large Sachet)':700,
         'Milo (Large Sachet)': 700, 'Bournvita (Large Sachet)': 100, 'Custard (small sachet)': 200,
         'Corn flakes (small sachet)':150, 'Golden morn (small sachet)': 100,
         'Detergent (small Wawu)': 120, 'Detergent (small Aerial)': 115, 'Detergent (Big Wawu)':200,
         'Detergent (Big Aerial)':250, 'Corn flakes (big sachet)': 750, 'Golden morn (Large sachet)': 650,
         'Sprite (small)': 80, 'Pepsi (small)': 80, 'Fanta (small)': 80, 'Lacasera (small)': 80,
         'Sprite (big)': 150, 'Pepsi (big)':150, 'Fanta (big)': 150, 'Lacasera (big)':150, 'Coke (big)':150 }
def set_price(item,n_price):
      try:
         price[item] = n_price
         print ('price changed successfully')
      except keyError:
         print('item does not exist')
      return    

d= set_price('Peak milk (tin)',130)
print(d)


def MoreItem(stock: n):
    n= int(input("How many items are newly bought"))
    TotalStock= stock[item] + n
    print("New Stock is   ", TotalStock)
    return
f = MoreItem('Sugar', 100)
print(f)

