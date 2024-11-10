from flask import Flask, render_template, request, redirect, url_for
class CategoryController:
    @staticmethod
    def getAllCategories():
        return 'фильм'
    
    @staticmethod
    def getCategoriesById():
        return 'фильм по id'
    
    @staticmethod
    def deleteCategoriesById():
        return ' Удалил фильм'
    
    @staticmethod
    def createCategory():
        json_data = request.get_json()
        return json_data
    
    @staticmethod
    def editCategoryByID():
        return 'фильм изменён'