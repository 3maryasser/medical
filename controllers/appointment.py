from datetime import date
from odoo import http
from odoo.http import request


class ServiceRequest(http.Controller):
    @http.route(['/appointment'], type="http", auth="public", website=True)
    def appointment(self,**kw):
        doctor = request.env["hr.employee"].sudo().search([])
        values = {
            'doc_names': doctor
        }
        return http.request.render('medical.appointment_website_form', values)
    
    @http.route(['/appointment/form'] ,methods=['POST','GET'], type='http',auth="public",website="True",csrf=False)
    def submit_form(self,**kw):
        if kw:
            patient = request.env['res.partner'].sudo().create({
                'name': kw.get('patient_name')})
            patient_name = kw.get('patient_name')
            # vals = {
            #     'patient_name': patient,
            # }
            # appointment = request.env['medical.appointment'].sudo().create(vals)
            

            