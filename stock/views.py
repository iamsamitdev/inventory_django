from django.shortcuts import render, redirect

# Import Model Product
from .models import Product

# Read All Product
def index(request):
    # Read All Product
    products = Product.objects.all() # SELECT * FROM product

    return render(request, 'frontend/index.html', { 'products': products })

# Read One Product
def product_detail(request, id):
    # Read One Product
    product = Product.objects.get(id=id) # SELECT * FROM product WHERE id = id

    return render(request, 'frontend/product_detail.html', { 'product': product })

# Create Product
def product_create(request):
    # เช็คว่ามีการ submit form
    if request.method == 'POST':
        # รับค่าจากฟอร์ม
        product = Product(
            product_name=request.POST['product_name'],
            product_detail=request.POST['product_detail'],
            product_barcode=request.POST['product_barcode'],
            product_qty=request.POST['product_qty'],
            product_price=request.POST['product_price'],
            product_image=request.POST['product_image'],
            product_status=request.POST['product_status']
        )

        # Save product to database
        product.save()

        # Redirect to index page
        return redirect('/')
    else:
        return render(request, 'frontend/product_create.html')

# Delete Product
def product_delete(request, id):
    # Delete Product
    product = Product.objects.get(id=id) 
    product.delete()

    # Redirect to index page
    return redirect('/')