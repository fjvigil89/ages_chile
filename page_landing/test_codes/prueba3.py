# -*- coding: utf-8 -*-
import odoorpc as rpc

url = "https://9999.geztion.pro"
db = "9999"
user = "jramonholy@gmail.com"
pwd = "Maranatha.2021++"

odoo = rpc.ODOO(url, port='')
odoo.login(db, user, pwd)

order = odoo.env['sale.order']
domain = []  # doamin escribir declaraciones condicionales
data = order.search_read(domain)  # ¿Aquí podemos intentar llamar al método personalizado en el modelo? Teóricamente factible
print (data)