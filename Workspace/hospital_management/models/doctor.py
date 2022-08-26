from odoo import fields,models,api

class Doctor(models.Model):
	_name = "hospital.doctor"
	_description = "Doctor"

	name = fields.Char(string = 'Name')
	gender = fields.Selection([('male','Male'),('female','Female')], string = "Gender")
	phone_number = fields.Char(string='Phone No.')
	email_address = fields.Char(string='Email')
	date_of_birth = fields.Date(string='Date of Birth')
	date_of_joining = fields.Date(string='Date of Joining')
	hospital_id = fields.Many2one(comodel_name="hospital.hospital", string='Hospital')
	branch_ids = fields.Many2one(comodel_name="hospital.branch", inverse_name="doctor_ids", string='Branch')
	speciality_id = fields.Many2one(comodel_name="hospital.specialities", string='Specialities')
	degree_ids = fields.Many2many(comodel_name = "doctor.degree", string = "Degree")

class Degree(models.Model):
	_name = "doctor.degree"
	_description = "Doctor Degrees"

	name = fields.Char(string = "Degree")