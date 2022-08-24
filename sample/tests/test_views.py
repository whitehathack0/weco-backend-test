import json
import math

from django.db.models import Sum
from django.test import TestCase, Client
from sample.models import Order, OrderedItem


class ViewsTest(TestCase):

    def setup(self):
        order = Order.objects.create(name='Kumars_order')
        order.save()

        ordered_item1 = OrderedItem.objects.create(
            order_id = order,
            name='carrots',
            sku='ao;isdjfo23',
            count=1,
            unit_price=5.00)
        ordered_item1.save()
        ordered_item2 = OrderedItem.objects.create(
            order_id=order,
            name='beans',
            sku='234ojsfos',
            count=1,
            unit_price=2.00)
        ordered_item2.save()

        order2 = Order.objects.create(name='Scotts_order')
        order2.save()

        ordered_item3 = OrderedItem.objects.create(
            order_id=order2,
            name='fried',
            sku='asdfj899s',
            count=2,
            unit_price=1.00)
        ordered_item3.save()
        ordered_item4 = OrderedItem.objects.create(
            order_id=order2,
            name='fish',
            sku='89238hjshj',
            count=3,
            unit_price=5.00)
        ordered_item4.save()

    def test_initial_creation(self):
        self.setup()
        num_order = Order.objects.all().count()
        total_num_items = OrderedItem.objects.aggregate(count=Sum('count'))['count']
        self.assertIs(num_order, 2)
        self.assertIs(total_num_items, 7)

    def test_client_get(self):
        self.setup()
        c = Client()
        res = c.get('/api/v1/orders/')
        self.assertIs(len(json.loads(res.content)), 2)

    def test_client_post(self):
        c = Client()
        file = open('sample/tests/sample_data/sample_post_data.json')
        data = json.load(file)

        self.assertIs(Order.objects.all().count(), 0)
        self.assertIs(OrderedItem.objects.aggregate(count=Sum('count'))['count'], None)

        c.post('/api/v1/orders/', data=data, content_type='application/json')

        num_order = Order.objects.all().count()
        total_num_items = OrderedItem.objects.aggregate(count=Sum('count'))['count']
        self.assertIs(num_order, 2)
        self.assertIs(total_num_items, 6)

    def test_client_stats(self):
        self.setup()
        c = Client()
        res = c.get('/api/v1/orderstats/')

        self.assertIs(int(json.loads(res.content)['order_count']), 2)
        self.assertIs(int(json.loads(res.content)['max_order_price']), 17)
        self.assertIs(int(json.loads(res.content)['min_order_price']), 7)
        self.assertTrue(math.isclose(float(json.loads(res.content)['total_order_price']), float(24)))
        self.assertIs(int(json.loads(res.content)['total_order_item_count']), 7)
