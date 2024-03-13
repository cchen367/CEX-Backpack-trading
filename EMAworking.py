import random
def calculate_ema(data, period):
    ema_values = []
    alpha = 2 / (period + 1)
    ema = data[0]  # Initial EMA value is the first data point

    for value in data:
        ema = alpha * value + (1 - alpha) * ema
        ema_values.append(ema)

    return ema_values

base_price = 45000  # You can adjust this value as needed

# Generate a list of 1000 slightly varying Bitcoin prices
bitcoin_prices = [base_price + round(random.uniform(-500, 500), 2) for _ in range(1000)]

print("\nGenerated random bitcoin prices, " + str((len(bitcoin_prices))) + " values:\n", bitcoin_prices)

# Generate a list of bitcoin prices after EMA 13 calculation
bit13 = calculate_ema(bitcoin_prices, 13)

print("\nEMA 13, " + str((len(bit13))) + " values:")

for num in bit13:
    print("{:.2f}".format(num), end=" ")

# Generate a list of bitcoin prices after EMA 34 calculation
bit34 = calculate_ema(bitcoin_prices, 34)

print("\n\nEMA 34, " + str((len(bit34))) + " values:")
for num in bit34:
    print("{:.2f}".format(num), end=" ")

# Find all points of intersection based on the given conditions
buy_intersections = []
sell_intersections = []

for i in range(1, len(bit13)-1):
    if bit13[i] >= bit34[i + 1] and bit34[i] <= bit13[i + 1]:
        sell_intersections.append((bit13[i], bit34[i]))

    if bit13[i] <= bit34[i + 1] and bit34[i] >= bit13[i + 1]:
        buy_intersections.append((bit13[i], bit34[i]))

print("\n\nBuy intersections:")
for tpl in buy_intersections:
    rounded_tpl = tuple(round(value, 2) for value in tpl)
    print(rounded_tpl, end=" ")

print("\nLength of buy intersections is " + str((len(buy_intersections))))

print("\nSell intersections:")
for tpl in sell_intersections:
    rounded_tpl = tuple(round(value, 2) for value in tpl)
    print(rounded_tpl, end=" ")

print("\nLength of sell intersections is " + str((len(sell_intersections))))