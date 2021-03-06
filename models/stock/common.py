# -*- coding: utf-8 -*-
# © 2018 Halltic eSolutions S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class AmazonShippingTemplate(models.Model):
    _name = 'amazon.shipping.template'

    name = fields.Char(required=True)
    backend_id = fields.Many2one('amazon.backend', required=False)
    marketplace_id = fields.Many2one('amazon.config.marketplace', required=True)
    is_default = fields.Boolean('Is the default template', default=False)
    delivery_standar_carrier_ids = fields.Many2many(comodel_name='delivery.carrier',
                                                    string='Delivery carrier associated', )
    delivery_expedited_carrier_ids = fields.Many2many(comodel_name='delivery.carrier',
                                                      string='Delivery carrier associated', )
