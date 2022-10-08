# -*- coding: utf-8 -*-
# from odoo import http


# class DragonBase(http.Controller):
#     @http.route('/dragon_base/dragon_base', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dragon_base/dragon_base/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dragon_base.listing', {
#             'root': '/dragon_base/dragon_base',
#             'objects': http.request.env['dragon_base.dragon_base'].search([]),
#         })

#     @http.route('/dragon_base/dragon_base/objects/<model("dragon_base.dragon_base"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dragon_base.object', {
#             'object': obj
#         })
