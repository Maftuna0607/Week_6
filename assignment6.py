def calculate_product_revenue(product_tuple):
    id, category, price, units_sold = product_tuple
    return price * units_sold


def find_top_revenue_product(products):
    top_revenue = 0
    top_product = ""
    for product in products:
        revenue = calculate_product_revenue(product)
        if revenue > top_revenue:
            top_revenue = revenue
            top_product = product[0]
        elif revenue == top_revenue:
            if product[0] < top_product:
                top_product = product[0]
    return top_product


def get_products_in_category(products, category_name):
    new = []
    for product in products:
        if product[1] == category_name:
            new.append(product[0])
    new.sort()
    return new


def get_category_sales_summary(products):
    categories = []
    totals = [] 
    for product in products:
        category = product[1]
        sold = product[3]
        if category not in categories:
            categories.append(category)
            totals.append(sold)
        else:
            index = categories.index(category)
            totals[index] += sold
    summary = []
    for i in range(len(categories)):
        summary.append((categories[i], totals[i]))
    summary.sort()
    return summary


def analyze_products(products, target_category):
    top = find_top_revenue_product(products)
    category_products = get_products_in_category(products, target_category)
    summary = get_category_sales_summary(products)

    if not category_products:
        print(f"Warning: No products found in category '{target_category}'.")

    return (top, category_products, summary)

products = [
    ('P101', 'Electronics', 799.99, 150),
    ('P205', 'Books', 24.50, 500),
    ('P102', 'Electronics', 499.50, 200),
    ('P301', 'Home Goods', 120.00, 800),
    ('P206', 'Books', 19.99, 650)
]
print(f"Available categories: Books, Electronics, Home Goods")
target_category= input("Enter the category name: ")
result = analyze_products(products, target_category)
print(result)













