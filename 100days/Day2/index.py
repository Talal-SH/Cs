#from tip calculator to -->
print('calculate board')
board_raw_price = int(input("board's raw price? per piece\n"))
melamine__raw_price = int(input("melamine's raw price? per board/sheet\n"))
board_selling_price = int(input("At what price would you sell the board for?\n"))
profit = board_selling_price - board_raw_price
print(f'Profit with nothing into consedaration: {profit}SAR')

ten_of_board =board_raw_price * (10/100)
fifteen_of_bord = board_raw_price * (15/100)
five_of_melamine = melamine__raw_price * (5/100)
materials_transport_cost = fifteen_of_bord + five_of_melamine
materials_energylabor_cost = ten_of_board + five_of_melamine

a = fifteen_of_bord + five_of_melamine
b = ten_of_board + five_of_melamine
print(f'With consederation of their raw selling price:\nMaterials transport cost:\n  15%% of Board price due to a higher wieght({fifteen_of_bord}) + 5%% of melamine price due to a lower wieght({five_of_melamine})')
print(f"                             {fifteen_of_bord} + {five_of_melamine} =  {a} SAR")
print(f'Material Energy and labol cost:\n  10%% of Board price due to a higher wieght({ten_of_board}) + 5%% of melamine price due to a lower wieght({five_of_melamine})')
print(f"                             {ten_of_board} + {five_of_melamine}=  {b} SAR")

total_expenises = a + b + board_raw_price + melamine__raw_price
net_profit = profit - total_expenises


print(f'Net profit: profit= {profit} - expinses= {total_expenises} = {net_profit} SAR')