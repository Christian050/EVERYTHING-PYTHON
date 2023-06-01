'''
Packages are another way to organize code

A package is a container of multiple modules.

It's a directory or folder.
'''

import Ecommerce.shipping

Ecommerce.shipping.calc_shipping()


# OR

from Ecommerce.shipping import calc_shipping

calc_shipping()


# OR

from Ecommerce import shipping

shipping.calc_shipping()