import os
import sys
import django

# Adicione o diretório do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Defina as configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# Carregue as configurações do Django
django.setup()

from schemas.models import Product

def create():
    # Criar um novo produto
    product1 = Product(id = "2", name="Shirt", price=29.99)
    product1.save()

def list():
    # Listar todos os produtos
    products = Product.objects.all()
    for product in products:
        print(f'{product.id} || {product.name} || {product.price}')

def update():
    # Atualizar um produto existente (se existir)
    product2 = Product.objects.filter(id=1).first()
    if product2:
        product2.price = 39.99
        product2.save()
        
def delete():
    # Excluir um produto (se existir)
    product3 = Product.objects.filter(id=1).first()
    if product3:
        product3.delete()

list()