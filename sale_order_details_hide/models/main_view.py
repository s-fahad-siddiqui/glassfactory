import datetime
from email.policy import default
from pyexpat import model
from re import U
from tokenize import String

from odoo import models, fields,api
from odoo.exceptions import UserError
import base64
import datetime
from ast import literal_eval
import time


class Sale_Order_details(models.Model):
    _inherit='sale.order'
    
    
class acount_move(models.Model):
    _inherit= 'account.move'

    
