from django.shortcuts import render

# Create your views here.
def bill_receipts(request):
    return render(request, 'BillAndReceipts/bill_receipts.html')