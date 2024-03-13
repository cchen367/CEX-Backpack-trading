import random

def calculate_ema(data, period):
    ema_values = []
    alpha = 2 / (period + 1)
    ema = data[0]  # Initial EMA value is the first data point

    for value in data:
        ema = alpha * value + (1 - alpha) * ema
        ema_values.append(ema)

    return ema_values

# Define the base price of Bitcoin
base_price = 45000  # You can adjust this value as needed

# Generate a list of 1000 slightly varying Bitcoin prices
bitcoin_prices = [base_price + round(random.uniform(-500, 500), 2) for _ in range(1000)]

# Printing the first few prices as an example
# print("First 10 Bitcoin prices:")
# for price in bitcoin_prices[:10]:
    # print("{:.2f}".format(price))

my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
temp13=calculate_ema(my_list, 13)

# print(calculate_ema(my_list, 13))
# print("{:.2f}".format(calculate_ema(my_list, 34)))

# for num in temp13:
#     print("{:.2f}".format(num), end=" ")
#
# temp34 = calculate_ema(my_list, 34)
#
# print("\n")
#
# for num in temp34:
#     print("{:.2f}".format(num), end=" ")

# Now do it with bitcoin prices:
print("\nNow using bitcoin prices:")
# Define the base price of Bitcoin
base_price = 45000  # You can adjust this value as needed

# Generate a list of 1000 slightly varying Bitcoin prices
bitcoin_prices = [base_price + round(random.uniform(-500, 500), 2) for _ in range(1000)]
bit13=calculate_ema(bitcoin_prices, 13)

for num in bit13:
    print("{:.2f}".format(num), end=" ")

bit34 = calculate_ema(bitcoin_prices, 34)

print("\n")

for num in bit34:
    print("{:.2f}".format(num), end=" ")