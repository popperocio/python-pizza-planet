from .report_creator import ReportCreator
from .models import db
from .models import Order, OrderDetail, Ingredient
from sqlalchemy.sql import func, desc
import calendar

class  ConcreteReport(ReportCreator):
    
    order = Order
    order_detail = OrderDetail
    ingredient = Ingredient
    
    def create_report(cls):
        session = db.session
        report = {}
        best_customers = []
        most_requested_ingredient = []
        date_with_most_revenue = []
        customers = session.query(
                                    cls.order.client_name,
                                    cls.order.client_dni,
                                    func.count(cls.order.client_dni).label('total_sales')
                                ).group_by(
                                    cls.order.client_dni
                                ).order_by(
                                    desc('total_sales')
                                ).limit(3).all()
        for customer in customers:
            best_customers.append(
                {'client_name': customer.client_name, 'total_sales': customer.total_sales})
        
        ingredients = session.query(
                                        cls.ingredient.name,
                                        func.count(cls.order_detail.ingredient_id).label('total_requests')
                                    ).join(
                                        cls.order_detail, cls.ingredient._id == cls.order_detail.ingredient_id
                                    ).group_by(
                                        cls.order_detail.ingredient_id
                                    ).order_by(
                                        desc('total_requests')
                                    ).limit(1)  
        for ingredient in ingredients:                                                       
            most_requested_ingredient.append(
                    {'name': ingredient.name, 'total_requests': ingredient.total_requests})

        months= session.query(
                                func.extract('month', cls.order.date).label('month'),
                                func.sum(cls.order.total_price).label('total_sales_revenue')
                                ).group_by(
                                    func.extract('month', cls.order.date)
                                ).order_by(
                                    func.sum(cls.order.total_price).desc()
                                ).all()
        if months:
            month_name = calendar.month_name[months[0].month]
            date_with_most_revenue.append({'month': month_name, 'total_sales_revenue': months[0].total_sales_revenue})
            
        report['best_customers'] = best_customers
        report['most_requested_ingredient'] = most_requested_ingredient
        report['date_with_most_revenue'] = date_with_most_revenue
        
        return report