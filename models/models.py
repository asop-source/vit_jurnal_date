# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class AccountMoveDate(models.Model):
	_inherit ='account.move'


	@api.model
	def create(self, vals):
		move = super(AccountMoveDate, self.with_context(check_move_validity=False, partner_id=vals.get('partner_id'))).create(vals)
		move.assert_balanced()
		move._create_validate()
		return move

	@api.multi
	def _create_validate(self):
		obj_picking = self.env['stock.picking'].search([('name','=',self.ref)])
		if self.ref == obj_picking.name:
			self.write({'date' : obj_picking.scheduled_date}) 
		else :
			self.date = self.date