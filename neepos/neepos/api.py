import frappe

@frappe.whitelist()
def get_total_sales_before_tax():
    # Query total sales before tax from the Sales Invoice table
    total_sales_before_tax = frappe.db.sql("""
        SELECT SUM(base_net_total) AS total_sales_before_tax
        FROM `tabSales Invoice`
        WHERE docstatus = 1
    """, as_dict=True)

    return total_sales_before_tax[0]['total_sales_before_tax'] if total_sales_before_tax else 0

@frappe.whitelist()
def get_sales_tax_collected():
    # Query total sales tax collected from the Sales Invoice table
    total_sales_tax_collected = frappe.db.sql("""
        SELECT SUM(base_total_taxes_and_charges) AS total_sales_tax_collected
        FROM `tabSales Invoice`      
        WHERE docstatus = 1
    """, as_dict=True)

    return total_sales_tax_collected[0]['total_sales_tax_collected'] if total_sales_tax_collected else 0
@frappe.whitelist()
def get_average_transaction_value():
    # Query total transaction value and number of transactions from the Sales Invoice table
    result = frappe.db.sql("""
        SELECT SUM(base_grand_total) AS total_transaction_value, COUNT(name) AS number_of_transactions
        FROM `tabSales Invoice`
        WHERE docstatus = 1
    """, as_dict=True)

    if result and result[0]['number_of_transactions'] > 0:    
        total_transaction_value = result[0]['total_transaction_value']
        number_of_transactions = result[0]['number_of_transactions']
        average_transaction_value = total_transaction_value / number_of_transactions
        return average_transaction_value
    else:
        return 0

@frappe.whitelist()
def get_total_items_sold():
    # Query total items sold from the Sales Invoice Item table
    total_items_sold = frappe.db.sql("""
        SELECT SUM(qty) AS total_items_sold
        FROM `tabSales Invoice Item`
        JOIN `tabSales Invoice` ON `tabSales Invoice Item`.`parent` = `tabSales Invoice`.`name`
        WHERE `tabSales Invoice`.`docstatus` = 1    
    """, as_dict=True)

    return total_items_sold[0]['total_items_sold'] if total_items_sold else 0
@frappe.whitelist()
def get_gross_earnings():
    # Query total gross earnings from Sales Invoice table
    gross_earnings = frappe.db.sql("""
        SELECT SUM(base_net_total) AS total_net_earnings
        FROM `tabSales Invoice`
        WHERE docstatus = 1
    """, as_dict=True)

    return gross_earnings[0]['total_net_earnings'] if gross_earnings else 0
    