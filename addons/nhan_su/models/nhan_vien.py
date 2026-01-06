from odoo import models, fields, api


class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Bảng chứa thông tin nhân viên'
    _rec_name = 'ho_ten'

    ma_dinh_danh = fields.Char(
        string="Mã nhân viên",
        readonly=True,
        copy=False,
        default='New'
    )

    ho_ten = fields.Char("Họ tên", required=True)
    ngay_sinh = fields.Date("Ngày sinh")
    que_quan = fields.Char("Quê quán")
    email = fields.Char("Email")
    so_dien_thoai = fields.Char("Số điện thoại")
    so_bhxh = fields.Char("Số BHXH")
    dia_chi = fields.Char("Địa chỉ")
    luong = fields.Float("Lương")

    phong_ban_id = fields.Many2one(
        'phong_ban',
        string='Phòng ban'
    )

    @api.model
    def create(self, vals):
        if vals.get('ma_dinh_danh', 'New') == 'New':
            vals['ma_dinh_danh'] = self.env['ir.sequence'].next_by_code(
                'nhan_vien.sequence'
            ) or 'NV00'
        return super(NhanVien, self).create(vals)
