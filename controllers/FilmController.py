from flask import Flask, render_template, request, redirect, url_for
class FilmController:
    @staticmethod
    def getAllFilms():
        return 'фильм'
    
    @staticmethod
    def  getFilmById():
        return 'фильм по id'
    
    @staticmethod
    def deleteFilmById():
        return ' Удалил фильм'
    
    @staticmethod
    def createFilm():
        
        return 'Создал фильм'
    
    @staticmethod
    def editFilmByID():
        return 'фильм изменён'