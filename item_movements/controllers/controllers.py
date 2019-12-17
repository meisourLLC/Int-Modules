# -*- coding: utf-8 -*-
from odoo import http

# class ItemMovements(http.Controller):
#     @http.route('/item_movements/item_movements/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/item_movements/item_movements/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('item_movements.listing', {
#             'root': '/item_movements/item_movements',
#             'objects': http.request.env['item_movements.item_movements'].search([]),
#         })

#     @http.route('/item_movements/item_movements/objects/<model("item_movements.item_movements"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('item_movements.object', {
#             'object': obj
#         })