# -*- coding: utf-8 -*-
from odoo import http

# class VitJurnalDate(http.Controller):
#     @http.route('/vit_jurnal_date/vit_jurnal_date/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_jurnal_date/vit_jurnal_date/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_jurnal_date.listing', {
#             'root': '/vit_jurnal_date/vit_jurnal_date',
#             'objects': http.request.env['vit_jurnal_date.vit_jurnal_date'].search([]),
#         })

#     @http.route('/vit_jurnal_date/vit_jurnal_date/objects/<model("vit_jurnal_date.vit_jurnal_date"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_jurnal_date.object', {
#             'object': obj
#         })