"""
Return the most profit from stock quotes: Stock quotes are stored in an array in order of date. The stock profit is
the difference in prices in buying and selling stock. Each day, you can either buy one unit of stock, sell any number
of stock units you have already bought, or do nothing. Therefore, the most profit is the maximum difference of all pairs
in a sequence of stock prices.
"""


def most_profit_from_stock_quotes(stocks: list) -> int:
    """
    This function takes as an input an array of integers and returns an integer representing the profit.

    Example:
        (1) arr = [ 1, 2, 3, 4, 5, 6 ]  => buy at 1, 2, 3, 4, 5 and then sell all at 6.
            most_profit_from_stock_quotes(arr) => 15 = (6 - 1) + (6 - 2) + ... + (6 - 5)
    """

    most_profit = 0
    if max(stocks) == stocks[0]:
        print("Example 2")
        return 0
    if max(stocks) == stocks[-1]:
        for price in stocks:
            most_profit = most_profit + max(stocks) - price
        print("Example 1")
        return most_profit
    temp = stocks.copy()
    while len(temp) != 0:
        peak = max(temp)
        peak_i = temp.index(peak)
        for i in range(len(temp[:peak_i])):
            most_profit = most_profit + temp[peak_i] - temp[i]
        if temp[peak_i] != stocks[-1]:
            temp = temp[peak_i + 1:].copy()
        else:
            break
    print("Examples 3 & 4")
    return most_profit


# ----------------- TESTS -----------------

arr_1 = [1, 2, 3, 4, 5, 6]
print(most_profit_from_stock_quotes(arr_1))
# Expected Output: 15

arr_2 = [6, 5, 4, 3, 2, 1]
print(most_profit_from_stock_quotes(arr_2))
# Expected Output: 0

arr_3 = [1, 6, 5, 10, 8, 7]
print(most_profit_from_stock_quotes(arr_3))
# Expected Output: 18

arr_4 = [1, 2, 10, 3, 2, 7, 3, 2]
print(most_profit_from_stock_quotes(arr_4))
# Expected Output: 26
