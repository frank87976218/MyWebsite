customer_spending={
    "小白" : 2000,
    "小黑" : 3000,
    "小黃" : 12000,
    "小綠" : 15000,
    "小灰" : 8000,
}

for i in customer_spending:
    if customer_spending[i] >= 10000:
        customer_spending[i] = "VIP"
    else:
        customer_spending[i] = "一般客戶"

print(customer_spending)
