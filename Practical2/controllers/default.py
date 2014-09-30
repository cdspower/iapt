# -*- coding: utf-8 -*-
# @IAPT: Very simple controller

def index():
    return dict(features=db(db.products.id==db.features.product_id).select())
