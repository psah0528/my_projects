from odoo import fields, models


class ORMSkill(models.Model):
    _name = "orm.skill"
    _description = "ORM Skill"
    _rec_name = "name"
    _order = "name"

    name = fields.Char(
        string="Skill",
        required=True,
    )

    employee_ids = fields.Many2many(
        "orm.employee",
        string="Employees",
    )