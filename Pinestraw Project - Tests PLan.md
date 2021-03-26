**PINESTRAW PROJECT**

PREMISSES:

- View Menu (list of products) - OK 

- Order at coffee shop with options - OK 

- View his order (product list, pricing & order status) - OK

- Change a waiting order - OK 

- Cancel a waiting orders - OK 


*=> TESTS PLAN <=*


PRODUCT

** -> Must be authenticated <- **

- List Products - OK


ORDERS

- Not authenticateduser - OK


** -> Must be authenticated <- **

1- As staff user

- Insert an Order - OK
- List Orders - OK
- Change an Order in Waiting status - OK
- Change an Order in other status - OK
- Exclude an Order - OK

2- As Superuser

- Insert an Order
- List Orders - OK
- Change an Order in Waiting status - OK
- Change an Order in other status - OK
- Exclude an Order with status different of WAITING - OK
- Exclude an Order with status equal to WAITING - OK
