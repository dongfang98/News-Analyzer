import re
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug import exceptions
from werkzeug.exceptions import abort

from analyzer.auth import login_required
from analyzer.db import get_db

from analyzer.Uploader.PDFUploader import convert_from_PDF
from analyzer.NLPAnalysis.NLPAnalysis import get_sen
from analyzer.NLPAnalysis.NLP_kwd import get_kwd, find_keyword
from analyzer.NewsIngester.News_Ingester import get_all

bp = Blueprint('uploading', __name__)

@bp.route('/')
def index():
    db = get_db()
    articles = db.execute(
        'SELECT a.id, title, body, sentiment, keyword, uploaded, uploader_id, article_url, username, published, author, para_list'
        ' FROM article a JOIN user u ON a.uploader_id = u.id'
        ' ORDER BY uploaded DESC'
    ).fetchall()
    return render_template('uploading/index.html', articles=articles)

@bp.route('/show')
def show(keyword=None, sentiment=None):
    db = get_db()
    
    articles = db.execute(
        'SELECT a.id, title, body, sentiment, keyword, uploaded, uploader_id, article_url, username, published, author'
        ' FROM article a JOIN user u ON a.uploader_id = u.id'
        ' WHERE sentiment = ? and keyword = ?'
        ' ORDER BY uploaded DESC',
        (sentiment, keyword)
    ).fetchall()
    length = len(articles)
    return render_template('uploading/show.html', articles=articles, length = length)

@bp.route('/upload', methods=('GET', 'POST'))
@login_required
def upload():
    if request.method == 'POST':
        file = request.files['filename']
        title = file.filename
        file.save(title)
        body = convert_from_PDF(title)
        sen = get_sen(body)  # get sentiment
        kwd = get_kwd(body)
        url = ''  # set url '' to repesent not avilable
        published = ''
        author = ''
        # add here
        para_list = find_keyword(body)
        
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO article (title, body, uploader_id, sentiment, keyword, article_url, published, author, para_list)'
                ' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (title, body, g.user['id'], sen, kwd, url, published, author, para_list)
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
            url = article['url']
            published = article['publishedAt']
            author = article['author']
            post(title, body, keyword, url, published, author)

        error = None
        if error is not None:
            flash(error)
        else:
            return redirect(url_for('uploading.index'))
        
    return render_template('uploading/ingest.html')

def post(title, body, keyword, url, published, author):
    if request.method == 'POST':
        sen = get_sen(body)
        kwd = keyword
        url = url
        published = published[0:10]
        author = author
        para_list = find_keyword(body)

        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO article (title, body, uploader_id, sentiment, keyword, article_url, published, author, para_list)'
                ' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (title, body, g.user['id'], sen, kwd, url, published, author, para_list)
            )
            db.commit()

@bp.route('/search', methods=('GET', 'POST'))
@login_required
def search(keyword=None, sentiment=None):
    if request.method == 'POST':
        keyword = request.form['keyword']
        sentiment = request.form['sentiment']
        
        error = None



        if error is not None:
            flash(error)
        else:
            return show(keyword, sentiment)
            # return redirect(url_for('uploading.show'))
            
     
    return render_template('uploading/search.html')

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
        para_list = find_keyword(body)
        print (f"para_list = {para_list}")
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE article SET title = ?, body = ?, sentiment = ?, keyword = ?, para_list = ?'
                ' WHERE id = ?',
                (title, body, sen, kwd, para_list, id)
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