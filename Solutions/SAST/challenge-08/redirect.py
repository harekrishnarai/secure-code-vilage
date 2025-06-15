from flask import Flask, request, redirect, abort

app = Flask(__name__)

@app.route('/go')
def go():
    target = request.args.get('url')
    if not target or not target.startswith('https://example.com/'):
        abort(400)
    return redirect(target)
