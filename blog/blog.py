from flask import Blueprint, render_template
from config import blue_prints

blog = Blueprint("blog", __name__, url_prefix='/blog', template_folder="templates", static_folder="static")


@blog.route('/')
def blog_read():
    """здесь специально создана ошибочная ситуация, в реальности это может быть например не полученная по api с другого
    сайта информация, неверно введенные данные или ещё какая то непредвиденная (или предвиденная ошибка), то несмотря
    на это все остальные части сайта продолжают работать, а в этой акуратно печатается сообщение об ошибке или о том
    что данный блок сайта временно не работает"""
    try:
        print(5 / 0)
        return render_template("blog/index.html", status="Blog", blue_prints=blue_prints)
    except Exception as err:
        print(err)
        return render_template("blog/index.html", status="Error", blue_prints=blue_prints)
