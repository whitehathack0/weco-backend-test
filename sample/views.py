"""
Views
"""
import json
import traceback

from django.core import serializers
from django.db.models import Max, Sum, F, FloatField
from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import GenericAPIView

# noinspection PyProtectedMember
from rest_framework.permissions import IsAuthenticated

from sample.models import Order, OrderedItem


class OrderListView(GenericAPIView):
    """
    Orders List

    For a GET, returns all orders
    For a POST, creates a new Order
    """

    permission_classes = (IsAuthenticated,)

    # noinspection PyMethodMayBeStatic
    def get(self, request):
        """
        Gets all orders
        """
        # Fill this out.  Should return all orders, JSON encoded

        try:
            orders = Order.objects.all()
            orders_json = serializers.serialize('json', orders)
        except Exception:
            return HttpResponse("Error occurred: " + traceback.format_exc(),
                                content_type='application/json',
                                status=status.HTTP_400_BAD_REQUEST)
        return HttpResponse(orders_json, content_type='application/json', status=status.HTTP_200_OK)

    def post(self, request):
        """
        Creates an Order
        """
        # Fill this out

        try:
            # FOR LOOP
            for order in request.data['orders']:
                print(order)
                new_order = Order()
                new_order.name = order['name']
                new_order.save()

                for item in order['items']:
                    ordered_item = OrderedItem()
                    ordered_item.order_id = new_order
                    ordered_item.name = item['name']
                    ordered_item.sku = item['sku']
                    ordered_item.count = item['count']
                    ordered_item.unit_price = item["unit_price"]
                    ordered_item.save()

        except Exception:
            return HttpResponse("Error occurred: " + traceback.format_exc(),
                                content_type='application/json',
                                status=status.HTTP_400_BAD_REQUEST)

        return HttpResponse(content_type='application/json', status=status.HTTP_201_CREATED)


class OrderStatsView(GenericAPIView):
    """
    Orders Stats

    For a GET, returns order stats
    """

    permission_classes = (IsAuthenticated,)

    # noinspection PyMethodMayBeStatic
    def get(self, request):
        """
        Gets order statistics
        """
        # Fill this out.  Return:
        #                   order count,
        #                   max order price,
        #                   min order price,
        #                   total order price, and
        #                   total order item count.

        statistics = {}
        statistics["order_count"] = str(Order.objects.all().count())
        statistics["max_order_price"] = str(OrderedItem.objects.values('order_id').annotate(total=Sum(F('unit_price') * F('count'))).order_by('-total')[0]['total'])
        statistics["min_order_price"] = str(OrderedItem.objects.values('order_id').annotate(total=Sum(F('unit_price') * F('count'))).order_by('total')[0]['total'])
        statistics["total_order_price"] = str(OrderedItem.objects.aggregate(total=Sum(F('count') * F('unit_price'), output_field=FloatField()))['total'])
        statistics["total_order_item_count"] = str(OrderedItem.objects.aggregate(total=Sum('count'))['total'])

        return HttpResponse(json.dumps(statistics), status=status.HTTP_200_OK)
