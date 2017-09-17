# -*- coding: utf-8 -*-
from odoo import http

# class TiendoOptimalpurchase(http.Controller):
#     @http.route('/tiendo_optimalpurchase/tiendo_optimalpurchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tiendo_optimalpurchase/tiendo_optimalpurchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tiendo_optimalpurchase.listing', {
#             'root': '/tiendo_optimalpurchase/tiendo_optimalpurchase',
#             'objects': http.request.env['tiendo_optimalpurchase.tiendo_optimalpurchase'].search([]),
#         })

#     @http.route('/tiendo_optimalpurchase/tiendo_optimalpurchase/objects/<model("tiendo_optimalpurchase.tiendo_optimalpurchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tiendo_optimalpurchase.object', {
#             'object': obj
#         })