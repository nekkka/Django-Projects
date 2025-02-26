import csv
import os
from celery import shared_task
from django.utils.timezone import now
from django.conf import settings
from .models import AnalyticsReport
from trading.models import Order
from django.core.files import File
from reportlab.pdfgen import canvas

@shared_task
def generate_trading_report(user_id):
    file_name = f"trading_report_{now().strftime('%Y%m%d_%H%M%S')}.csv"
    file_path = os.path.join(settings.MEDIA_ROOT, 'reports', file_name)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'User', 'Type', 'Price', 'Quantity', 'Status', 'Created At'])
        for order in Order.objects.all():
            writer.writerow([order.id, order.user.username, order.order_type, order.price, order.quantity, order.status, order.created_at])

    report = AnalyticsReport.objects.create(
        report_type='trading',
        file=file_path,
        generated_by_id=user_id
    )

    return f"Report generated: {report.file.url}"


@shared_task
def generate_profit_loss_report(user_id):
    """Фоновая задача для генерации отчета о прибыли и убытках (PDF)"""
    file_name = f"profit_loss_report_{now().strftime('%Y%m%d_%H%M%S')}.pdf"
    file_path = os.path.join(settings.MEDIA_ROOT, 'reports', file_name)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    c = canvas.Canvas(file_path)
    c.drawString(100, 800, "Profit/Loss Report")
    
    total_revenue = sum(order.price * order.quantity for order in Order.objects.all())
    total_cost = sum(order.quantity * order.price * 0.7 for order in Order.objects.all())  # пусть себестоимость 70%
    profit_loss = total_revenue - total_cost

    c.drawString(100, 770, f"Total Revenue: {total_revenue}")
    c.drawString(100, 750, f"Total Cost: {total_cost}")
    c.drawString(100, 730, f"Profit/Loss: {profit_loss}")
    
    c.save()

    report = AnalyticsReport.objects.create(
        report_type='profit_loss',
        file=file_path,
        generated_by_id=user_id
    )

    return f"Report generated: {report.file.url}"
