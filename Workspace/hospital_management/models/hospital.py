# from odoo import fields, models

# class Hospital(models.Model):
#   _name = "hospital.hospital"
#   _description = "Hospital Management"

#   name = fields.Char(string='Name')
#   country_id = fields.Many2one(comodel_name="res.country", string='Country')
#   branch_ids = fields.One2many(comodel_name="hospital.branch", inverse_name="hospital_id", string='Branches')
#   speciality_ids = fields.Many2many(comodel_name="hospital.speciality", string='Specialities')

# class HospitalBranch(models.Model):
#   _name = "hospital.branch"
#   _description = "Hospital Management"

#   name = fields.Char(string='Name')
#   country_id = fields.Many2one(comodel_name="res.country", string='Country')
#   hospital_id = fields.Many2one(comodel_name="hospital.hospital", string='Hospital')
#   speciality_ids = fields.Many2many(comodel_name="hospital.speciality", string='Specialities')

# class HospitalSpeciality(models.Model):
#   _name = "hospital.speciality"
#   _description = "Speciality"

#   name = fields.Char(string='Name')

from odoo import fields,models,api
from datetime import date

class Hospital(models.Model):
    _name = "hospital.hospital"
    _description = "Hospital Management"


    name=fields.Char(string='Name')
    # phone_number = fields.Char(string='Phone No.')
    # email_address = fields.Char(string='Email')
    website = fields.Char(string='Website')
    branch_ids = fields.One2many(comodel_name="hospital.branch", inverse_name="hospital_id", string='Branches')
    # country_id = fields.Many2one(comodel_name="res.country", string='Country')
    # specialities_ids = fields.Many2many(comodel_name="hospital.specialities", string="Specialities")
    # facilities_ids = fields.Many2many(comodel_name="hospital.facilities", string= "Facilities")
    # department_ids = fields.Many2many(comodel_name="hospital.departments", string= "Departments")

    # def create(self,vals):
    #     res = super(Hospital,self).create(vals)
    #     res.branch_ids.name = res.branch_ids.hospital_id.name + " " + res.branch_ids.country_id.name 
    #     return res

    # @api.model
    def unlink(self):
        for record in self:
            branch = self.env['hospital.branch'].search([('hospital_id','=',record.id)])
            print(branch,"-------------------rec------------")
            res = super(Hospital,self).unlink()
            branch.unlink()
            return res

class HospitalBranch(models.Model):
    _name = "hospital.branch"
    _description = "Hospital Management"

    name = fields.Char(string='Name')
    phone_number = fields.Char(string='Phone No.')
    email_address = fields.Char(string='Email')
    date = fields.Date(string='Date of Opening')
    year = fields.Integer(string = 'Year', compute = '_compute_year')
    facilities_ids = fields.Many2many(comodel_name="hospital.facilities", string= "Facilities")
    country_id = fields.Many2one(comodel_name="res.country", string='Country')
    hospital_id = fields.Many2one(comodel_name="hospital.hospital", string='Hospital')
    department_ids = fields.Many2many(comodel_name="hospital.departments", string= "Departments")
    specialities_ids = fields.Many2many(comodel_name="hospital.specialities", string='Specialities')

    
    
    @api.depends('date')
    def _compute_year(self):
        for rec in self:
            rec.year = 0
            if rec.date:
                openingdate = rec.date
                today = date.today()
                age = today.year - openingdate.year - ((today.month, today.day) < (openingdate.month, openingdate.day))
                rec.year = age

    @api.model
    def create(self,vals):
        res = super(HospitalBranch,self).create(vals)
        res.name=res.hospital_id.name + "-" + res.country_id.name
        return res


    # def unlink(self):
    #     """Override method to unlink hospital branches that is linked to Hospital"""
    #     for record in self:
    #         result = self.env['hospital.branch'].search([('bran','=',record.id)])
    #         print(hospital_references,"-------------hospital_references------\n\n")
    #         res = super(HospitalPatient,self).unlink()
    #         hospital_references.unlink()
    #         return res


    def _inverse_type(self):
        # rec.phone_number = 7
        for rec in self:
           print("-------------------",rec)

class HospitalSpecialities(models.Model):
    _name = "hospital.specialities"
    _description = "Hospital Specialities"
 
    name=fields.Char(string='Name')

class Facilities(models.Model):
    _name = "hospital.facilities"
    _description = "Hospital Facilities"

    name=fields.Char(string='Name')

class Departments(models.Model):
    _name = "hospital.departments"
    _description = "Hospital Departments"

    name=fields.Char(string='Name')
    # hospital_id = fields.One2many(comodel_name='hospital.hospital',inverse_name='department_ids' , string = 'Hospital')
