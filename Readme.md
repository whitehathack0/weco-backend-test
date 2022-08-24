# Weco Backend Code Test

Welcome to the Weco code test.  The goal of this test is both to let you show us a bit of what you can do, and also for you to get a feel for what we do on a day-to-day basis.

If you've used Django in the past, and in particular, Django Rest Framework, this should be very straightforward.  Even if you haven't, nothing super advanced is required here, and it shouldn't be too demanding.

## Instructions

Your goal is to fill in the two views referenced in urls.py.  One lists and also creates Orders (and should work with embedded order items) and the second returns generic order statistics.  These are intended to be REST API endpoints (hence the Django REST Framework GenericAPIViews) and should return JSON along with appropriate HTTP status codes.

Currently, thr Order and OrderItem models are not linked in any way.  Your first task is to link them.  There should be a OneToMany relationship between Orders and OrderItems.  One Order can have many Items. 

If you have any questions, please don't hesitate to ask.

Best of luck.

Once you are done, please tar/zip everything up and send it to greg@wecohospitality.com (or just send me a link to a public git repo.)  We'll schedule another call to discuss.

Thanks in advance!

------------------

Sample POST input located in 
```
/weco-backend-test/sample/tests/sample_data/sample_post_data.json
```
```json
{
    "orders" : [
        {
            "name":"aditya",
            "items" : [
                {
                    "name" : "item9",
                    "sku" : "1234lkaje",
                    "count" : 1,
                    "unit_price" : 5.99
                },
                {
                    "name" : "item10",
                    "sku" : "akjsdfh8923",
                    "count" : 1,
                    "unit_price" : 5.00
                },
                {
                    "name" : "item11",
                    "sku" : "alsdkfj8923",
                    "count" : 1,
                    "unit_price" : 2.99
                }
            ]
        },
        {
            "name":"scott",
            "items" : [
                {
                    "name" : "item7",
                    "sku" : "asdjkfas889",
                    "count" : 1,
                    "unit_price" : 1.00
                },
                {
                    "name" : "item6",
                    "sku" : "asdjkfas89dfy",
                    "count" : 1,
                    "unit_price" : 10.00
                },
                {
                    "name" : "item5",
                    "sku" : "899899sdf",
                    "count" : 1,
                    "unit_price" : 7.00
                }
            ]
        }
    ]
}
```






