from flask import Blueprint, render_template

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route("/admin/login")
def admin_login():
    return render_template("authen/login.html")

@admin.route("/admin/register")
def admin_register():
    return render_template("authen/register.html")

@admin.route("/admin/forgot-password")
def admin_forgot_password():
    return render_template("authen/forgot_password.html")

@admin.route("/admin/legal/terms")
def admin_legal_terms():
    return render_template("policy/terms.html")





@admin.route("/admin/profile")
def admin_profile():
    return render_template("adm/profile.html")


@admin.route("/admin/posts")
def admin_posts():
    return render_template("adm/posts.html")

@admin.route("/admin/users")
def admin_users():
    return render_template("adm/users.html")























