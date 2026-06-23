def stock_span(price):

    n = len(price)
    span = [0] * n
    stack = []

    for i in range(n):

        while stack and price[i] >= price[stack[-1]]:
            stack.pop()

        if not stack:
            span[i] = i + 1
        
        else:
            span[i] = i - stack[-1]
        
        stack.append(i)

    return span

price = [100, 80, 60, 70, 60, 75, 85]
print(stock_span(price))