from website import create_app

app = create_app()

'''Debug must be set to false in order to launch the website'''
if __name__ == '__main__':
    app.run(debug=True)