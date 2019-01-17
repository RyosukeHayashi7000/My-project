from .models import Category


def common(request):
    """テンプレートに毎回渡すデータ
    　　base.htmlにカテゴリー一覧表示のデータを毎回渡す
       settings.pyのTEMPLATESに追加で処理をかく
    """
    context = {
        'category_list': Category.objects.all(),
    }
    return context