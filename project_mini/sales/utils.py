# sales/utils.py
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.shortcuts import get_object_or_404
from .models import Invoice

def generate_invoice_pdf(invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{invoice.id}.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, f"Invoice ID: {invoice.id}")
    p.drawString(100, 730, f"Order ID: {invoice.order.id}")
    p.drawString(100, 710, f"Total Amount: ${invoice.total_amount}")
    p.drawString(100, 690, f"Date: {invoice.created_at.strftime('%Y-%m-%d')}")

    p.showPage()
    p.save()
    return response
