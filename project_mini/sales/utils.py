from io import BytesIO
from django.http import FileResponse
from reportlab.pdfgen import canvas
from .models import Invoice

def generate_invoice_pdf(invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(100, 750, f"Invoice #{invoice.id}")
    p.drawString(100, 730, f"Total: ${invoice.total_amount}")

    p.showPage()
    p.save()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename=f'invoice_{invoice.id}.pdf')
