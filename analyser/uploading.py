import re
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug import exceptions
from werkzeug.exceptions import abort

from analyser.auth import login_required
from analyser.db import get_db

from analyser.Uploader.PDFUploader import convert_from_PDF
from analyser.NLPAnalysis.NLPAnalysis import get_sen
from analyser.NLPAnalysis.NLP_kwd import get_kwd
from analyser.NewsIngester.News_Ingester import get_all

bp = Blueprint('uploading', __name__)

@bp.route('/')
def index():
    db = get_db()
    articles = db.execute(
        'SELECT a.id, title, body, sentiment, keyword, uploaded, uploader_id, username'
        ' FROM article a JOIN user u ON a.uploader_id = u.id'
        ' ORDER BY uploaded DESC'
    ).fetchall()
    return render_template('uploading/index.html', articles=articles)

@bp.route('/upload', methods=('GET', 'POST'))
@login_required
def upload():
    if request.method == 'POST':
        file = request.files['filename']
        title = file.filename
        file.save(title)
        body = convert_from_PDF(title)
        sen = get_sen(body) # get sentiment
        kwd = get_kwd(body)
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO article (title, body, uploader_id, sentiment, keyword)'
                ' VALUES (?, ?, ?, ?, ?)',
                (title, body, g.user['id'], sen, kwd)
            )
            db.commit()
            return redirect(url_for('uploading.index'))

    return render_template('uploading/upload.html')

@bp.route('/ingest', methods=('GET', 'POST'))
@login_required
def ingest(keyword=None):
    if request.method == 'POST':
        keyword = request.form['keyword']
        res_number = int(request.form['number'])
        if res_number > 100:
            abort(403, "Number should be no greater than 100.")
        all = get_all(keyword, res_number)
        all_articles = all['articles']
        for article in all_articles:
            title = article['title']
            body = article['content']
            post(title, body, keyword)

        error = None
        if error is not None:
            flash(error)
        else:
            return redirect(url_for('uploading.index'))
        
    return render_template('uploading/ingest.html')

def post(title, body, keyword):
    if request.method == 'POST':
        sen = get_sen(body)
        kwd = keyword
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO article (title, body, uploader_id, sentiment, keyword)'
                ' VALUES (?, ?, ?, ?, ?)',
                (title, body, g.user['id'], sen, kwd)
            )
            db.commit()

def get_article(id, check_uploader=True):
    article = get_db().execute(
        'SELECT a.id, title, body, uploaded, uploader_id, username'
        ' FROM article a JOIN user u ON a.uploader_id = u.id'
        ' WHERE a.id = ?',
        (id,)
    ).fetchone()

    if article is None:
        abort(404, "Article id {0} doesn't exist.".format(id))

    if check_uploader and article['uploader_id'] != g.user['id']:
        abort(403)

    return article

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    article = get_article(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        sen = get_sen(body) # update sentiment
        kwd = get_kwd(body)
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE article SET title = ?, body = ?, sentiment = ?, keyword = ?'
                ' WHERE id = ?',
                (title, body, sen, kwd, id)
            )
            db.commit()
            return redirect(url_for('uploading.index'))

    return render_template('uploading/update.html', article = article)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_article(id)
    db = get_db()
    db.execute('DELETE FROM article WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('uploading.index'))
