subscribers = {
    "haniya@gmail.com",
    "ayman@gmail.com",
    "anah@gmail.com",
    "Sanu@gmail.com"
}

customers = {
    "ayman@gmail.com",
    "shifa@gmail.com",
    "anah@gmail.com",
    "fatima@gmail.com"
}

subscribers_wo_purchase = subscribers - customers
customers_wo_subscription = customers - subscribers

print("Subscribers without purchase:", subscribers_wo_purchase)
print("Customers without subscription:", customers_wo_subscription)