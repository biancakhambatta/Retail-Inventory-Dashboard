from flask import Blueprint, jsonify, render_template
from models import db, SuperstoreProduct
from sqlalchemy import func

api_bp = Blueprint('api', __name__)

# Frontend Route
@api_bp.route('/')
def index():
    return render_template('index.html')

# API Endpoints
@api_bp.route('/api/products', methods=['GET'])
def get_products():
    products = SuperstoreProduct.query.all()
    return jsonify([{
        "id": p.id,
        "product_name": p.product_name,
        "sales": p.sales,
        "profit": p.profit
    } for p in products])

@api_bp.route('/api/analytics/summary', methods=['GET'])
def get_analytics_summary():
    total_sales = db.session.query(func.sum(SuperstoreProduct.sales)).scalar() or 0.0
    total_profit = db.session.query(func.sum(SuperstoreProduct.profit)).scalar() or 0.0
    total_items = db.session.query(func.count(SuperstoreProduct.id)).scalar() or 0
    
    avg_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0.0
    top_product = SuperstoreProduct.query.order_by(SuperstoreProduct.profit.desc()).first()
    
    return jsonify({
        "total_inventory_items": total_items,
        "total_sales": round(total_sales, 2),
        "total_profit": round(total_profit, 2),
        "overall_profit_margin_percent": round(avg_margin, 2),
        "highest_profit_product": {
            "product_name": top_product.product_name if top_product else None,
            "profit": top_product.profit if top_product else None
        }
    })