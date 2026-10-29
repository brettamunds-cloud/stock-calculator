#Version 2

#Version 1 calculations

stock_name = "Apple"
number_of_shares = 10
share_price = 150

total_cost = number_of_shares * share_price

# Version 2 additions
new_share_price = 175
current_value = new_share_price * number_of_shares
profit_or_loss = current_value - total_cost
percentage_return = (profit_or_loss / total_cost) * 100

print("Stock:", stock_name)
print("Number of shares:", number_of_shares)
print(f"Original price per share: ${share_price}")
print(f"Total investment cost: ${total_cost}")
print(f"New price per share: ${new_share_price}")
print(f"Current investment value: ${current_value}")
print(f"Profit or loss: ${profit_or_loss}")
print(f"Percentage return: {percentage_return:.2f}%")


