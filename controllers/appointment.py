from datetime import date
from odoo import http
from odoo.http import request


class ServiceRequest(http.Controller):
    @http.route(['/appointment'], type="http", auth="public", website=True)
    def appointment(self,**kw):
        return http.request.render('medical.appointment_website_form', {})