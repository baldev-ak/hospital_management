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
    website = fields.Char(string='Website')
    branch_ids = fields.One2many(comodel_name="hospital.branch", inverse_name="hospital_id", string='Branches')
    no_of_branch = fields.Integer(compute='_compute_count_branch', string='Total Branches')
    no_of_doctors = fields.Integer(compute='_compute_count_doctor', string='Total Doctors')
    no_of_patients = fields.Integer(compute='_compute_count_patients', string='Total Patients')
    doctor_ids = fields.One2many(comodel_name="hospital.doctor", inverse_name="hospital_id", string='Doctors')
    patient_ids = fields.One2many(comodel_name="hospital.patient", inverse_name="hospital_id", string='Patients')
    
    # def create(self,vals):
    #     res = super(Hospital,self).create(vals)
    #     res.branch_ids.name = res.branch_ids.hospital_id.name + " " + res.branch_ids.country_id.name 
    #     return res

    def _compute_count_patients(self):
        # print(self,"---------self-----------")
        for rec in self:
            patients = self.env['hospital.patient'].search_count([('hospital_id','=',rec.id)])
            rec.no_of_patients = patients

    def _compute_count_doctor(self):
        # print(self,"---------self-----------")
        for rec in self:
            doctors = self.env['hospital.doctor'].search_count([('hospital_id','=',rec.id)])
            rec.no_of_doctors = doctors

    def _compute_count_branch(self):
        # print(self,"---------self-----------")
        for rec in self:
            branch = self.env['hospital.branch'].search_count([('hospital_id','=',rec.id)])
            rec.no_of_branch = branch

    def action_branch(self):
        return {
        'type': 'ir.actions.act_window',
        'name':'Branches',
        'res_model':'hospital.branch',
        'domain':[('hospital_id','=',self.id)],
        'view_mode': 'tree,form',
        'target':'new'
        }

    def action_doctor(self):
        return {
        'type': 'ir.actions.act_window',
        'name':'Doctors',
        'res_model':'hospital.doctor',
        'domain':[('hospital_id','=',self.id)],
        'view_mode': 'tree,form',
        'target':'current'
        }
        
    def action_patient(self):
        return {
        'type': 'ir.actions.act_window',
        'name':'Patients',
        'res_model':'hospital.patient',
        'domain':[('hospital_id','=',self.id)],
        'view_mode': 'tree,form',
        'target':'current'
        }  

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
    no_of_department = fields.Integer(compute='_compute_count_branch_department', string='Total Departments')
    no_of_facilities = fields.Integer(compute='_compute_count_branch_facilities', string='Total Facilities')
    no_of_specialities = fields.Integer(compute='_compute_count_branch_specialities', string='Total Specialities')
    department_ids = fields.Many2many(comodel_name="hospital.departments", string= "Departments")
    specialities_ids = fields.Many2many(comodel_name="hospital.specialities", string='Specialities')
    status = fields.Selection([('open','Open 24 hours'),('closed','Closed')], string='Status')
    no_of_doctors = fields.Integer(compute='_compute_count_branch_doctor', string='Total Doctors')
    no_of_patients = fields.Integer(compute='_compute_count__branch_patients', string='Total Patients')
    doctor_ids = fields.One2many(comodel_name="hospital.doctor", inverse_name="branch_id", string='Doctors')
    patient_ids = fields.One2many(comodel_name="hospital.patient", inverse_name="branch_id", string='Patients')

    def _compute_count_branch_department(self):
        for rec in self:
            rec.no_of_department = 0
            result = len(rec.department_ids.ids)
            rec.no_of_department = result
    def _compute_count_branch_facilities(self):
        for rec in self:
            rec.no_of_facilities = 0
            result = len(rec.facilities_ids.ids)
            rec.no_of_facilities = result

    def _compute_count_branch_specialities(self):
        for rec in self:
            rec.no_of_specialities = 0
            result = len(rec.specialities_ids.ids)
            rec.no_of_specialities = result

    def _compute_count__branch_patients(self):
        # print(self,"---------self-----------")
        for rec in self:
            patients = self.env['hospital.patient'].search_count([('branch_id','=',rec.id)])
            rec.no_of_patients = patients

    def _compute_count_branch_doctor(self):
        # print(self,"---------self-----------")
        for rec in self:
            doctors = self.env['hospital.doctor'].search_count([('branch_id','=',rec.id)])
            rec.no_of_doctors = doctors

    def action_branch_department(self):
        print("\n\n\n\n-----------Test--------\n\n\n\n")
    def action_branch_facility(self):
        print("\n\n\n\n-----------Test1--------\n\n\n\n")
    def action_branch_speciality(self):
        print("\n\n\n\n-----------Test2--------\n\n\n\n")
    def action_branch_doctor(self):
        return {
        'type': 'ir.actions.act_window',
        'name':'Doctors',
        'res_model':'hospital.doctor',
        'domain':[('branch_id','=',self.id)],
        'view_mode': 'tree,form',
        'target':'current'
        }
        
    def action_branch_patient(self):
        return {
        'type': 'ir.actions.act_window',
        'name':'Patients',
        'res_model':'hospital.patient',
        'domain':[('branch_id','=',self.id)],
        'view_mode': 'tree,form',
        'target':'current'
        }  

    def count_status(self):
        print("\n\n\n------------Clicked----------------\n\n\n")

    @api.depends('date')
    def _compute_year(self):
        for rec in self:
            rec.year = 0
            if rec.date:
                openingdate = rec.date
                today = date.today()
                age = today.year - openingdate.year - ((today.month, today.day) < (openingdate.month, openingdate.day))
                rec.year = age

    # @api.model
    # def create(self,vals):
    #     res = super(HospitalBranch,self).create(vals)
    #     res.name=res.hospital_id.name + "-" + res.country_id.name
    #     return res

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
