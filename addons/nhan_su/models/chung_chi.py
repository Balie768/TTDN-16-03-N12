from odoo import models, fields

class ChungChi(models.Model):
    _name = 'chung_chi'
    _description = 'Chứng chỉ'

    ten_chung_chi = fields.Char(string='Tên chứng chỉ', required=True)
    nhan_vien_id = fields.Many2one(
        'nhan_vien',
        string='Nhân viên'
    )
    ngay_cap = fields.Date(string='Ngày cấp')
