import frappe
from frappe.website.path_resolver import resolve_path as original_resolve_path

def path_resolver(path: str):
    # frappe.redirect("https://google.com")
    if frappe.db.exists("Short Link", path):
        short_link = frappe.db.get_value("Short Link", {"short_link": path}, ["destination_url", "short_link"], as_dict=True)
        click = frappe.new_doc("Short Link Click")
        request_headers = frappe.request.headers
        click.ip = request_headers.get("X-Forwarded-For")
        click.user_agent = request_headers.get("User-Agent")
        click.referrer = request_headers.get("Referer")
        # # breakpoint()
        print(frappe.request.headers)
        click.link = short_link.short_link
        click.insert()
        frappe.db.commit()
        frappe.redirect(short_link.destination_url)

    return original_resolve_path(path)  