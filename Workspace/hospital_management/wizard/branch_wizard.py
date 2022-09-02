from odoo import fields,models,api
from datetime import date

class BranchWizard(models.TransientModel):
    _name = "branch.wizard"
    _description = "Branch Wizard"

    name = fields.Char(string = "Name")
    gender = fields.Selection([('male','Male'),('female','Female')], string = "Gender")
    phone_number = fields.Char(string='Phone No.')
    email_address = fields.Char(string='Email')
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string = 'Age', compute = '_compute_age', store = True)
    blood_group = fields.Selection([('a+','A+'),('a-','A-'),('b+','B+'),('b-','B-')], string = "Blood Group")
    hospital_id = fields.Many2one(comodel_name="hospital.hospital", string='Hospital')
    branch_id = fields.Many2one(comodel_name="hospital.branch", inverse_name="doctor_ids", string='Branch')
    doctor_id = fields.Many2one(comodel_name="hospital.doctor", string='Responsible Dr.')

    # @api.model
    # def create(self,vals):
    #     res = super(BranchWizard, self).create(vals)
    #     if vals.get('name', False):
    #         self.env['hospital.patient'].create({
    #             'name': res.name,
    #         })
    #     print("-------------",res)
        
    #     return res

    # def button_confirm(self):
    #     doc = self.env['hospital.doctor'].search([('id','in',self.doctor_id.ids)])
    #     hospital = self.env['hospital.hospital'].search([('id','in',self.hospital_id.ids)])
    #     branch = self.env['hospital.branch'].search([('id','in',self.branch_id.ids)])
    #     patient = self.env['hospital.patient'].search([('name','=',self.name)])

    #     for rec in patient:
    #         print("\n\n1------------\n",rec)

    #     if self.name and self.doctor_id:
    #         print("Found")
    #         self.env['hospital.patient'].create({
    #             'name': self.name,
    #             'gender': self.gender,
    #             'phone_number': self.phone_number,
    #             'email_address': self.email_address,
    #             'date_of_birth': self.date_of_birth,
    #             'age': self.age,
    #             'blood_group': self.blood_group,
    #             'hospital_id': hospital.id,
    #             'branch_id': branch.id,
    #             'doctor_id': doc.id
    #             })
            
    # @api.depends('date_of_birth')
    # def _compute_age(self):
    #     for rec in self:
    #         rec.age = 0
    #         if rec.date_of_birth:
    #             openingdate = rec.date_of_birth
    #             today = date.today()
    #             age = today.year - openingdate.year - ((today.month, today.day) < (openingdate.month, openingdate.day))
    #             rec.age = age