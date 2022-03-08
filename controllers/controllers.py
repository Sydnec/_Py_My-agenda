# -*- coding: utf-8 -*-
# from odoo import http


# class TpOdoo(http.Controller):
#     @http.route('/tp_odoo/tp_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tp_odoo/tp_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tp_odoo.listing', {
#             'root': '/tp_odoo/tp_odoo',
#             'objects': http.request.env['tp_odoo.tp_odoo'].search([]),
#         })

#     @http.route('/tp_odoo/tp_odoo/objects/<model("tp_odoo.tp_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tp_odoo.object', {
#             'object': obj
#         })
