from odoo import api, fields, models
from odoo.exceptions import UserError


class ORMEmployee(models.Model):
    _name = "orm.employee"
    _description = "ORM Employee"
    _rec_name = "name"
    _order = "id desc"

    # -------------------------
    # General Information
    # -------------------------

    name = fields.Char(
        string="Employee Name",
        required=True,
    )

    employee_code = fields.Char(
        string="Employee Code",
        readonly=True,
        copy=False,
    )

    email = fields.Char(
        string="Email",
    )

    phone = fields.Char(
        string="Phone",
    )

    mobile = fields.Char(
        string="Mobile",
    )

    # -------------------------
    # Basic Fields
    # -------------------------

    short_bio = fields.Char(
        string="Short Bio",
    )

    address = fields.Text(
        string="Address",
    )

    description = fields.Html(
        string="Description",
    )

    # -------------------------
    # Numeric Fields
    # -------------------------

    age = fields.Integer(
        string="Age",
    )

    experience = fields.Float(
        string="Experience (Years)",
    )

    currency_id = fields.Many2one(
        "res.currency",
        string="Currency",
        default=lambda self: self.env.company.currency_id,
    )

    salary = fields.Monetary(
        string="Salary",
        currency_field="currency_id",
    )

    # -------------------------
    # Date Fields
    # -------------------------

    date_of_birth = fields.Date(
        string="Date of Birth",
    )

    joining_datetime = fields.Datetime(
        string="Joining Date & Time",
    )

    # -------------------------
    # Selection Fields
    # -------------------------

    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ],
        string="Gender",
    )

    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("done", "Done"),
        ],
        string="Status",
        default="draft",
    )

    # -------------------------
    # Boolean Fields
    # -------------------------

    active_employee = fields.Boolean(
        string="Active Employee",
        default=True,
    )

    is_manager = fields.Boolean(
        string="Is Manager",
    )

    # -------------------------
    # Binary Fields
    # -------------------------

    photo = fields.Image(
        string="Employee Photo",
    )

    resume = fields.Binary(
        string="Resume",
        attachment=True,
    )

    resume_filename = fields.Char(
        string="Resume File Name",
    )

    # -------------------------
    # Relationships
    # -------------------------

    department_id = fields.Many2one(
        "orm.department",
        string="Department",
        ondelete="restrict",
    )

    # -------------------------
    # Many2many
    # -------------------------

    skill_ids = fields.Many2many(
        "orm.skill",
        string="Skills",
    )

    # =====================================================
    # ORM METHODS
    # =====================================================
 # CREATE METHODS
    @api.model_create_multi
    def create(self, vals_list):

        for vals in vals_list:

            vals["employee_code"] = self.env[
                "ir.sequence"
            ].next_by_code("orm.employee.sequence") or "New"

            if not vals.get("status"):
                vals["status"] = "draft"

        records = super().create(vals_list)

        for rec in records:
            print("Employee Created :", rec.name)

        return records
    
 # search btn  METHODS
    
    def action_search_employees(self):
        employees = self.search([
        ("active_employee", "=", True)
    ])
        print("========== SEARCH RESULT ==========")
        for emp in employees:
             print(emp.name)

    print("===================================")

    
 # WRITE  METHODS
    def write(self, vals):

     if "name" in vals:
        vals["name"] = vals["name"].title()

     if "email" in vals and vals["email"]:
        vals["email"] = vals["email"].lower()

     return super().write(vals)
    

# Search METHOD
    def action_search_employees(self):
     self.ensure_one()

     if not self.department_id:
        raise UserError("Please select a department first.")

     employees = self.search([
        ("department_id", "=", self.department_id.id)
    ])

     return {
        "type": "ir.actions.act_window",
        "name": "Department Employees",
        "res_model": "orm.employee",
        "view_mode": "list,form",
        "domain": [("id", "in", employees.ids)],
        "target": "current",
    }
    
# BROWSE METHODS    
    def action_browse_employee(self):

     employee = self.browse(self.id)
     raise UserError(
        f"""Employee Details

Name : {employee.name}

Email : {employee.email or '-'}

Department : {employee.department_id.name or '-'}

Employee Code : {employee.employee_code}
"""
    )
# COPY METHOD 

    def copy(self, default=None):

     default = dict(default or {})

     default["employee_code"] = self._generate_employee_code()

     return super().copy(default)

# generate emp code
    def _generate_employee_code(self):

     last = self.search([], order="id desc", limit=1)

     if last and last.employee_code:

        try:
            number = int(last.employee_code.replace("EMP-", ""))
        except:
            number = 0
     else:
        number = 0

     return f"EMP-{number + 1:04d}"





    
    

    
