from website import create_app

##using the jinja2 template engine
"""
{%....%} conditions for loops, while loops
{{    }} expressions to print output
{#.....#} this is for comments
"""

app = create_app()

if __name__ == '__main__':   #for debugging purposes
    app.run(debug=True) 