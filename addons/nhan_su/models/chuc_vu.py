from odoo import models, fields

class ChucVu(models.Model):
    _name = 'chuc_vu'
    _description = 'Chức vụ'

    ma_chuc_vu = fields.Char(string='Mã chức vụ', required=True)
    ten_chuc_vu = fields.Char(string='Tên chức vụ', required=True)
    ghi_chu = fields.Text(string='Ghi chú')
