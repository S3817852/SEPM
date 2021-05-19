from django.shortcuts import render

# Create your views here.
def bill_receipts(request):
    return render(request, 'BillAndReceipts/bill_receipts.html')

def bill_receipts_add(request):
    return render(request, 'BillAndReceipts/O_billreceipt_new.html')

def bill_receipts_paid(request):
    return render(request, 'BillAndReceipts/O_billreceipt_allpaid.html')

def bill_receipts_processing(request):
    return render(request, 'BillAndReceipts/O_billreceipt_paymentinprogress.html')