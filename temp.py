# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:56:14 2024

@author: pramo
"""
import joblib
model=joblib.load("churn_predictor.pkl")
model.predict([[0,1,42,0,8,4,1,113945,800,113943,189870]])
