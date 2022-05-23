# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class odooTutorial(models.Model):
    _name = 'odoo.tutorial'
    _description = 'Odoo Tutorial'

    name = fields.Char(string='Tutorial Name', required=True)
    number_of_videos = fields.Integer(string='Number of Videos', required=True)

