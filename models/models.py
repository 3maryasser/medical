from odoo import api,models,fields



class Patient(models.Model):
    _inherit = "res.partner"
    desc = fields.Char()
    channel_ids = fields.Char()

    gender = fields.Selection([('male','Male'),('female','Female')])


class Doctor(models.Model):
    _inherit = "hr.employee"


class Appointment(models.Model):
    _name = "medical.appointment"
    name = fields.Char(string='Appointment Refrence',index=True,copy=True,required=True,readonly=True, default= 'New')
    patient = fields.Many2one('res.partner', string='Patient')
    doctor = fields.Many2one('hr.employee', string='Doctor')
    date = fields.Datetime()
    state = fields.Selection(selection=[("draft","Draft"),("on","On Session"),("done","Done")], default="draft")
    prescription = fields.Html(string='Prescription')
    
    def start_session(self):
        self.write({"state":"on"})

    def end_session(self):
        self.write({"state":"done"})
    
    @api.model
    def create(self,vals):
        if vals.get('name','New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('name.sequence') or 'New'
        return super(Appointment,self).create(vals)
    

