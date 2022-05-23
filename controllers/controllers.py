# -*- coding: utf-8 -*-
# from odoo import http


# class PopupMessageBackend(http.Controller):
#     @http.route('/popup_message_backend/popup_message_backend/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/popup_message_backend/popup_message_backend/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('popup_message_backend.listing', {
#             'root': '/popup_message_backend/popup_message_backend',
#             'objects': http.request.env['popup_message_backend.popup_message_backend'].search([]),
#         })

#     @http.route('/popup_message_backend/popup_message_backend/objects/<model("popup_message_backend.popup_message_backend"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('popup_message_backend.object', {
#             'object': obj
#         })
