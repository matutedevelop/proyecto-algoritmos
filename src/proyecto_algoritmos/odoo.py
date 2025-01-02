import xmlrpc.client

url = 'https://your-odoo-instance.com'
db = 'your-database-name'
username = 'your-username'
password = 'your-password'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

def create_quotation(partner_id, product_id, quantity):
    quotation = {
        'partner_id': partner_id,
        'order_line': [(0, 0, {
            'product_id': product_id,
            'product_uom_qty': quantity,
        })]
    }
    quotation_id = models.execute_kw(db, uid, password, 'sale.order', 'create', [quotation])
    return quotation_id

# Example usage
partner_id = 1  # Replace with actual partner ID
product_id = 1  # Replace with actual product ID
quantity = 10   # Replace with actual quantity

quotation_id = create_quotation(partner_id, product_id, quantity)
print(f'Quotation created with ID: {quotation_id}')