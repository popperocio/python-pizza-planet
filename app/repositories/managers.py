from typing import Any, List, Optional, Sequence

from sqlalchemy.sql import text, column, func, desc

from .models import Beverage, Ingredient, Order, OrderDetail, Size, db
from .serializers import (IngredientSerializer, OrderSerializer,
                          SizeSerializer, BeverageSerializer, ma)
import calendar

class BaseManager:
    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    session = db.session

    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_by_id(cls, _id: Any):
        entry = cls.model.query.get(_id)
        return cls.serializer().dump(entry)

    @classmethod
    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.session.add(new_entry)
        cls.session.commit()
        return serializer.dump(new_entry)

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        cls.session.query(cls.model).filter_by(_id=_id).update(new_values)
        cls.session.commit()
        return cls.get_by_id(_id)


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(cls, order_data: dict, ingredients: List[Ingredient], beverages: List[Beverage]):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        cls.session.add_all(
                            OrderDetail(
                                    order_id=new_order._id,
                                    ingredient_id=ingredient._id,
                                    ingredient_price=ingredient.price,
                                    beverage_id=beverage._id,
                                    beverage_price=beverage.price
                                    )
                                    for ingredient in ingredients
                                for beverage in beverages)
        cls.session.commit()
        return cls.serializer().dump(new_order)

    @classmethod
    def update(cls):
        raise NotImplementedError(f'Method not suported for {cls.__name__}')


class IndexManager(BaseManager):

    @classmethod
    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()


class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []


class ReportManager(BaseManager):
    order = Order
    order_detail = OrderDetail
    ingredient = Ingredient

    @classmethod
    def get_reports(cls):
        report = {}
        best_customers = []
        most_requested_ingredient = []
        date_with_most_revenue = []
        customers = cls.session.query(
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
        
        ingredients = db.session.query(
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

        months= cls.session.query(
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