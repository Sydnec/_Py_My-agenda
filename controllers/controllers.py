# -*- coding: utf-8 -*-
# from odoo import http


# class TpOdoo(http.Controller):
#     @http.route('/my-agenda/my-agenda/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my-agenda/my-agenda/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my-agenda.listing', {
#             'root': '/my-agenda/my-agenda',
#             'objects': http.request.env['my-agenda.my-agenda'].search([]),
#         })

#     @http.route('/my-agenda/my-agenda/objects/<model("my-agenda.my-agenda"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my-agenda.object', {
#             'object': obj
#         })
