import frappe
from frappe.website.path_resolver import resolve_path as original_resolve_path

def path_resolver(path: str):
    # frappe.redirect("https://google.com")
    if frappe.db.exists("Short Link", path):
        destination = frappe.db.get_value("Short Link", {"short_link": path}, "destination_url")
        frappe.redirect(destination)

    return original_resolve_path(path)  