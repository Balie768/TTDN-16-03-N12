from odoo import models, fields


class PhongBan(models.Model):
    _name = 'phong_ban'
    _description = 'Phòng ban'
    _rec_name = 'ten_phong_ban'

    ma_dinh_danh = fields.Char("Mã định danh", required=True)
    ten_phong_ban = fields.Char("Tên phòng ban", required=True)

    nhan_vien_id = fields.One2many(
        'nhan_vien',
        'phong_ban_id',
        string="Danh sách nhân viên"
    )