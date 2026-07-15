from odoo import fields, models


class ORMDepartment(models.Model):
    _name = "orm.department"
    _description = "ORM Department"
    _rec_name = "name"
    _order = "name"

    name = fields.Char(
        string="Department Name",
        required=True,
    )

    employee_ids = fields.One2many(
        "orm.employee",
        "department_id",
        string="Employees",
    )